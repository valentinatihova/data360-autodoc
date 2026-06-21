# Launch post templates

Two channels, two tones. Fill the `[brackets]`. Keep the GitHub link consistent.
Repo: https://github.com/valentinatihova/data360-autodoc

---

## LinkedIn

Tone: personal, problem-first, a little bold. Hook in line one (LinkedIn
truncates after ~3 lines, so the hook has to land before "...see more").

> I got tired of spending the first two days of every Salesforce Data Cloud
> engagement writing the same documentation by hand.
>
> So I built **data360-autodoc** — an open-source CLI that points at a Data 360
> org and generates the whole thing in seconds:
>
> • A full DMO/DLO data dictionary (fields, types, keys)
> • An ERD of your DLO → DMO mappings
> • A deterministic JSON snapshot of the org schema
>
> One command. No more copy-pasting field lists into a Google Doc that's stale by
> the time the client reads it.
>
> It's free and open-source (MIT). The deterministic snapshot is also the
> foundation for what's next: drift monitoring — re-run on a schedule and get a
> client-ready changelog of exactly what changed in the org.
>
> If you do Data Cloud / Data 360 consulting, I'd love your feedback. Link in
> comments 👇
>
> #Salesforce #DataCloud #Data360 #SalesforceConsulting #OpenSource

**First comment (put the link here, not in the post — LinkedIn down-ranks
posts with outbound links in the body):**
> GitHub: https://github.com/valentinatihova/data360-autodoc — try it on a Dev
> Edition org first, it works against any org you can auth a connected app to.

---

## Trailblazer Community — Data Cloud group

Tone: helpful, community-first, no hard sell. Trailblazer norms reward "I made
a thing that might help you" over marketing. Lead with the shared pain.

**Title:** Open-source CLI to auto-generate Data 360 org documentation (DMO/DLO dictionary + ERD)

**Body:**

> Hey all — sharing a free tool in case it saves someone the same hours it was
> costing me.
>
> Documenting a Data 360 org (DMOs, DLOs, fields, identity resolution rules,
> calculated insights) by hand is slow and goes stale fast. I built
> **data360-autodoc**, an open-source Python CLI that generates it for you:
>
> - Markdown data dictionary — every DMO/DLO with fields, types, and keys
> - A Mermaid ERD of DLO → DMO mappings (renders right in GitHub)
> - A deterministic JSON snapshot of the schema
>
> Auth is the standard JWT Bearer flow (connected app + private key, no passwords
> stored), and it works against Developer Edition / Data Cloud Dev orgs so you can
> try it safely.
>
> Quick start:
> ```
> pip install data360-autodoc
> data360-autodoc generate --instance-url ... --client-id ... \
>   --private-key ./server.pem --username ... --format all
> ```
>
> Repo (MIT): https://github.com/valentinatihova/data360-autodoc
>
> It's early — would genuinely love feedback on what fields/metadata you'd want
> covered next, and whether the ERD matches how you think about your mappings.
> Roadmap includes drift monitoring (diff two snapshots to see what changed in an
> org over time).
>
> Happy to answer questions here. 🙏
