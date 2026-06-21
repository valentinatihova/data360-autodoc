# API Reference (assumed shapes)

> **Status: ASSUMED, not yet verified against a live org.**
> No real Data 360 payloads were available when these clients were written, so
> the response shapes below are reasonable assumptions. Tests mock exactly these
> shapes (`responses` library). When you capture real payloads, reconcile them
> here and adjust the `from_api` / `from_metadata` helpers in `models.py` — the
> downstream generators consume `OrgSchema`, so they should not need changes.

## 1. Auth — JWT Bearer token exchange

`POST {instance_url}/services/oauth2/token`

Form body:

| field        | value                                                        |
| ------------ | ------------------------------------------------------------ |
| `grant_type` | `urn:ietf:params:oauth:grant-type:jwt-bearer`                |
| `assertion`  | signed RS256 JWT (`iss`=client_id, `sub`=username, `aud`, `exp`) |

Success (`200`):

```json
{
  "access_token": "00D...!AQ...",
  "instance_url": "https://mydomain.my.salesforce.com",
  "token_type": "Bearer"
}
```

- `aud` claim is `https://login.salesforce.com` (production) or
  `https://test.salesforce.com` (sandbox).
- `4xx` → terminal (bad assertion/config); `5xx`/transport → retried 3× with
  1s/2s/4s backoff.

## 2. Org metadata catalog

`GET {instance_url}/api/v1/metadata/`

One **page** of the catalog. Pagination via `nextPageUrl` (absolute or relative,
`null`/absent on the last page); `totalSize` is the grand total across pages.

```json
{
  "orgName": "Acme Data Cloud",
  "totalSize": 1240,
  "nextPageUrl": "/api/v1/metadata/?page=2",
  "dmos": [
    {
      "name": "Individual__dmo",
      "label": "Individual",
      "fields": [
        { "name": "Id__c", "type": "Text", "isKey": true },
        { "name": "FirstName__c", "type": "Text" }
      ]
    }
  ],
  "dlos": [
    {
      "name": "Order_Home__dll",
      "label": "Order (Home)",
      "fields": [
        { "name": "OrderId", "type": "Text", "isKey": true }
      ]
    }
  ],
  "cios": [
    {
      "name": "CLV__cio",
      "label": "Customer Lifetime Value",
      "dimensions": ["Individual__dmo.Id__c"],
      "measures": ["TotalSpend"]
    }
  ],
  "identityResolutionRulesets": [
    {
      "name": "Default_Ruleset",
      "label": "Default Ruleset",
      "matchRules": ["Exact Email", "Fuzzy Name + Address"],
      "reconciliationRule": "Most Recent"
    }
  ],
  "mappings": [
    { "sourceDlo": "Order_Home__dll", "targetDmo": "Individual__dmo" }
  ]
}
```

Collections may be absent on a given page; only `mappings`, `dmos`, `dlos`,
`cios`, and `identityResolutionRulesets` are merged across pages.

## 3. DLO schema (per-DLO detail)

`GET {instance_url}/services/data/v62.0/ssot/metadata/dlo/{name}`

```json
{
  "name": "Order_Home__dll",
  "fields": [
    { "name": "OrderId", "type": "Text", "keyQualifier": "PrimaryKey" },
    { "name": "Amount", "type": "Number" }
  ]
}
```

- `keyQualifier` present ⇒ the field is treated as a key (`FieldDef.is_key`).
