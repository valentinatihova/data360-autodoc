# Demo GIF script (10–15 seconds)

A tight terminal-to-editor loop that shows the whole value in one breath. Script
only — record the GIF later. Target length **12s**, hard cap 15s. No audio.

## Setup (before recording)

- Clean terminal, large readable font (≥ 18pt), dark theme.
- Pre-fill the command in shell history (press ↑ to recall) so there's no typing
  fumble — or use a typing-animation tool.
- Have a real (or realistic mock) org so the output is genuine.
- Editor open in the background with the output folder, Markdown preview ready.

## Shot list

| Time | Shot | What happens |
|------|------|--------------|
| 0.0–2.0s | **Terminal** | The `data360-autodoc generate ... --format all` command is visible on the prompt. |
| 2.0–4.5s | **Run** | Hit Enter. The `Wrote ...` lines and the summary `Generated docs for 12 DMOs, 8 DLOs, 3 Identity Rulesets` print. |
| 4.5–7.0s | **Switch to editor** | Open `acme-data-cloud.md` — the H1 title + first DMO table render in Markdown preview. |
| 7.0–10.0s | **Scroll** | Smooth scroll down through a fields table and into the Mermaid ERD, which renders as an actual diagram. |
| 10.0–12.0s | **Hold** | Rest on the ERD for a beat. Optional end card: `data360-autodoc · pip install data360-autodoc`. |

## Direction notes

- **One continuous feel.** No jump cuts mid-action; the cut from terminal to
  editor should feel like "and here's the result," ~0.3s.
- **Let the output be the hero.** The point is "I ran one command and got a
  real document." Don't over-narrate with captions.
- **Loop-friendly:** end on the ERD, start on the prompt — it reads fine on
  auto-loop for social.
- Export at 2x for retina; keep under ~5 MB so it inlines in the README and on
  social without transcoding.
