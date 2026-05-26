---
title: Evaluator Calibration — False-Positive Analysis 2026-05-15
created: 2026-05-15
type: calibration
covers_runs:
  - eval-2026-05-05-weekly.md
  - eval-2026-05-08-karl-obrien.md
  - eval-2026-05-12-to-2026-05-15.md
---

# Evaluator Calibration — False-Positive Analysis (2026-05-15)

This note captures every false positive surfaced across the May 2026 eval runs, the root-cause categories they fall into, and the specific refinements that go into the agent's instructions to reduce false positives on future runs.

## False positives identified

| # | Call | Criterion as flagged | Verbatim quote | Why it was wrong |
|---|---|---|---|---|
| 1 | LearnUpon #2 (2026-05-15) | HF-05 | Simon Ward: *"1.5 employer, 1.5 employee and 0.5 state top"* | Exactly matches gov.ie Year 1–3 AE split. Correct statement, no breach. |
| 2 | 365 Finance (2026-05-12) | HF-10 | Paul O'Hanlon: *"3.5% between employer and employee... won't be re-enrolled into auto enrollment"* | Matches gov.ie Pensions Authority occupational-scheme exemption standard verbatim ("minimum total contribution rates must be 3.5% of an employee's gross pay, with a minimum of 1.5% from the employer"). |
| 3 | Riot Games (2026-05-07) | HF-00 (×2) | Katie Garry: *"Nico, sorry, just with regards to your renewals, are you involved with that?"* and *"So we have 50 in total. And then in the Dublin office, I think at the moment we have about 20 in"* | Sales discovery (asking prospect about their internal structure) + Kota intro headcount. Neither is regulated product talk. Whole call regraded Grade 3 Fail → Grade 1 Pass; Asana task deleted. |
| 4 | Carwow (2026-05-08) | HF-00 | Simon Ward: *"I'm sure you're aware Edan, that Matthew moved to the GM platform role"* | Internal Kota org-chart comment. Not a regulated product. Finding removed from task; call stays Grade 3 on other findings (Dan's HF-02 × 3 + ES-01/02). |
| 5 | 13 calls (2026-05-05 week) | HF-06 | "no recording disclosure opener in first 60 seconds" | Kota collects recording consent via the **pre-call booking form**, not verbally during the call. Criterion removed from the spec entirely. 5 Grade 2 calls regraded to Grade 1; 5 Asana tasks deleted. |
| 6 | Karl/India + Karl/Andrew Moore | HF-10 | Karl: *"3.5%... at a minimum the employer has to offer 1.5%"* | Ambiguous: matches gov.ie's Pensions Authority occupational-scheme exemption standard, but also overlaps with AE total. Reclassified HF-05 borderline rather than HF-10. |
| 7 | Simon AE "taxable income" (LearnUpon #1, #2) | HF-10 | Simon Ward: *"3.5% of total taxable pay" / "based on their total taxable income"* | Principle correct (gross-earnings-based contribution with €80k cap), but used "taxable income" — a different figure under Irish tax law. Reclassified HF-05 light rather than HF-10. |
| 8 | 365 Finance (2026-05-12) | HF-05 (×2) | Paul O'Hanlon discussing private-pension tax relief and 40% relief at €45k | Paul holds **QFA** (covers all retail products in Ireland) plus APA PMI. The agent was applying "APA PMI only" status. Both findings withdrawn. |
| 9 | Forest x Kota (2026-05-14) | HF-10, HF-11, HF-13 (Grade 3) | Callum Pearse discussing PMI anti-selection, cash-plan vs PMI comparison, PMI provider pricing | Callum holds APA Pensions + New Entrant PMI. Per Kota's interpretation of New Entrant arrangements, he can discuss PMI products. All three speaker-scoped findings withdrawn; call regraded Grade 3 → Grade 1; task deleted. |
| 10 | Digilab (2026-05-14) | HF-05, HF-10, HF-13 (Grade 3) | Callum Pearse on PMI salary-sacrifice, BIK / P11D, pension cost-saving percentages | Same issue as #9 — Callum qualified for pensions + PMI. All three findings withdrawn; call regraded Grade 3 → Grade 1; task deleted. |
| 11 | GA Agency (2026-05-11) | HF-00, HF-00/HF-13, HF-10 (Grade 3) | Matthew Brennan discussing regulated product scope, PMI premium ranges, group-scheme mechanics without Trevor on call | Matthew has been **upgraded** — he now holds APA Pensions + APA Life + New Entrant PMI (was previously New Entrant only). Same level as Callum/Dan. All three findings withdrawn; call regraded Grade 3 → Grade 1; task deleted. Flagged by Sola Olaniyan 2026-05-26. |
| 12 | Gorilla (2026-05-11) | HF-00 (Grade 3 + ES-03 escalation) | Slav Stankov (unrecognised) self-introducing as "responsible for benefits integration" and saying "we were also exploring" the salary-sacrifice space | Slav was on the call in a **learning / product-research capacity**, not advising the customer. Self-introductions about role and product research are not regulated activity. New pattern; new rule (R7) added. Call regraded Grade 3 → Grade 1; task deleted. Flagged by Sola Olaniyan 2026-05-26. |

## Root causes — 5 patterns

### Pattern 1: Speaker-presence vs speaker-content
The agent flagged unqualified speakers for being *on* a call that touched regulated products, regardless of whether the specific person discussed regulated products. The correct test is whose mouth the words came out of.

**Examples**: Riot Games (Katie's BDR sales-discovery question), Carwow (Simon's org-chart line about Matthew's role change).

**Cost**: Two Grade 3 Fails were issued where no actual breach occurred; one entire task deleted.

### Pattern 2: Over-broad HF-10 — "any pension/insurance mention by an unqualified speaker is a breach"
The original HF-10 wording treated all pension and AE mechanics as restricted product information. But AE is **public-policy information**, not Kota product information. Anyone can discuss it — the breach is only when statements diverge from the gov.ie source-of-truth.

**Examples**: All of Simon Ward's AE flags this week (LearnUpon #1, #2, capeMBX Health), all of Karl O'Brien's AE flags (Andrew Moore, India Healy O Connor), Paul O'Hanlon's AE flag on 365 Finance.

**Cost**: Two findings withdrawn as exactly correct (Simon "1.5+1.5+0.5"; Paul "3.5% / 1.5% employer"); five reclassified from "out-of-scope" (HF-10) to "wrong" (HF-05 confirmed) or "terminology off" (HF-05 light).

### Pattern 3: Transcript-detectable ≠ actual breach
HF-06 ("no recording disclosure opener") was a synthetic criterion that didn't map to Kota's actual operating model. Kota collects consent on the booking form before the call begins; the verbal disclosure was never the basis for legal consent.

**Examples**: HF-06 fired on 13 of 16 calls in the 2026-05-05 week.

**Cost**: 5 Grade 2 calls dropped to Grade 1 (DailyPay, Frontiers, Voltalis, Gabriela, Allianz White Label); 5 Asana tasks created then deleted.

### Pattern 4: No charitable-interpretation pass before flagging
Multiple Irish AE statements (Karl's "3.5%", Paul's "3.5% between employer and employee", Simon's "1.5+1.5+0.5") have **two valid gov.ie interpretations** — the AE Year 1–3 contribution split, and the Pensions Authority occupational-scheme exemption standard. The agent picked the AE interpretation and flagged whenever the numbers didn't fit it, missing that the speaker may have meant the exemption standard.

**Cost**: Two findings withdrawn as correct after the source-of-truth comparison.

### Pattern 5: No severity distinction within HF-05
"Wrong rule entirely" (Simon's *"2% employee contribution mandate"* — gov.ie says 1.5%) and "right principle, wrong terminology" (Simon's *"taxable income"* — should be "gross earnings") were both stamped HF-05 at the same severity. Compliance treats these very differently in practice — the first is a customer-misled-on-material-fact issue, the second is a wording-clarity issue.

**Cost**: Compliance triage time is wasted on light findings that are flagged at the same level as confirmed errors.

### Pattern 6: Qualification register out of sync with reality
The agent's input register for speaker qualifications had errors that led to false-positive flags:

- **Paul O'Hanlon** was treated as "APA PMI only" — in reality he holds **QFA & APA PMI**. QFA covers all retail product advice in Ireland, so Paul is qualified to discuss pensions, life, PMI, and tax-relief topics independently.
- **Callum Pearse** was treated as "Pensions independent; Health (supervised)" with the supervised qualifier interpreted as "Trevor must be on the call". In reality Callum holds APA Pensions + New Entrant PMI, and Kota's interpretation of his New Entrant arrangement permits him to discuss PMI products without Trevor on the call.
- **Matthew Brennan** was treated as "New Entrant only — pursuing QFA, cannot conduct independent regulated activity" — in reality he now holds **APA Pensions + APA Life + New Entrant PMI** (upgraded 2026-05-26). Same scope as Callum and Dan: qualified for pensions and life independently, PMI under New Entrant arrangement.

**Cost**: 365 Finance dropped from 4 findings to 1; Forest x Kota and Digilab regraded G3 → G1; **GA Agency regraded G3 → G1 (Matthew upgrade); 8 false-positive findings withdrawn in total across four calls.**

### Pattern 7: Speaker on call in learner / observer / research capacity, not advisory
HF-00 was firing on speakers who appeared on calls in non-advisory capacities. The current HF-00 test is "unqualified speaker discussing a regulated product" — but "discussing" was being interpreted to include things that are not advice:

- **Self-introductions about role** ("I'm responsible for benefits integration related to health and salary sacrifices") — this is a job-title statement, not regulated activity.
- **Product research / competitive intel** ("we were also exploring [salary-sacrifice provider] X") — Kota learning what the customer uses or what the market does.
- **Observer participation** — staff sitting in on a call where a qualified colleague is leading the regulated content.

**Example**: Slav Stankov (unrecognised) on the Gorilla call was flagged HF-00 for his self-introduction and product-research statements. Sola Olaniyan flagged this as a false positive — Slav was learning, not advising.

**Cost**: 1 false positive on the Gorilla call (Grade 3 task deleted; the entire ES-03 → Simon Ellis escalation was unwarranted).

## Refinements going into the agent

### R1 — Speaker-content binding (always)
Every finding must name **the specific speaker who said the specific quote**, and the quote must contain the regulated product content. Do not flag a qualified colleague's presence on the call. Do not flag a speaker for being on a call where regulated products were mentioned by someone else. The format is: `[Criterion]: [Speaker X] said "[verbatim quote about product Y]"`.

### R2 — Charitable-interpretation pass on AE quotes
Before tagging HF-05 on an AE statement, the agent compares the speaker's quote against **all** relevant gov.ie sections in `Researcher/source-of-truth-ae-myfuturefund.md`:
- Section 3 (eligibility)
- Section 4 (contribution rates + Year 1–3 split)
- Section 5 (contribution base + 80k cap)
- The "minimum-contribution standards for existing occupational schemes" subsection (Pensions Authority 3.5% exemption standard)
- Section 7 (opt-out and suspension)

If **any** section makes the statement correct under a reasonable reading, do not flag. Only flag when no section supports the statement.

### R3 — HF-05 severity ladder
The agent distinguishes:
- **HF-05 confirmed**: wrong number, wrong rule, wrong eligibility threshold, wrong phasing year. The customer has been told a specific fact that contradicts gov.ie.
- **HF-05 light**: right principle, wrong terminology (e.g. "taxable income" vs "gross earnings"); minor inaccuracy on a mechanic that doesn't change the customer's takeaway.

Compliance escalation logic stays unchanged — HF-05 confirmed at Simon Ellis routing severity; HF-05 light is documented for coaching but doesn't auto-escalate on its own.

### R4 — Document Kota's actual processes (so the agent doesn't flag what's handled elsewhere)
The following Kota processes are **NOT** transcript-detectable findings, because they happen outside the call:
- **Recording consent** — collected on the booking form, before the call.
- **Broker-of-record paperwork** — separate signed documents, not verbal commitments on the call.
- **Internal Slack BDR-to-AE handoff** — happens in Slack, not on the call.

If the agent sees these patterns missing from the transcript, that is **not** a finding.

### R5 — Track withdrawn findings explicitly
Every eval report includes a "Findings withdrawn after reassessment" section listing false positives surfaced during compliance review. This lets the agent's false-positive rate be tracked and informs the next round of calibration. Format:

```
| Call | Original finding | Why withdrawn | Reassessment date |
|---|---|---|---|
```

### R6 — Verify qualifications against the canonical register before applying speaker-scoped flags
Before applying any speaker-scoped hard rule (HF-00, HF-10, HF-11, HF-12, HF-13, HF-15) or making a qualification-based judgement, the agent **must** check the speaker's actual qualifications against `Researcher/research-mcc-fitness-probity.md` (the "Fully Qualified MCC Persons" table).

Rules of interpretation:
- **QFA holder** → all retail product topics in scope.
- **APA Pensions + APA Life + New Entrant PMI** (Matthew Brennan from 2026-05-26) → pensions + life independent; PMI in scope under New Entrant arrangement.
- **APA Pensions + New Entrant PMI** (Callum Pearse, Dan McAvinue) → both product areas discussable; Trevor's call presence not required.
- **APA PMI only** → PMI in scope; pensions / life / tax-relief out of scope.
- **Script pathway** → no regulated product discussion in scope.

The register is the source of truth. If qualifications are unclear or stale, the agent treats the speaker as "unrecognised" — but per R7, "unrecognised" only triggers HF-00 if the speaker is actually advising on a regulated product.

### R7 — Distinguish learner / observer capacity from adviser capacity
HF-00 only fires when an unqualified or unrecognised speaker is **advising / informing the customer about a regulated product**. The following are **NOT** HF-00 triggers:

- **Self-introductions about role** ("I'm responsible for benefits integration") — a job-title statement, not regulated activity.
- **Asking questions to learn about the customer's setup** ("what salary sacrifice platform are you using?") — research, not advice.
- **Product research / competitive intel** ("we were also exploring [provider X]") — Kota learning market behaviour.
- **Observer participation** — sitting in on calls where a qualified colleague leads the regulated content; observer doesn't advise.

The HF-00 test is: did the speaker *advise the customer on a regulated product*, or *give the customer information that would help them choose / configure / arrange a regulated product*? If yes → flag. If they only asked questions, observed, or stated their job title → do not flag.

This is the principal nuance the agent missed on the Gorilla x Kota call (2026-05-11). Slav was on the call to learn about Gorilla's salary-sacrifice platform choice; he was not advising Gorilla.

## Acceptance criteria for the next eval run

The refinements above are working if, on the next weekly eval:
- No findings get withdrawn for being **speaker-presence** issues (Pattern 1).
- No findings get withdrawn for being **correct AE statements** (Pattern 2 + 4).
- No HF-06 / HF-07 findings appear at all (Pattern 3 — already fixed).
- The HF-05 severity ladder is used consistently in the Issues field (Pattern 5).
- The "Findings withdrawn after reassessment" section exists in the eval report, even if empty.

If a finding still gets withdrawn after compliance review, the cause goes into the next calibration note.

## Source files updated

- `Designer/CONTEXT.md` — new R1–R4 rules added
- `Researcher/req-detection-criteria.md` — HF-05 severity ladder added (R3)
- `Researcher/source-of-truth-ae-myfuturefund.md` — already populated (supports R2)
- This file — covers the analysis (R5 is operational: the agent writes this section into each eval going forward)
