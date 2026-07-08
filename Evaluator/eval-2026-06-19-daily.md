---
title: Daily Compliance Eval — 2026-06-19
created: 2026-06-22
type: eval
run_type: live-fireflies
date_range: "2026-06-19"
calls_assessed: 6
calls_flagged: 4
grade_5: 0
grade_4: 0
grade_3: 2
grade_2: 2
grade_1: 2
excluded: 1
revised: 2026-06-22 — Creature Comforts re-graded 3→2 after Compliance confirmed Barbara Murray is on the MCC register (CF4); the HF-10/HF-13 findings rested on a fail-closed unregistered treatment that no longer applies.
---

# Daily Compliance Eval — 2026-06-19

> **Script-based re-grading — 2026-07-06.** **Onboard Retail (Grade 3 → withdrawn):** the income-protection deferred-period (13 vs 26 weeks) and occupational-pension tax-relief statements are within the approved Irish Life scripts; the only residual is the "best thing you could possibly do" recommendation = Grade-2 coaching. Asana task moved to Resolved. See `Researcher/research-prescribed-scripts.md`. (The Entegro HF-09 PPS-over-Gmail finding on this day is unaffected — PII handling is not a script matter.)

## Summary
| Calls assessed | Customer-facing | Calls flagged | Grade 5 | Grade 4 | Grade 3 | Grade 2 | Grade 1 |
|---|---|---|---|---|---|---|---|
| 6 | 6 | 4 | 0 | 0 | 2 | 2 | 2 |

> **Revised 2026-06-22:** Creature Comforts re-graded 3→2 after Compliance confirmed **Barbara Murray is on the MCC register (CF4)**. The original HF-10/HF-13 findings depended on the fail-closed "unregistered → unqualified" rule; with Barbara registered, her pension salary-sacrifice and PMI-positioning statements are in-scope benefits-consulting and no longer hard-rule breaches. Only Callum's soft signals (SF-13/SF-15) remain → Grade 2 (no Asana task). The register snapshot in `research-mcc-fitness-probity.md` has been updated; her exact APA/QFA product scope is still to be recorded by Compliance.

> Six customer-facing calls reviewed (one further meeting — "Planhat x Kota Catchup" — excluded as out-of-scope; see Excluded section). No Severe Fails or Grade-4 referrals today. **Two Grade-3 single-breach calls** (post-revision):
> - **Onboard Retail** — Simon Ward (Customer Success, **script pathway, unqualified**) describing the IP deferred-period choice and the occupational-pension tax-relief/"best thing you could possibly do" framing on a launch call where the qualified colleague (Dan) is not present (HF-10 / HF-01).
> - **Entegro bi-weekly** — Simon Ward (script/unqualified) agreeing to send a pension contribution file **containing matched PPS numbers as a Gmail attachment** (HF-06 unsecured PII handoff).
> - **Creature Comforts** — originally Grade 3 (Barbara Murray treated fail-closed unqualified); **re-graded to Grade 2** after the register correction — see that section and the revision note above.
> The **Vinted** call (Callum, pensions/PMI-qualified) is Grade 2 — one AE-mechanics statement ("40 days") that is not supported by the gov.ie source-of-truth (HF-05 light). The **Antony Harding (Germany)** and **Peacocks** calls are operational/non-IE and graded Pass.

---

## Per-Call Results

### Kota / Onboard Retail — 01KVFE2THW428J1KFVT1YB7BC6 — 2026-06-19 08:00
**Kota speaker(s)**: Simon Ward — Customer Success — **❌ Script pathway (unqualified; supervised by Trevor Gardiner)**
**External / Client**: Onboard Retail / Retail in Motion — Kelly Mahoney (kelly.mahoney@retailinmotion.com), Celine Notin (celine.notin@onboardretail.com, did not speak)
**Department**: CS-CX (Customer Success — benefits launch)
**Duration**: ~18 min
**Grade**: **3 — Fail**
**Fireflies**: https://app.fireflies.ai/view/01KVFE2THW428J1KFVT1YB7BC6

#### Findings
| Criterion | Severity | Speaker (status) | Timestamp | Transcript span | Regulation |
|---|---|---|---|---|---|
| HF-10 | High | Simon Ward (script/unqualified) | ~03:00 | "Either selling the Irish Life packages that approve the pmi, the IP deferred period. Did you decide whether that was going to be the 13 versus the 26 weeks?" — soliciting/confirming the income-protection deferred-period term (product mechanics) | MCC 2017 (info = regulated activity); Kota "Financial Product Information to Customers" |
| HF-01 | High | Simon Ward (script/unqualified) | ~07:30 | "It's like if you're putting stuff into a savings spot, like, this is literally like the best thing you could possibly do." — implicit personal recommendation on the occupational pension | CPC 2025 advice perimeter; IDR Reg. 23(1)(e); FCA COBS 9 / PERG 8 |
| HF-10 | Medium | Simon Ward (script/unqualified) | ~06:30 | "explain the occupational pension and why it's beneficial to money. And so explaining the tax relief piece and giving a couple of scenarios of what that looks like … oh, shit, I'm going to like, save like 700, 800 quid." — describing pension tax-relief mechanics with a worked saving | MCC 2017; HF-05/HF-10 (non-AE pension mechanics — tax relief at source) |
| SF-12 | Low | Simon Ward (script/unqualified) | ~07:30 | "this is literally like the best thing you could possibly do" / "That's unbelievable" — emotive framing of a regulated product (co-occurs with HF-01) | CPC 2025 Part 3; CBI Standards for Business |

#### Notes
This is a benefits-launch logistics call for the Onboard Retail / Retail in Motion go-live on 1 July. **Most of the call is genuine, in-scope launch admin** and is correctly not flagged: comms timing and the lovable→Coda URL conversion, suppressing/triggering platform invites, the 29/30 June webinar scheduling, the Smart Pension UK future-date quirk, the Vitality quote sign-off (seven-vs-actual headcount), the Irish Life scheme-number request, and the levy-on-termination admin question. Simon also correctly states the **product walkthrough at the webinar is Dan's**: *"So Dan will take them through, like, what the different policies offer and like, what cover they can … select."* That hand-off is good practice.

The breaches are where Simon steps onto the product himself:
- **HF-10 (IP deferred period)**: Simon actively asks the client to confirm the **13-vs-26-week income-protection deferred period** — a cover-mechanics term of a regulated IP product — rather than routing it to Dan/Paul. The client answers "26", so the term is being settled in a conversation led by an unqualified speaker.
- **HF-01 / SF-12 (pension)**: Simon goes beyond admin into advocacy — *"this is literally like the best thing you could possibly do"* — an implicit recommendation, and frames the tax-relief saving emotively ("save like 700, 800 quid … That's unbelievable"). This is the occupational-pension equivalent of the audit's recurring "talk up the benefit" pattern.
- **HF-10 (tax relief)**: describing the occupational-pension tax-relief mechanic and a worked saving scenario is non-AE pension mechanics by an unqualified speaker.

**AE / My Future Fund check (HF-05)**: The only AE reference is the **client's** ("I promise you we're giving more than auto enrollment"). Simon makes **no** statement of AE public-law rules (no percentage, eligibility, phasing, or opt-out claim). **No HF-05.** The "4% no matter what … and we don't have a match" exchange is occupational-pension **configuration/admin** (how to enter a non-contributory employer rate in the platform), not a public-law AE claim.

**HF-03 check**: "We offer lay and BHI now as well" and the Irish Life partnership colour ("they were the first ones to back us") are factual statements about Kota's provider panel — not a misrepresentation of firm capability/scope. **No HF-03.**

**Grade rationale**: Grade 3 (single clear perimeter breach class) — a script-pathway speaker conducting regulated activity (IP deferred-period confirmation + pension recommendation/mechanics) on a launch call without the qualified colleague present. It is **below** the Paligo Grade-4 of 2026-06-12 because the volume is far lower (no sustained premium/excess/plan-comparison run), it is largely launch logistics, and Simon explicitly reserves the product walkthrough for Dan at the webinar.

**Escalation**: No ES trigger fired. Recommend Benefits (Dan / Paul) own the IP deferred-period sign-off and the webinar pension/tax-relief content, and that Simon's webinar part stay to the ~2-minute intro he describes.

---

### Vinted x Kota — 01KVFKQT85ZGAN2BT8HMT74RR2 — 2026-06-19 09:35
**Kota speaker(s)**: Callum Pearse — Account Executive — **✅ Qualified APA Pensions (independent); PMI under New Entrant arrangements (may discuss PMI). NOT Life Assurance / IP.**
**External / Client**: Vinted — Alice Hu, Federica Misantone (Vinted; @vinted not captured in participant string, Fireflies recorded callum@kota.io only)
**Department**: GTM / Account Executive (Irish payroll + pension setup; UK/Luxembourg benefits review)
**Duration**: ~28 min
**Grade**: **2 — Pass with comments**
**Fireflies**: https://app.fireflies.ai/view/01KVFKQT85ZGAN2BT8HMT74RR2

#### Findings
| Criterion | Severity | Speaker (status) | Timestamp | Transcript span | Regulation |
|---|---|---|---|---|---|
| HF-05 (light) | Medium | Callum Pearse (qualified Pensions) | ~04:00 | "the way the government has set it up is that they will automatically enroll the employee into the my future fund … some companies have 40 days where they haven't had it and then they're actually fine. But the likelihood is employee would be also enrolled into the government scheme and then … as long as a pension is on their payroll the month after, they'll then be reimbursed that contribution." | MCC 2017; HF-05 AE accuracy vs `source-of-truth-ae-myfuturefund.md` |

#### Notes
Callum is **pensions-qualified**, so Irish occupational-pension setup mechanics are squarely in scope, and PMI is within his New-Entrant arrangement. **No Life/IP content arises** (the UK insurers named — Canada Life, AXA, Royal London — are surfaced **by the client**, and Callum's responses stay at broker/admin level: "we can broker with everything, all of those providers"). The spend-card walkthrough (allowances, MCC merchant-category-code restriction, receipts/tax-deduction reporting), salary-sacrifice/cycle-to-work, and the UK "is it tax free" answers are platform mechanics and UK general-tax facts, not Irish retail-product advice.

**AE check (HF-05) — the one flag.** Callum's description of the auto-enrolment interaction is **partly unsupported by the gov.ie source-of-truth**:
- The **"40 days where they haven't had it and then they're actually fine"** grace-period figure does **not** appear anywhere in `source-of-truth-ae-myfuturefund.md`. The source says enrolment "may take up to 13 weeks" in defined circumstances and that overlapping contributions are refunded — there is no blanket "40 days and you're fine" exemption.
- The **auto-reimbursement principle** he describes ("as long as a pension is on their payroll the month after, they'll then be reimbursed") is **directionally consistent** with the source's overlapping-contribution refund and no-waiting-period text ("You will get a refund of any overlapping contributions"), so that limb is not itself a breach.
Net: the "40 days" specific is a wrong/unsupported number on a public-law mechanic → **HF-05 light** (right general principle of refund-on-late-pension, but a fabricated grace-period figure the customer could act on). Logged for coaching; it does not on its own meet the Grade-3 perimeter threshold.

**Grade rationale**: Grade 2 — one HF-05-light AE inaccuracy by an otherwise in-scope, qualified speaker; documented in this report, no Asana task per the rubric (Grade 2 = coaching). Recommend Callum default to "I'll send you the gov.ie page" on AE timing specifics rather than quoting a day-count.

**Escalation**: No.

---

### Kota <> Lorraine Wood — 01KVAJNBNDASEX5GKK8NGRKBZN — 2026-06-19 10:00
**Kota speaker(s)**: Callum Pearse — Account Executive — **✅ Qualified APA Pensions; PMI under New Entrant arrangements.** | Barbara Murray (barbara@kota.io) — **✅ On the MCC register (CF4) — confirmed by Compliance 2026-06-22; benefits-consulting content treated as in-scope.**
**External / Client**: Creature Comforts (veterinary group) — Lorraine Wood (lorraine.wood@creaturecomforts.co.uk), HR Director
**Department**: GTM / Benefits (UK benefits discovery / EVP)
**Duration**: ~30 min
**Grade**: **2 — Pass with comments** *(revised 2026-06-22 from 3 — Fail; see note)*
**Fireflies**: https://app.fireflies.ai/view/01KVAJNBNDASEX5GKK8NGRKBZN

#### Findings
> **Revised 2026-06-22.** The two hard-rule findings below (HF-10, HF-13) were raised **only** because Barbara Murray was absent from the register snapshot and treated fail-closed as unqualified. Compliance has since confirmed she is on the MCC register (CF4), so her pension salary-sacrifice explanation and PMI-positioning are **in-scope benefits-consulting** — the HF-10/HF-13 hard rules are **withdrawn**. They are retained here (struck through) for the audit trail. Only the two soft signals remain, which place the call at Grade 2.

| Criterion | Severity | Speaker (status) | Timestamp | Transcript span | Regulation |
|---|---|---|---|---|---|
| ~~HF-10~~ *(withdrawn — speaker in scope)* | — | Barbara Murray (✅ CF4, registered) | ~14:00 | "do you salary, salary sacrifice your pension at the moment? … because that's, that's a real good way to unlock some budget from your national insurance savings." | In-scope pensions benefits-consulting; no breach |
| ~~HF-13~~ *(withdrawn — speaker in scope)* | — | Barbara Murray (✅ CF4, registered) | ~05:30 | "our health insurance is with axa." / "Okay, yeah, that. Yeah, Premium brand for in terms of cost." | In-scope PMI benefits-consulting; no breach |
| SF-13 | Low | Callum Pearse (qualified Pensions/PMI) | ~24:00 | "since they were bought by Eden Bread, yeah, it's massively slowed down" / "they don't manage your private medical … there's big, big chunks of benefits that are missing from them" — disparaging Reward Gateway (competitor platform) | CPC 2025 Part 3; FCA COBS 4.2.4R; SF-13 |
| SF-15 | Low | Callum Pearse (qualified) | ~16:00 | "I talk to people every day about benefits. So I see … what lots of people are doing." — social-proof anchoring (co-occurs with the tiering pitch) | CPC 2025; SF-15 |

#### Notes
A UK benefits-discovery call. Callum (pensions-qualified, PMI New-Entrant) carries most of the regulated content within scope: health-cash-plan tiering, EAP bolt-ons, the broker/platform model, and the £9→£5 PEPM pricing for the **Kota platform fee** (explicitly out of HF-13 scope). The platform/admin/HRIS/payroll-2027/P11D material is operational and not flagged.

The original hard-rule flags clustered on **Barbara Murray**, who speaks substantively on pension salary-sacrifice and PMI positioning. At the time of the first pass she was **absent from the register snapshot** in `research-mcc-fitness-probity.md`, so the fail-closed rule treated her as unqualified and raised HF-10/HF-13.

**Revised 2026-06-22:** Compliance (Sola Olaniyan) confirmed **Barbara Murray is on the MCC register as a CF4**. With Barbara registered:
- The **pension salary-sacrifice mechanic** ("a real good way to unlock some budget from your national insurance savings") is **in-scope benefits-consulting** — HF-10 **withdrawn**.
- The **AXA "Premium brand … in terms of cost"** positioning is **in-scope PMI consulting** — HF-13 **withdrawn**.
The register file has been updated to include her (CF4); her exact APA/QFA product-scope detail is still to be recorded by Compliance.

Two soft signals remain (Callum), insufficient for a hard finding but co-occurring → they set the residual grade:
- **SF-13 (Callum)**: sustained disparagement of **Reward Gateway** ("massively slowed down … big chunks of benefits missing … since … Eden Bread"). Reward Gateway is a benefits-platform competitor rather than a regulated insurance product/provider, so this is SF-13 tone, not HF-14 — but it is the assertion-without-evidence pattern reviewers flag.
- **SF-15 (Callum)**: light social-proof anchoring.

**Grade rationale (revised)**: **Grade 2 — Pass with comments.** With Barbara's register status confirmed, no hard rule stands; the call carries two co-occurring soft signals from Callum (SF-13 + SF-15), which is Grade 2 territory — documented for coaching, **no Asana task** per the queue rules. *(Originally graded 3 — Fail on the fail-closed unqualified treatment of Barbara, now withdrawn.)*

**Escalation**: No. The earlier "HF-00 fires structurally" reasoning is **withdrawn** — Barbara is registered, not an unregistered speaker. Coaching note for Callum on the competitor disparagement (SF-13) stands.

---

### Kota <> Antony Harding — 01KVD7JG0XWXG69ZQJAKGER8AV — 2026-06-19 10:30
**Kota speaker(s)**: Callum Pearse — Account Executive — **✅ Qualified APA Pensions; PMI New Entrant.**
**External / Prospect**: Pace People — Antony Harding (antony@pace-people.com), clean-energy headhunter
**Department**: GTM (UK benefits review + Germany expansion enquiry)
**Jurisdiction note**: The German-entity request is **non-IE/UK** — MCC is an Irish regime and does not apply extraterritorially; Callum correctly declines to advise on Germany and offers only to ask his team for provider names.
**Duration**: ~15 min
**Grade**: **1 — Pass**
**Fireflies**: https://app.fireflies.ai/view/01KVD7JG0XWXG69ZQJAKGER8AV

#### Findings
No findings flagged. Documented negatives below.

#### Notes
A short discovery/demo. The prospect asks Kota to build a benefits package for a new **German** entity (medical/pension). Callum stays in scope:
- He **does not advise on Germany**, repeatedly deferring ("I can't promise we'd be able to … we need to set up our license in Germany … at least six months"). Good perimeter discipline on a non-IE jurisdiction.
- UK content is platform/admin: HRIS sync, payroll-reconciliation reports, the 2027 P11D/BIK change, spend cards. The single product-mechanics-adjacent line — *"life insurance isn't a taxable benefit but health insurance is"* — is a UK general-tax fact stated by a pensions/PMI-qualified speaker in the course of describing the platform's payroll reporting, not retail-product advice; not flagged.
- **Smart Pension** named as the only current pension integration with a correct regulatory caveat ("it's a very regulated market and … we need to update our license"). Factual, not a capability misrepresentation — **no HF-03**.

Incidental: the prospect mentions he was referred by "ChatGPT or Claude" — no compliance relevance.

**Grade rationale**: Grade 1 — operational/discovery call, qualified speaker, correct non-IE deferral. No Asana task.

**Escalation**: No.

---

### Kota <> Rachel Seller — 01KTXX7HDE22JRBRQ69Q31SMSH — 2026-06-19 13:00
**Kota speaker(s)**: Callum Pearse — Account Executive — **✅ Qualified APA Pensions; PMI New Entrant.** | Barbara Murray (barbara@kota.io) — **❌ not on MCC register → fail-closed unqualified.**
**External / Prospect**: Peacocks (NHS-adjacent, 123-year-old company) — Rachel Seller (rachel.seller@peacocks.com), + Chris (Head of HR, did not speak materially)
**Department**: GTM (platform/payroll-automation discovery — turned out to be a scope mismatch)
**Duration**: ~23 min
**Grade**: **1 — Pass**
**Fireflies**: https://app.fireflies.ai/view/01KTXX7HDE22JRBRQ69Q31SMSH

#### Findings
No findings flagged. Documented negatives below.

#### Notes
This call is **entirely operational** and ends in the prospect realising Kota is not what she expected (she was looking for a payroll/sickness-policy automation tool, not a benefits broker/platform). The whole conversation is about manual payroll exceptions, sickness-scheme calculations, new-starter/leaver pro-rating, HRIS/payroll-export flow, P11D reconciliation, and the 2027 BIK change. No regulated retail-product advice, information, comparison, pricing, or cover mechanics are discussed by either Kota speaker.

- Barbara's contribution is limited to describing the broker/renewal-streamlining role and asking which payroll/HR system they use — operational, no product mechanics (contrast with the Creature Comforts call where she crossed into pension salary-sacrifice mechanics).
- Callum's P11D/2027 explanation is a factual public-tax-change statement framed around the platform's reconciliation reporting, not advice to a specific person.

**Grade rationale**: Grade 1 — operational discovery with a scope mismatch; no findings. Defines the negative class. No Asana task.

**Escalation**: No.

---

### Kota / Entegro: bi-weekly — 01KV8GATQXPZ0JAQCCY76Q1RCW — 2026-06-19 13:00
**Kota speaker(s)**: Simon Ward — Customer Success — **❌ Script pathway (unqualified)** | Dan McAvinue — Benefits Co-Ordinator — **✅ Qualified APA Pensions & Life (independent); PMI New Entrant.**
**External / Client**: Entegro/Integro — Brena Hamilton (bhamilton@entegro.com), payroll/accountancy; A. Caulfield (acaulfield@entegro.com, did not speak)
**Department**: CS-CX / Benefits (pension administration bi-weekly)
**Duration**: ~29 min
**Grade**: **3 — Fail**
**Fireflies**: https://app.fireflies.ai/view/01KV8GATQXPZ0JAQCCY76Q1RCW

#### Findings
| Criterion | Severity | Speaker (status) | Timestamp | Transcript span | Regulation |
|---|---|---|---|---|---|
| HF-06 | High | Simon Ward (script/unqualified) | ~21:30 | "I'll share this with you in Gmail but I know you don't ever it seems like receive these but it's just so that you have it. … I'll pop it to you in a Gmail attachment." — agreeing to send the pension contribution **change report** (employee-level data, PPS-matched) as an unsecured Gmail attachment | GDPR Art. 5(1)(f) / Art. 32; DPC guidance; Kota PII-handling policy |

#### Notes
A pension-administration bi-weekly. **Dan McAvinue carries all the regulated pension content and is qualified for it** — so the substantive pension-rules discussion is correctly **not** flagged:
- Dan on the **occupational-scheme rule changes** ("the government changed a load of the rules around occupational pension schemes on Christmas Eve … the two year vesting period on private schemes is going to get shuttered at some point this year") — this is Dan (qualified Pensions) relaying Irish Life's view of likely future legislation, explicitly hedged ("nothing's happened yet", "that's not happened yet"). Within scope; the hedging is appropriate, not SF-14 gaming.
- Dan on the **outgoing-worker form / employer-refund** mechanics (EU-member-state checkboxes, refund trigger) — pensions mechanics by a qualified speaker, in scope.
- The **Irish Life invoice split** (employer vs employee contribution for corporation-tax relief), the **TRS** reference, and the salary-forecast-view explanation (Irish Life updates annually on 1 Jan) are pension-administration/billing, handled by Dan (qualified) — not flagged.

**AE / source-of-truth check**: No AE public-law percentages/eligibility/phasing/opt-out claims are made. Dan's "as close as possible to the minimum standards … with auto enrollment" is a forward-looking comment on occupational-scheme minimum standards, not a statement of the AE contribution split. **No HF-05.**

**The flag is HF-06 (Simon).** The artefact Simon proposes to email is the **pension contribution change report** — explicitly employee-level and **PPS-matched** ("I do all of the … the PPS is matched … we need to work through what that errors look like in the file"). Agreeing to send a file containing employee PPS numbers / contribution data as a **Gmail attachment**, rather than via the in-product secure flow, is the exact HF-06 pattern (Q4-25-PII-01). It is squarely Simon's action (script-pathway/unqualified), and it lands as a single clear PII-handling breach.

Operational items correctly not flagged: change-report headcount sense-check (May 141 → June 145), leaver/joiner timing shift from 10th to month-end, payroll-driven-billing roadmap, Sage payroll integration, the spend-card "test euros"/gift-voucher chat, and the workflow/rule-set automation preview.

**Grade rationale**: Grade 3 — a single clear breach of **PII handling** (HF-06) by an unqualified speaker. It is not Grade 4/5 (no advice-perimeter or capability deception), but PII handoff is a Red-class breach in the rubric and warrants a task. Note this is a **transcript-stated action**; per the v1 perimeter the agent flags the stated intent — Compliance to confirm whether the file actually went by email and, if so, that it be retracted/re-sent via the secure flow.

**Escalation**: No ES trigger, but recommend Compliance verify the Gmail send did not occur (or remediate if it did).

---

## Cross-Call Patterns

- **Script-pathway speaker (Simon Ward) on two of today's flagged calls.** Onboard Retail (HF-10/HF-01 on IP/pension) and Entegro (HF-06 PII). Simon repeatedly operates on regulated/sensitive content where a qualified colleague exists (Dan/Paul). On Entegro, Dan **was present and carried the pension content correctly** — the residual breach was purely Simon's PII-handoff intent; on Onboard Retail, Dan/Paul were **not** on the call and Simon stepped onto IP/pension himself. Reinforces the 2026-06-12 recommendation: route regulated content to the qualified attendee, and never run product confirmation solo.
- **Register gap — Barbara Murray (barbara@kota.io) — RESOLVED 2026-06-22.** She spoke substantively on two calls and was absent from the register snapshot; fail-closed drove the initial Creature Comforts Grade-3. Compliance (Sola) confirmed she **is** on the MCC register as a **CF4**; the register file has been updated and Creature Comforts re-graded 3→2. Outstanding: record her exact APA/QFA product scope in the register so the agent can scope-check future calls (e.g. a future PMI/pension/life boundary). This confirms the value of an explicit "register-miss → confirm status" flag rather than silently grading unqualified (see Open Questions #1).
- **AE "specific number" risk.** Callum's "40 days" (Vinted) repeats the long-running pattern of reps attaching a precise figure to an AE mechanic that the gov.ie source does not state. Same coaching point as the prior Karl O'Brien / Simon Ward AE findings.
- **Fireflies mis-transcriptions preserved verbatim.** "COTA/Coda/Cosa/kosher" for Kota, "Boop/PUPA" not seen today; "hysterical life policy" = (Irish Life) "group life policy"; "his/HIS" = HRIS; "Integra/Integro" = Entegro; "John" used interchangeably for Dan in one Entegro turn. Quotes above are left as transcribed.

## Asana

- **Onboard Retail (01KVFE2THW428J1KFVT1YB7BC6)** — Grade 3 → create Asana task, route to **CS-CX / Benefits**, @-mention the relevant executive. HF-10 (IP deferred period), HF-01 (pension recommendation).
- **Creature Comforts / Lorraine Wood (01KVAJNBNDASEX5GKK8NGRKBZN)** — **revised 2026-06-22 to Grade 2 → no Asana task.** Original HF-10/HF-13 withdrawn after Compliance confirmed Barbara Murray is on the MCC register (CF4); residual SF-13/SF-15 (Callum) are coaching-only. Register snapshot updated.
- **Entegro bi-weekly (01KV8GATQXPZ0JAQCCY76Q1RCW)** — Grade 3 → create Asana task, route to **CS-CX**; HF-06 PII handoff. Verify/remediate the Gmail send.
- **Vinted (01KVFKQT85ZGAN2BT8HMT74RR2)** — Grade 2 → **no Asana task** (coaching note only): HF-05-light AE "40 days".
- **Antony Harding (01KVD7JG0XWXG69ZQJAKGER8AV)** — Grade 1 → no task.
- **Peacocks / Rachel Seller (01KTXX7HDE22JRBRQ69Q31SMSH)** — Grade 1 → no task.

## Excluded (not assessed)

- **Planhat x Kota Catchup — 01KVAV9QY2PPF1BJGTVVA9B724 — 10:00.** Simon Ward evaluating **Planhat (a Customer-Success software vendor) for Kota's own internal use**. No retail consumer is present and no Kota financial product is discussed — this is Kota as a buyer of SaaS, not a customer-facing benefits/insurance call. **Out of MCC scope; not assessed.**

## Open Questions for the Designer

1. **Register completeness (Barbara Murray).** barbara@kota.io speaks as a benefits consultant on two calls but is absent from the MCC register snapshot. Fail-closed forced an unqualified treatment and a Grade-3. The agent needs a path to distinguish "genuinely unqualified" from "register not yet updated" — recommend surfacing register-miss as an explicit "register gap — confirm status" flag rather than silently grading as unqualified, so Compliance can reconcile.
2. **Transcript-stated PII actions (HF-06).** Entegro's HF-06 is a *stated intent* to email a PPS-matched file. The v1 perimeter is "transcript only" and excludes out-of-call execution — but the **agreement on the call** is itself the trigger here. Confirm the agent should flag the stated intent (as done) and hand verification of the actual send to Compliance.
3. **AE day-count specifics.** "40 days where they're fine" (Vinted) and similar precise AE-timing figures keep recurring. Should the agent treat *any* unsourced AE numeric (day-count, percentage, threshold) as at least HF-05-light by default, since the gov.ie source only states "up to 13 weeks"?
4. **Silent qualified attendee vs. present-and-active (carried over from 2026-06-12).** Entegro is the positive case: Dan was present **and spoke to the regulated content**, so Simon's non-pension lines were not HF-00. Confirm the rule: a qualified colleague mitigates only the content they actually cover, and an unqualified speaker's own out-of-scope lines (e.g. Simon's PII handoff) remain flaggable regardless.
