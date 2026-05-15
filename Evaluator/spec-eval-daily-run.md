---
title: Daily Compliance Eval — Run Procedure
created: 2026-05-08
type: spec
---

# Daily Compliance Eval — Run Procedure

Step-by-step instructions for the Evaluator agent to run a compliance assessment across all customer-facing calls on a given date using Fireflies.

## Inputs

| Input | Source |
|---|---|
| Target date | User-supplied (ISO 8601: `YYYY-MM-DD`) |
| Detection criteria | `Researcher/req-detection-criteria.md` |
| MCC register | `Researcher/research-mcc-fitness-probity.md` |

## Step 1 — List customer-facing calls

Call `fireflies_get_transcripts`:
```
fromDate: "<target-date>"
toDate:   "<target-date>"
limit: 50
format: "json"
```

From the returned list, keep meetings where at least one participant email domain is **not** `kota.io`. Discard internal-only meetings (standups, team syncs, 1:1s where all participants are `@kota.io`).

Log: `N meetings returned; M customer-facing after filter`.

## Step 2 — Fetch full transcripts

For each retained meeting ID, call `fireflies_get_transcript(transcriptId)`.

Extract:
- `sentences[]` — array of `{speaker_name, text, start_time}` objects
- `participants[]` — list with name and email
- `duration` — call length in minutes

## Step 3 — Identify Kota-side speakers

From `participants`, identify all `@kota.io` email addresses as the Kota-side speakers. Non-kota.io participants are customers — do not apply MCC detection to customer speech.

For each Kota-side speaker, resolve their authorisation status from the MCC register:

| Name | Status | Product scope |
|---|---|---|
| Trevor Gardiner | ✅ Qualified | All (QFA, APA PGI) |
| Patrick O'Boyle | ✅ Qualified | Pensions, Health, Life |
| Paul O'Hanlon | ✅ Qualified | Health (PMI), Pensions |
| Naoise Baker | ✅ Qualified | Health (PMI) |
| Colin Pon | ✅ Qualified | Health (PMI) |
| Charlie Blake | ✅ Qualified | Health (PMI) |
| Callum Pearse | ✅ Qualified (Pensions) / ⚠️ New Entrant (PMI) | Pensions independent; PMI supervised |
| Daniel McAvinue | ✅ Qualified (Pensions, Life) / ⚠️ New Entrant (PMI) | Pensions/Life independent; PMI supervised |
| Matthew Brennan | ⚠️ New Entrant | Must act under direction of Trevor Gardiner |
| Henry Godson | ❌ Script pathway | Script only; supervised by Trevor |
| Katie Garry | ❌ Script pathway | Script only; supervised by Trevor |
| Will Robbins | ❌ Script pathway | Script only; supervised by Trevor |
| Simon Ward | ❌ Script pathway | Script only; supervised by Trevor |
| Claudia Correa | ❌ Script pathway | Script only; supervised by Trevor |
| Karl O'Brien | ❌ Script pathway | Script only; supervised by Trevor |
| Kate Fullen | ❌ Unregistered | Cannot conduct regulated activity |
| Any unrecognised speaker | ❌ Unqualified (default) | None |

## Step 4 — Apply detection criteria

Scan each Kota-side speaker's sentences against `Researcher/req-detection-criteria.md`.

**Hard rules (HF-00 through HF-12)** — flag any match immediately:

| Criterion | What to look for |
|---|---|
| HF-00 | Unqualified/script/New-Entrant speaker providing advice OR product information OR arranging. Compare against MCC carve-outs (pointing to FAQ, general non-product info, brochure pass-through) — those are NOT breaches. |
| HF-01 | Explicit recommendation: "I recommend", "you should", "best thing to do", "what might be best for you" |
| HF-02 | Comparative value judgement: "so superior", "much better than", "98% of clients do this" |
| HF-03 | Misrepresented firm role / capability / regulatory status: "we go to market for best quotes", "we're global", "qualified financial advisor" |
| HF-04 | Cross-selling / arranging regulated product without authorisation: offering to get a quote for life, IP, pension when not authorised |
| HF-05 | Tax / AE / public-law conclusion applied to specific scenario, **OR misstating the public-law rules** — any Irish auto-enrolment claim (percentage, eligibility, phasing, opt-out, contribution base) that diverges from `Researcher/source-of-truth-ae-myfuturefund.md`. If that file is empty for the relevant section, fail closed (flag with note "AE source-of-truth missing"). |
| HF-08 | Absolute certainty claim: "everything's covered", "full cover", "won't lose cover", "can be certain" |
| HF-09 | GDPR / PII mishandling: agreement to receive personal data (PPS numbers, salary, DOB, addresses) by unprotected channel |
| HF-10 | Unqualified speaker describing **mechanics, cover, or terms** of a regulated product — cover, excesses, **underwriting (moratorium / MHD / virgin scheme), premium mechanics (age-rated), non-AE pension mechanics (occupational contributions, BIK, fund composition), claims process**. **Auto-enrolment is carved out** — any speaker may discuss AE, but statements must match the gov.ie source (deviations are HF-05, not HF-10). |
| HF-11 | Unqualified speaker comparing two Kota plans or Kota vs competitor plans |
| HF-12 | Unqualified speaker discussing changing or amending level of cover |
| HF-13 | Unqualified speaker discussing pricing, premiums, or pricing trends of a regulated product (specific amounts, "X is cheaper", "prices will go down"). Kota's own platform fee (€9 PEPM) is **not** in scope. |
| HF-14 | Disclosure of confidential client, partner, or third-party information — naming clients, sharing their setup, churn, complaints, or disparaging Kota's partners/providers in front of a prospect |
| HF-15 | Unqualified speaker discussing fund or product performance / returns — "Aviva and Zurich are the highest performing", "Smart Pension isn't market-leading" |

> **Excluded — recording/call consent**: HF-06 (recording disclosure opener) and HF-07 (implied/assumed recording consent) are **not** detection criteria. Kota collects recording consent via a booking form when prospects and customers schedule the call. The agent must not flag the absence of a verbal recording disclosure, an implied "I'm assuming that's okay", or any related opener-script issue.

**Soft signals (SF-10 through SF-15)** — note; escalate only if N≥2 or co-occurring with an HF:

| Criterion | What to look for |
|---|---|
| SF-10 | Circumvention language: "set 1% so they don't fall into My Future Fund", "ways around" |
| SF-11 | Inducement / commission framing: "you can start making money", promotional commission talk |
| SF-12 | Emotive / marketing language: "wild west", "all good news", "good news story" |
| SF-13 | Disparaging a competitor product or provider |
| SF-14 | "At the moment" hedging on regulatory rules |
| SF-15 | Social proof anchoring without evidence: "all our clients do X" |

**Escalation signals (ES-01 through ES-03)** — flag for immediate human review:

| Criterion | What to look for |
|---|---|
| ES-01 | Customer expresses distress, complaint, or explicit dissatisfaction |
| ES-02 | Speaker mentions a claim, coverage dispute, or potential liability |
| ES-03 | Speaker agrees to an action (e.g. sending data, changing cover) that is outside authorised scope |

## Step 5 — Grade each call

Use the human reviewer's 1–5 rubric from `Researcher/research-call-supervision-audit.md`:

| Grade | Label | Criteria |
|---|---|---|
| 5 | Severe Fail | Customer misled on firm capability, scope, or a material fact |
| 4 | Fail w/ referral | Repeated explicit recommendations (HF-01) or unauthorised regulated activity (HF-00, HF-04) |
| 3 | Fail | Single clear breach of advice perimeter, MCC scope, or PII handling |
| 2 | Pass with comments | Language hygiene (HF-08), soft signals (SF-12, SF-13, SF-14) — documented in eval report only; **no Asana task** |
| 1 | Pass | No findings; operational / admin call |

## Step 6 — Write the eval report

Create `Evaluator/eval-<YYYY-MM-DD>-daily.md` following the template in `CONTEXT.md`.

Required for each flagged utterance:
- Criterion ID
- Severity (High / Medium / Low)
- Speaker name + authorisation status
- Timestamp (MM:SS)
- Exact transcript span (do not paraphrase)
- Applicable regulation

## Notes for edge cases

**Script-pathway speaker but no supervisor present**: Flag under HF-00 (unqualified speaker conducting regulated activity) if they discuss product details. Note absence of supervised call structure.

**Qualified speaker discusses product outside their scope**: Flag under HF-00 — e.g. an APA PMI holder discussing pension contribution strategy is out of scope.

**Call is entirely operational** (e.g. onboarding tech walkthrough, billing, password reset): Grade 1 (Pass), note as negative-class example.

**Call language is ambiguous**: Quote the span, assign the closest criterion, and add a note in "Open Questions for the Designer" so the criterion can be tightened.
