# API Reference

> **Status: VERIFIED against the Data 360 Connect REST API.**
> The endpoints and shapes below are the real ones the tool calls (derived from
> working Apex against a live Data Cloud org). The fetchers assemble these into
> an `OrgSchema`; the generators consume `OrgSchema`, so adding/adjusting an
> endpoint only touches `fetcher/*` and this file.

All metadata calls are the **Data 360 Connect REST API** under the standard
Salesforce domain (`{instance_url}/services/data/{version}/ssot/...`), authorized
with the JWT access token as a `Bearer` token. There is **no** single
`/api/v1/metadata/` call (that endpoint exists in the separate Data Cloud Query
API on a different tenant host and needs a token exchange — not used here).

## 1. Auth — JWT Bearer token exchange

`POST {token_url}` — default `https://login.salesforce.com/services/oauth2/token`
(production) or `https://test.salesforce.com/services/oauth2/token` (sandbox, via
`--sandbox`).

| field        | value                                                            |
| ------------ | ---------------------------------------------------------------- |
| `grant_type` | `urn:ietf:params:oauth:grant-type:jwt-bearer`                    |
| `assertion`  | signed RS256 JWT (`iss`=client_id, `sub`=username, `aud`, `exp`) |

Success (`200`) returns `access_token` and `instance_url`. `4xx` is terminal
(bad assertion/config); `5xx`/transport are retried 3× with 1s/2s/4s backoff.

## 2. API version detection

`GET {instance_url}/services/data/`

Returns the list of REST API versions the org supports:

```json
[ { "version": "62.0", "url": "/services/data/v62.0" },
  { "version": "66.0", "url": "/services/data/v66.0" } ]
```

The tool picks the **numerically highest** version and uses it for every
`/ssot/*` call. If discovery fails or returns nothing, it falls back to a floor
(`v62.0`). `--api-version` overrides detection entirely (see the CLI section).

## 3. Data Model Objects (DMOs)

`GET .../v{version}/ssot/data-model-objects?limit=500`

```json
{
  "dataModelObject": [
    { "name": "Individual__dmo", "label": "Individual", "isEnabled": true }
  ],
  "nextPageUrl": "/services/data/v66.0/ssot/data-model-objects?page=2"
}
```

- Paginated via `nextPageUrl` (absolute or relative; absent on the last page).
- `isEnabled: false` entries are filtered out.
- Capped at **500** DMOs; if the org has more enabled DMOs, a `WARNING` is logged
  and the rest are omitted.

## 4. DLO → DMO mappings (per DMO)

`GET .../v{version}/ssot/data-model-object-mappings?dataspace={ds}&dmoDeveloperName={name}`

```json
{
  "objectSourceTargetMaps": [
    {
      "sourceEntityDeveloperName": "Order_Home__dll",
      "targetEntityDeveloperName": "Individual__dmo",
      "fieldMappings": [ { "targetFieldDeveloperName": "Email__c" } ]
    }
  ]
}
```

- `sourceEntityDeveloperName` (DLO) → `targetEntityDeveloperName` (DMO) becomes a
  `Mapping` (deduplicated across DMOs).
- `fieldMappings[].targetFieldDeveloperName` becomes a DMO field with type
  `Unknown` (type comes from relationships, below).

## 5. DMO relationships + field types (per DMO)

`GET .../v{version}/ssot/data-model-objects/{name}/relationships?dataspace={ds}&limit=500`

Verified shape (live org, v67.0). Each relationship is self-describing via
nested `sourceObject`/`targetObject`; the queried DMO may be **either** side:

```json
{
  "relationships": [
    {
      "cardinality": "ManyToOne",
      "status": "INACTIVE",
      "name": "Account_PrimarySalesContactPointId_map_ContactPointEmail_Id_N_1_…",
      "sourceObject": { "name": "ssot__Account__dlm", "label": "Account" },
      "sourceField":  { "name": "ssot__PrimarySalesContactPointId__c", "type": "MktDataModelField" },
      "targetObject": { "name": "ssot__ContactPointEmail__dlm", "label": "Contact Point Email" },
      "targetField":  { "name": "ssot__Id__c", "type": "MktDataModelField" }
    }
  ]
}
```

- Paginated via `nextPageUrl`.
- **Relationship rows (Relationships section):** built straight from
  `sourceObject`/`targetObject` + `cardinality` (normalized `ManyToOne` → `N:1`).
  `status` is surfaced; inactive standard relationships are kept, not dropped.
- **Field types:** only the side that IS the queried DMO contributes a typed
  field, and only when `status == "ACTIVE"` (or absent). In practice these types
  are generic (`MktDataModelField`), so the real DMO type source is the mapped
  DLO field type (see `_enrich_dmo_field_types`).

## 6. Data Lake Objects (DLOs), from data streams

`GET .../v{version}/ssot/data-streams`

DLOs are not a separate endpoint — they come from each stream's
`dataLakeObjectInfo`:

```json
{
  "dataStreams": [
    {
      "dataLakeObjectInfo": {
        "name": "Order_Home__dll",
        "label": "Order (Home)",
        "dataLakeFieldInfoRepresentation": [
          { "name": "OrderId", "dataType": "Text", "isPrimaryKey": true },
          { "name": "Amount", "dataType": "Number" }
        ]
      }
    }
  ]
}
```

- Paginated via `nextPageUrl`.
- A DLO referenced by multiple streams is emitted once (first occurrence wins).
- `isPrimaryKey: true` → `is_key=True` and `key_qualifier="PrimaryKey"`.

## 7. Assembly into OrgSchema

- **DMOs:** name + label from §3; fields = relationship types (§5) merged with
  mapping target fields (§4), relationship types winning.
- **DLOs:** name + label + fields from §6.
- **Mappings:** DLO→DMO from §4.
- All collections sorted alphabetically → deterministic output.

**Not fetched yet (future):** Calculated Insights and Identity Resolution
rulesets. `OrgSchema` has fields for both, but no endpoint populates them today,
so they stay empty and their document sections render as empty placeholders
(`_No Calculated Insights found._` / `_No Identity Resolution Rules found._`).
Note: Engagement and Profile DMOs **are** covered — those are DMO *categories*,
returned by the DMO and data-stream endpoints above, not separate entities.

## 8. Failure behavior

- Any request: `4xx` terminal; `5xx`/transport retried 3× (1s/2s/4s); a `200`
  with a non-JSON body is treated as an error. All become a `FetchError`.
- **Fatal** (the document can't be built): a failure on the **DMO list** (§3) or
  **data streams** (§6) → `MetadataError` → the CLI prints a clean one-line
  `Error:` and exits non-zero (never a traceback).
- **Non-fatal** (the document is still produced): a per-DMO failure on **mappings
  (§4)** or **relationships (§5)** → that DMO is skipped with a `WARNING`, and
  the rest of the org is documented. A summary `WARNING` reports how many were
  skipped.
- **Truncation:** more than 500 enabled DMOs → `WARNING` and the rest omitted.

Warnings are emitted on the module logger and surface on stderr.
