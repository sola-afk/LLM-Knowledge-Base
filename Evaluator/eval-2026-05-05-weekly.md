---
title: Weekly Compliance Eval — 2026-05-05 to 2026-05-08
created: 2026-05-08
type: eval
run_type: live-fireflies
date_range: "2026-05-05 to 2026-05-08"
calls_reviewed: 16
calls_flagged: 10
grade_5: 1
grade_4: 3
grade_3: 2
grade_2: 4
grade_1: 6
note: "Recording consent check removed — collected pre-call. 5 calls regraded from Grade 2 to Grade 1. Timestamps in this run are approximate; future runs will report exact MM:SS from Fireflies sentence data."
---

# Weekly Compliance Eval — 2026-05-05 to 2026-05-08

## Summary
| Calls assessed | Customer-facing | Calls flagged | Grade 5 | Grade 4 | Grade 3 | Grade 2 | Grade 1 |
|---|---|---|---|---|---|---|---|
| 16 (19 not pulled) | 15 | 10 | **1 — URGENT** | 3 | 2 | 4 | 6 |

> 16 calls assessed: 6 direct transcript review + 10 via evaluation agent. 19 lower-risk calls not pulled — see "Calls Not Pulled" table. **CHM Pension Update is Grade 5 Severe Fail — requires immediate escalation to Simon Ellis.**
>
> **Note — recording consent removed**: Pre-call consent is collected separately; verbal disclosure at call start is no longer a detection criterion. 5 calls regraded from Grade 2 to Grade 1 (DailyPay, Frontiers, Voltalis, Gabriela, Allianz White Label).
>
> **Note — timestamps**: Timestamps for the 6 priority calls (CHM, Carwow, Jennifer Kenyon, Volta, Enrico Grande, Riot Games) are anchored to Fireflies AI-summary topic ranges (~±30s accuracy). The Fireflies `fireflies_get_summary` returns timestamped action items and topic-section ranges that map cleanly to specific moments in the call. Per-sentence `start_time` is not currently exposed by the MCP transcript tools — Designer/CONTEXT.md requires future runs to use the summary anchors and/or push for exact `start_time` exposure.

---

## Per-Call Results

### Volta <> Kota — 01KR1C17K3073PNG1AMMYDH31V — 2026-05-08 09:30
**Kota speaker(s)**: Karl O'Brien — Script pathway (❌ unqualified)
**External**: Satpal (Volta AI)
**Department**: GTM
**Duration**: 32 min
**Grade**: **4 — Fail w/ referral**
**Fireflies**: https://app.fireflies.ai/view/01KR1C17K3073PNG1AMMYDH31V

#### Findings
| Criterion | Severity | Timestamp | Transcript span | Regulation |
|---|---|---|---|---|
| HF-00 | High | ~00:06 onwards | Karl runs full regulated advisory call solo — PMI underwriting, pension providers, group risk — no qualified supervisor present | CBI MCC 2017; FCA COBS |
| HF-10 | High | ~02:40 | "It is moratorium" — Karl confirms and explains underwriting type (moratorium vs MHD) to prospect | CBI MCC 2017 — unqualified speaker describing type of cover |
| HF-11 | High | ~04:08 | "We can ask Vitality, Accent, Aviva as well if you want to look at them" — Karl initiating plan comparison across PMI providers | CBI MCC 2017 — unqualified speaker comparing plans |
| HF-02 | High | ~30:06 | "Unum usually come back a lot more competitive" re group risk; "Aviva, who have been performing really well over the past year or two" re pensions | CPC 2025 Part 3 — clear, fair, not misleading |
| HF-11 | High | ~15:50 | Karl compares pension providers by quality: "it's not as market leading as you would with a Cushon or a Royal London Scottish Widows... Even Aviva, who have been performing really well" | CBI MCC 2017 — unqualified speaker comparing plans |
| HF-01 | High | ~24:01 | "I would say it is better off to go with the platform process" — explicit recommendation on service pathway | CBI MCC 2017; CPC 2025 |

#### Notes
Karl explicitly states at 00:30: *"from a regulatory perspective, the salesperson can't do much purely because we're regulated by the FCA"* — demonstrating awareness of the constraint — then spends 32 minutes conducting full regulated activity including PMI underwriting explanations, pension provider quality comparisons, and group risk product recommendations. No qualified supervisor present throughout.

**Escalation**: No — Grade 4 does not auto-escalate. No ES-01/02/03. No unregistered speaker.

---

### Kota <> Enrico Grande — 01KR0ZTP2QQK36GEHCZZFXBXYG — 2026-05-07 10:30
**Kota speaker(s)**: Karl O'Brien — Script pathway (❌ unqualified)
**External**: Enrico Grande (PortX)
**Department**: GTM
**Duration**: 36 min
**Grade**: **4 — Fail w/ referral**
**Fireflies**: https://app.fireflies.ai/view/01KR0ZTP2QQK36GEHCZZFXBXYG

#### Findings
| Criterion | Severity | Timestamp | Transcript span | Regulation |
|---|---|---|---|---|
| HF-00 | High | ~01:01 onwards | Karl runs full regulated advisory call solo — PMI market overview, pension contribution rules, group risk product descriptions, tax implications | CBI MCC 2017; FCA COBS |
| HF-11 | High | ~14:23 | "BUPA and Vitality are probably the optimal ones within the market... BUPA has more flexibility in the pricing packages... Vitality are less likely to come back with the custom price and medical history disregarded for smaller businesses" | CBI MCC 2017 — unqualified speaker comparing plans |
| HF-10 | High | ~14:14 | Karl explains MHD vs moratorium underwriting to prospect for a virgin PMI scheme (Note: agent verification could not pin down explicit moratorium contrast — see Asana task) | CBI MCC 2017 — unqualified speaker describing type of cover |
| HF-05 | High | ~20:32 | "you'll also get tax implications for that. With benefit in kind... it will benefit you through benefit in kind... you can get benefit in kind and tax relief at source on that too" — tax conclusions applied to Enrico's specific scenario | CPC 2025; personal tax conclusions outside scope |
| HF-00 | High | ~18:15 | Karl explains occupational pension contribution mechanics: "the employer is minimum three and the employee has to give 5%... has to add up to 8%" — applied to Enrico's specific hire | CBI MCC 2017; FCA COBS |

#### Notes
Karl's self-correction at end of call (*"I can't go through it, for regulatory reasons"* when asked for a specific plan cost estimate) demonstrates awareness of the boundary but this occurs after ~30 minutes of sustained regulated activity. Self-correction does not undo the prior breaches.

Cross-call pattern: same breach profile as Volta x Kota (01KR1C17K3073PNG1AMMYDH31V) same day. Karl is conducting this pattern systematically across solo sales calls this week.

**Escalation**: No — Grade 4. No ES/HF-03/unregistered trigger.

---

### PMI Via Employment Hero - Beyondly — 01KR0SKMWRBK3P940K1CYKX49C — 2026-05-08 09:00
**Kota speaker(s)**: Paul O'Hanlon — Qualified APA PMI (✅); Kate Fullen — Unregistered (❌) present but silent
**External**: Aoife Hargreaves, Lucy Boyes (Beyondly); Deepak Baliga (Yonder/EmploymentHero)
**Department**: Benefits
**Duration**: 27 min
**Grade**: **2 — Pass with comments**
**Fireflies**: https://app.fireflies.ai/view/01KR0SKMWRBK3P940K1CYKX49C

#### Findings
No hard-rule or soft-signal findings.

#### Notes
Kate Fullen (`kate@kota.io`) is listed as a meeting participant but does not speak. All substantive PMI discussion is handled by Paul O'Hanlon (APA PMI qualified) — within scope. Kate Fullen's attendance on regulated PMI calls as an unregistered person is a compliance risk even if silent. Recommend Compliance confirm Kate has no customer interaction on these calls.

**Escalation**: No.

---

### DailyPay <> Kota - Platform Overview — 01KQQ6CST6K3AYH7H8TXGVZ7JW — 2026-05-05 14:00
**Kota speaker(s)**: Karl O'Brien — Script pathway (❌)
**External**: Clyntin Aoki-Saffer, Molly Deng (DailyPay)
**Department**: GTM
**Duration**: 35 min
**Grade**: **1 — Pass**
**Fireflies**: https://app.fireflies.ai/view/01KQQ6CST6K3AYH7H8TXGVZ7JW

#### Findings
No findings.

#### Notes
This call is a platform demonstration — Karl shows the Kota admin dashboard, HRIS integration (ADP Workforce), payroll reports, spend module, and employee app. Content is operational/technology focused, not regulated product advice. Karl does not compare plans, discuss cover details, or give pension advice. Falls within the permitted MCC carve-out of "selling the platform & its benefits — not the insurance or pension product itself."

Contrast with Volta (01KR1C17K3073PNG1AMMYDH31V) and Enrico Grande (01KR0ZTP2QQK36GEHCZZFXBXYG) where Karl's calls are substantively advisory. The nature of the call (demo vs advisory) is the differentiating factor.

**Escalation**: No.

---

### Frontiers <> Kota — 01KQPHSNTJ6HXH766WK791BKT1 — 2026-05-05 08:30
**Kota speaker(s)**: Karl O'Brien — Script pathway (❌); Matthew Brennan — New Entrant (⚠️)
**External**: Stéphane Bavaud, Maria (Frontiers)
**Department**: GTM
**Duration**: 29 min
**Grade**: **1 — Pass**
**Fireflies**: https://app.fireflies.ai/view/01KQPHSNTJ6HXH766WK791BKT1

#### Findings
No findings.

#### Notes
This is a commercial strategy / account management call — Karl and Matthew discuss transitioning Frontiers from Benefex to Kota, proposing Ireland as a proof-of-concept, and planning next steps. No specific plan comparisons, underwriting discussions, or product recommendations. Matthew Brennan (New Entrant) joins as "General Manager" and discusses platform capabilities and process — not regulated product advice.

Karl explicitly defers regulated discussion to Dan McAvinue for the next session: *"Dan will probably join us on the next session"* — correct behaviour for a Script pathway rep.

**Escalation**: No.

---

### Kota & Life Scientific UK Pension Update Call — 01KQWB2KZRQ767HN3MA969G9DV — 2026-05-07 10:00
**Kota speaker(s)**: Daniel McAvinue — Qualified APA Pensions/Life (✅); Simon Ward — Script pathway CS (❌) — facilitative role only
**External**: Michelle Fogarty, Alison Bosher, Eleanor Long, Andrea Milne, Sam Gorny, Simon Ford, Anne-Marie Lowry, Katie, others (Life Scientific UK employees)
**Department**: CS
**Duration**: 47 min
**Grade**: **2 — Pass with comments**
**Fireflies**: https://app.fireflies.ai/view/01KQWB2KZRQ767HN3MA969G9DV

#### Findings
| Criterion | Severity | Timestamp | Transcript span | Regulation |
|---|---|---|---|---|
| ES-02 | Medium | ~35:00 | Sam Gorny: "are we as Life Scientific not now quite vulnerable to HMRC and the pension ombudsman?" — potential regulatory liability flagged by customer | Pension ombudsman / HMRC auto-enrolment compliance |

#### Notes
Simon Ward's role is entirely operational: he introduces Dan, manages screen-sharing logistics, and provides brief acknowledgments ("Yeah", "Still in the postponement period"). All substantive pension content is handled by Dan McAvinue (APA Pensions, qualified) — within scope.

The ES-02 signal arises from Sam Gorny (Life Scientific employee) raising HMRC/Pension Ombudsman exposure due to delayed pension enrollment. Dan appropriately explains the detriment calculation process and commits to clarifying with Smart Pension. Life Scientific's HR lead (Michelle Fogarty) also acknowledges competency questions about the previous payroll provider (Sintra). Well-handled but should be documented for Compliance awareness.

**Escalation**: No — ES-02 is customer-raised, Dan handles appropriately. No Kota staff made the liability statement.

---

## Agent-Assessed Calls

The following 10 calls were assessed via evaluation agent using direct Fireflies transcript analysis.

---

### Kota x Jennifer Kenyon — 01KQVGS5SSY6ZHXC8NSCW996E0 — 2026-05-05
**Kota speaker(s)**: Karl O'Brien — Script pathway (❌ unqualified)
**External**: Jennifer Kenyon (Vocal AI / getvocal.ai)
**Department**: GTM
**Duration**: 18 min
**Grade**: **4 — Fail w/ referral**
**Fireflies**: https://app.fireflies.ai/view/01KQVGS5SSY6ZHXC8NSCW996E0

#### Findings
| Criterion | Severity | Timestamp | Transcript span | Regulation |
|---|---|---|---|---|
| HF-00 | High | ~05:34 | "So I would split it down into kind of two sides of benefits. So you have your core benefits and you're flexible. So the core would be like. I kind of look at it as like the big four. So you'd look at your pmi, your pension, your life assurance and your income protection" — Karl describes regulated products solo | CBI MCC 2017; FCA COBS |
| HF-01 | High | ~10:19 | "I would almost tier them into like that pet, like healthcare and pension. Like they're obviously kind of the bog standard that people understand. And then like the life assurance and income protection, like feeding them in thereafter is quite nice" | CBI MCC 2017; CPC 2025 |
| HF-01 | High | ~11:26 | "I would probably recommend just wait until you get them on because there's a level of underwriting, they expect minimum for the group." | CBI MCC 2017; CPC 2025 |
| HF-11 | High | ~08:30 | "Allianz is really good, but it's really expensive like because it's an international… if you're going to be in the UK for a while, like Bupa and Vitality are great options." | CBI MCC 2017 — unqualified speaker comparing plans |
| HF-02 | High | ~08:30 | "Allianz is really good, but it's really expensive" — comparative value judgement | CPC 2025 Part 3 |
| SF-15 | Low | ~10:19 | "when you see it like because 18% of usually is what it comes down to about is total payroll is benefits" — social proof anchoring without evidence | MCC SF-15 |

#### Notes
Karl conducts the entire 18-minute sales call solo, describing and comparing regulated products (PMI, pension, life assurance, income protection) and making explicit recommendations. Third solo advisory call this week alongside Volta and Enrico Grande — systematic pattern.

**Escalation**: No per spec (script pathway, not unregistered; no ES/HF-03 triggers). Three Karl Grade 4 calls this week require supervisor-level intervention by Trevor Gardiner.

---

### Anjana x Kota — 01KR0YY81A2NYNXG5VCFGZFW5Q — 2026-05-07
**Kota speaker(s)**: Henry Godson — Script pathway BDR (❌ absent, no spoken lines); Callum Pearse — Qualified Pensions (✅), New Entrant PMI (⚠️)
**External**: Anjana Shah (City of Westminster Academy)
**Department**: GTM
**Duration**: 19 min
**Grade**: **2 — Pass with comments**
**Fireflies**: https://app.fireflies.ai/view/01KR0YY81A2NYNXG5VCFGZFW5Q

#### Findings
| Criterion | Severity | Timestamp | Transcript span | Regulation |
|---|---|---|---|---|
| Observation | Informational | Throughout | Callum (PMI New Entrant) leads substantive PMI renewal/broker engagement including provider comparisons (AXA, BUPA, Vitality, Aviva); no supervisor on call | MCC New Entrant supervision |

#### Notes
Henry organised the call but has zero spoken lines — "Henry's had to quickly pop out" per Callum's opening. Callum stays within scope: no recommendations, transparent about broker-of-record process. The PMI New Entrant point is a supervision question (is Trevor Gardiner aware and supervising?).

**Escalation**: No.

---

### Voltalis x Kota Intro — 01KQSC4X435R27HC3F2M6727AY — 2026-05-06
**Kota speaker(s)**: Henry Godson — Script pathway BDR (❌ absent, no spoken lines); Paul O'Hanlon — Qualified APA PMI (✅)
**External**: Stéphanie Thiagharajah (Voltalis)
**Department**: GTM
**Duration**: 12 min
**Grade**: **1 — Pass**
**Fireflies**: https://app.fireflies.ai/view/01KQSC4X435R27HC3F2M6727AY

#### Findings
No findings.

#### Notes
Henry absent (no spoken lines). Paul handles the call cleanly: accurate firm description, honest about product fit mismatch (Voltalis too small), no product recommendations. Positive example of compliant APA PMI conduct.

**Escalation**: No.

---

### Model ML x Kota — 01KPZMN04Q9ZSKWSFKJ0183Y9N — 2026-05-05
**Kota speaker(s)**: Henry Godson — Script pathway BDR (❌ absent, no spoken lines); Callum Pearse — Qualified Pensions (✅), New Entrant PMI (⚠️)
**External**: Tom Hughes (Model ML)
**Department**: GTM
**Duration**: 25 min
**Grade**: **2 — Pass with comments**
**Fireflies**: https://app.fireflies.ai/view/01KPZMN04Q9ZSKWSFKJ0183Y9N

#### Findings
| Criterion | Severity | Timestamp | Transcript span | Regulation |
|---|---|---|---|---|
| Observation | Informational | Throughout | Callum (PMI New Entrant) describes PMI providers (Vitality, Bupa, Aviva, AXA) and pension/group risk; no supervisor on call | MCC New Entrant supervision |

#### Notes
Henry absent (no spoken lines). Callum stays within scope: transparent about geographic limitations (no US), refers to Dan as benefits lead, manages discovery professionally without specific product recommendations.

**Escalation**: No.

---

### Gabriela x Kota Intro — 01KQQEB7P2H826H7MR9K9ZTQ4D — 2026-05-05
**Kota speaker(s)**: Henry Godson — Script pathway BDR (❌ absent, no spoken lines); Paul O'Hanlon — Qualified APA PMI (✅)
**External**: Gabriela Merea (Cambiaso Risso)
**Department**: GTM
**Duration**: 14 min
**Grade**: **1 — Pass**
**Fireflies**: https://app.fireflies.ai/view/01KQQEB7P2H826H7MR9K9ZTQ4D

#### Findings
No findings.

#### Notes
Henry absent (no spoken lines). Paul's conduct is exemplary: accurate firm description, live platform demo, no recommendations, no plan comparisons, transparent about fit. Grade 2 only for disclosure phrasing — recommend standardising the opener script.

**Escalation**: No.

---

### Kota x Riot Games Intro — 01KQ5DJ7ANYBBSJSFKXSPP5RE7 — 2026-05-07
**Kota speaker(s)**: Katie Garry — Script pathway BDR (❌ unqualified); Paul O'Hanlon — Qualified APA PMI (✅)
**External**: Nike Furlong (Riot Games EMEA HR)
**Department**: GTM
**Duration**: 19 min
**Grade**: **3 — Fail**
**Fireflies**: https://app.fireflies.ai/view/01KQ5DJ7ANYBBSJSFKXSPP5RE7

#### Findings
| Criterion | Severity | Timestamp | Transcript span | Regulation |
|---|---|---|---|---|
| HF-00 | High | ~09:00 | Katie Garry (script pathway BDR ❌): "Nico, sorry, just with regards to, you know, your renewals, are you involved with that or is that more part of the US team as well?" — Katie actively participates in substantive PMI renewal discussion, crossing script pathway carve-out | CBI MCC 2017 — script pathway BDR active in regulated product discussion |
| HF-00 | Medium | ~14:37 | Katie: "So we have 50 in total. And then in the Dublin office, I think at the moment we have about. There's, I think 20 in. But I think there's around 30 are in the Dublin office..." — active participation in regulated call context | CBI MCC 2017 |

#### Notes
Paul's conduct throughout is clean. The failure is Katie's active participation beyond a pure admin/intro role: the renewals question probes the commercial relationship in a regulated PMI context and is outside the script pathway carve-out.

**Escalation**: No per spec (Katie is script pathway, not unregistered; no ES-01/02/03 triggers). Flag to GTM management for BDR role boundary coaching.

---

### KOTA / Allianz White Label Platform — 01KQQFE4XGGC4D3FEANP3NF53Y — 2026-05-05
**Kota speaker(s)**: Luke Mackey — Removed from APA Pensions register Sept 2024 (❌); Matthew Brennan — New Entrant (⚠️)
**External**: Marco Fattori, Patrick Lawlor, Paul Hogan (Allianz Partners)
**Department**: GTM
**Duration**: N/A
**Grade**: **1 — Pass**
**Fireflies**: https://app.fireflies.ai/view/01KQQFE4XGGC4D3FEANP3NF53Y

#### Findings
No findings.

#### Notes — Luke Mackey
Luke Mackey (deregistered APA Pensions) participates as CEO in commercial/strategic B2B discussion with Allianz Partners. Does not conduct consumer-facing regulated activity on this call. Compliance to confirm Luke's external commercial call perimeter given deregistered status.

#### Notes
B2B platform partnership meeting — not a consumer-facing regulated product call. Luke's deregistration is a live compliance concern but on this call he does not engage in regulated activity. Recommend Compliance confirm Luke's external commercial call perimeter.

**Escalation**: No.

---

### Advised Sales Meeting — 01KQFMTW78W68T3RCFQTV34PFJ — 2026-05-05
**Kota speaker(s)**: Trevor Gardiner — Fully Qualified QFA (✅); Elaine Kinsella — Compliance/Legal (internal capacity)
**External**: Richard Jackson (Innovative Risk, FCA-regulated compliance consultant); Patrick O'Boyle (Yonder)
**Department**: Internal — Compliance/Legal
**Duration**: 39 min
**Grade**: **1 — Pass**
**Fireflies**: https://app.fireflies.ai/view/01KQFMTW78W68T3RCFQTV34PFJ

#### Findings
No findings — internal compliance strategy meeting with an external professional consultant. No retail consumer present; no regulated product advice given.

#### Notes
Trevor and Elaine consult Richard Jackson (Innovative Risk) about the framework for moving from non-advised to advised sales. Elaine explicitly references the existing call monitoring programme. Discussion of Luke Mackey's FCA registration process. Demonstrates strong institutional regulatory awareness.

**Escalation**: No — not a customer-facing call.

---

### Kota x Carwow — 01KQYYQJH8SX5KVDYPJ7ECV7MR — 2026-05-08
**Kota speaker(s)**: Daniel McAvinue — Qualified Pensions/Life (✅), New Entrant PMI (⚠️); Simon Ward — Script pathway CS Co-ordinator (❌)
**External**: Idan Shteinberg (Carwow)
**Department**: CS
**Duration**: 30 min
**Grade**: **3 — Fail + ES-01/ES-02 escalation**
**Fireflies**: https://app.fireflies.ai/view/01KQYYQJH8SX5KVDYPJ7ECV7MR

#### Findings
| Criterion | Severity | Timestamp | Transcript span | Regulation |
|---|---|---|---|---|
| HF-02 | High | ~12:31 | Dan: "if you are really sick, you know, ultimately you'd be better served under paper." — comparative quality judgement: BUPA better than Vitality for serious illness, presented as a factual conclusion | CPC 2025 Part 3 — clear, fair, not misleading |
| HF-02 | High | ~17:59 | Dan: "This doesn't relate specifically to you, but if I look at all of the new schemes that are coming through us at the moment when we quote with Vitality and Bupa at the moment, Bupa is often 10 to 15% cheaper for the exact same cover." — directional pricing claim using aggregate data | CPC 2025 Part 3 |
| HF-02 | High | ~20:36 | Dan: "I'd personally be surprised if they weren't able to come in with a price either at the same level or cheaper than what Vitality will give you." — personal opinion framed as near-certainty on pricing | CPC 2025 Part 3 |
| HF-00 | Medium | ~27:24 | Simon Ward (script pathway CS Co-ordinator ❌): "I'm sure you're aware Edan, that Matthew moved to the GM platform role. So he's sort of overseeing all products go to market..." — active participation in regulated PMI renewal call | CBI MCC 2017 |
| ES-01 | Escalation | ~02:57 | Idan: "In the past few months we received a few complaints from employees about vitality...the very bad experience that we had with them regarding the five employees that we wanted to enroll, which was absolutely appalling." | MCC ES-01 — customer distress / complaint |
| ES-02 | Escalation | ~04:30 | Idan: "the complaints we have for employees are around how difficult it is to prove vitality, that a potential claim is not pre existing condition...they give you a booklet that they expect the GP to complete. Now that's very unacceptable." — active coverage/claims dispute | MCC ES-02 — coverage dispute / potential liability |
| SF-12 | Soft | ~15:23 | Dan: "The Vitality program, like across all of the healthcare providers, is absolutely the best rewards program." | MCC SF-12 |
| SF-13 | Soft | ~12:31 | Dan: "if you are really sick, you know, ultimately you'd be better served under paper." — disparaging Vitality's claims capability | MCC SF-13 |

#### Notes
ES-01 and ES-02 both triggered: Idan reports active employee complaints about Vitality and a specific claims dispute (GP booklet process). Dan's three HF-02 breaches include a directional pricing claim and a comparative quality judgement presented as factual conclusions. Simon Ward's active participation in a regulated PMI renewal call is a script pathway breach.

**Escalation**: Yes — ES-01 and ES-02 triggered. Task placed in Escalated section, assigned to Simon Ellis.

---

### Kota / CHM — Pension Update — 01KQZFKDCM3EVJTVHZMEYJH500 — 2026-05-08
**Kota speaker(s)**: Simon Ward — Script pathway CS Co-ordinator (❌ unqualified) — leads entire call solo; Daniel McAvinue — Qualified Pensions/Life (✅) — absent, no spoken lines
**External**: Laura Mc Quaid, HR (CHM Ltd)
**Department**: CS
**Duration**: 28 min
**Grade**: **5 — Severe Fail**
**Fireflies**: https://app.fireflies.ai/view/01KQZFKDCM3EVJTVHZMEYJH500

#### Findings
| Criterion | Severity | Timestamp | Transcript span | Regulation |
|---|---|---|---|---|
| HF-00 | Critical | ~01:21 onwards | Simon Ward (script pathway CS Co-ordinator ❌) leads the entire call solo: explaining pension scheme enrollment failures, contribution status, regulatory compliance position, employee options (occupational pension vs. My Future Fund), and quasi-advice on employer communications. Simon holds no regulated qualification. | CBI MCC 2017; APA Pensions requirement; OPSA |
| HF-05 | High | ~22:30 | Simon: "we have deducted from their pay slip. Like it has been a pension contribution that has been assigned to their pay slip that we're then refunding to them." — characterising legal/tax status of pension deductions for specific named employees | CBI MCC 2017; pension regulation |
| HF-05 | High | ~07:00 | Simon: "no employees will be worse off from this. Yeah it's just a reassurance and it's just that it's a confirmation that we're not gamma just." and "nothing wrong has been done." — representing the regulatory and legal position of the situation | CBI MCC 2017 |
| HF-00 | Critical | ~14:38 | Simon: "the decision for him is, does he want to continue with an occupational pension? We have the funds, we haven't refunded them yet. Then we can, we can do that. If he wants to be refunded and go to my future fund. Absolutely. We can also do that." — framing pension decision options for specific named employees without qualification | CBI MCC 2017; APA Pensions |
| ES-02 | Critical | ~16:56 | Laura: "he has his WRC lodge. I'm just waiting on a round envelope...he's lodged it with the wrc." — live WRC (Workplace Relations Commission) complaint by a named employee directly related to Kota's pension administration error | MCC ES-02 — coverage dispute / legal complaint |
| ES-03 | Critical | ~15:47 | Simon: "I'm not going to say employment type. We'll come up with some way of explaining that caused a bug that basically caused you to be removed from coda." — Simon agrees to draft communications obscuring the true cause of the administration failure | MCC ES-03; Consumer Protection / transparency obligations |
| HF-09 | High | ~17:18 (mobile) / ~16:56 (email) | Laura shares personal mobile number on recorded call: "So I am 087-490-7363" — Simon confirms he will save it. Additionally Laura: "I was kind of just trying to stay off the email just because I don't want to be putting too much in the email" — GDPR request avoidance strategy discussed on a recorded call | GDPR Art. 5; MCC HF-09 |
| HF-03 | High | ~07:00 | Simon: "The pension regulator they're, they're. They're fully aware of the scenarios that are like." — regulatory authority claim Simon is not qualified to make | CBI MCC 2017; HF-03 — misrepresented regulatory status |
| SF-10 | Soft | ~16:56 | Simon agrees to use WhatsApp/phone instead of email specifically to avoid creating a written record around the active GDPR request | MCC SF-10 — circumvention |

#### Notes
This is the most severe finding of the week. Simon Ward — Script pathway CS Co-ordinator with no regulated qualifications — led a regulated pension administration call solo while the qualified Kota contact (Dan McAvinue) was absent.

Key findings:
- A named employee (Leon) has lodged a WRC complaint related to Kota's pension enrollment failure
- Simon agreed to draft communications designed to obscure the cause of the failure ("I'm not going to say employment type")
- Simon and Laura discuss a strategy to avoid email trails specifically because of the active GDPR request
- Laura's personal mobile number (087-490-7363) is shared on a recorded call
- Simon makes an unqualified claim about the pension regulator's awareness

**Escalation**: Yes — Grade 5, ES-02 (WRC complaint), ES-03 (agreement to draft misleading communications), HF-03 (misrepresented regulatory status), HF-09 (GDPR/PII). Immediate escalation to Simon Ellis. Legal review required for WRC complaint. All communications drafted pursuant to this call must be reviewed before sending.

### Calls Not Pulled (Lower-Risk — Qualified Staff Primary)

The following calls have qualified Kota staff as the primary speakers and no unregistered/script-only staff operating independently. Assessed as likely Grade 1 (Pass) or Grade 2 based on participant list; not pulled due to context constraints. Should be spot-checked by Compliance:

| Title | Kota Staff | Notes |
|---|---|---|
| Kota x David Barker | Callum Pearse + Dan McAvinue | Both qualified |
| Kota & Exile — Employee Benefits | Paul O'Hanlon | Qualified APA PMI |
| Maria Jefcoate and Charlie Blake | Charlie Blake + Trevor + Paul | All qualified |
| KOTA X Irish Life Wellbeing Catch Up | Charlie Blake | Qualified APA PMI |
| Remote GL,IP,CIC & Rise | Naoise Baker + Trevor | Both qualified |
| Kota / Linear — Platform & HRIS | Simon Ward + John Hayes | John Hayes unknown — recommend spot-check |
| 30 min with Callum | Callum Pearse | Qualified Pensions |
| Kota / CLS — Biweekly | Dan + Simon Ward | Dan qualified; Simon facilitative |
| Kota / Sliide | Dan + Simon Ward | Dan qualified; Simon facilitative |
| Kota <> Wayflyer — Weekly | Dan + Simon + Matthew Brennan | Matthew New Entrant — recommend spot-check |
| Kota / Tines — Bi-weekly | Dan + Simon + Trevor | Trevor present; lower risk |
| Shaw Gibbs x Kota | Dan + Callum | Both qualified |
| Gaelvert x Kota | Callum Pearse | Qualified Pensions |
| Kota Intro (Gaelvert) | Callum Pearse | Qualified Pensions |
| Sarah <> Callum: Kota Intro | Callum Pearse | Qualified Pensions |
| Kota & Sentient — Benefits Chat | Paul O'Hanlon | Qualified APA PMI |
| Aikido <> Kota | Karl O'Brien + Dan McAvinue | Karl script pathway — recommend spot-check |
| Bark <> Kota — Open Questions | Karl O'Brien + Dan McAvinue | Karl script pathway — recommend spot-check |
| LearnUpon x Kota Onboarding | Dan + Simon + Callum + John Hayes | John Hayes unknown — recommend spot-check |
| Kota / CHM - Pension Update | Dan + Simon Ward | Assessed by agent |

---

## Cross-Call Patterns

### Karl O'Brien — Systematic Regulated Activity Without Supervision (CRITICAL)
Karl O'Brien (Script pathway) conducted **3 fully regulated advisory calls solo** this week (Volta, Enrico Grande, Jennifer Kenyon), in addition to clean platform demos (DailyPay) and accompanied commercial meetings (Frontiers). In all three solo advisory calls:
- Full regulated product information provided (PMI underwriting, pension contribution mechanics, pension provider quality comparisons)
- Explicit recommendations made ("I would recommend", "I would say it is better off to go with")
- No qualified supervisor present
- Karl self-references the FCA regulatory constraint but proceeds regardless

Three Grade 4 failures on solo calls in a single week is a systemic pattern. **Recommend immediate supervisor intervention by Trevor Gardiner, review of all Karl O'Brien call recordings this week, and temporary suspension of Karl from solo customer calls pending compliance coaching.**

### Simon Ward — Script Pathway CS Co-ordinator Conducting Independent Regulated Activity (CRITICAL)
Simon Ward appeared on 8+ CS calls this week. In the majority, Dan McAvinue (qualified) ran the substantive content while Simon facilitated — structurally compliant. However on CHM Pension Update (01KQZFKDCM3EVJTVHZMEYJH500), Simon led the entire regulated pension administration call solo while Dan was absent. This is a Grade 5 Severe Fail. **Immediate escalation to Simon Ellis. Review all Simon Ward solo call recordings.**

### Daniel McAvinue — HF-02 Pattern on PMI Calls
Dan McAvinue (Qualified Pensions/Life, New Entrant PMI) made multiple comparative value judgements on PMI providers in the Carwow call: directional pricing claims ("Bupa is often 10 to 15% cheaper for the exact same cover"), near-certainty pricing opinions, and quality comparisons disparaging Vitality's claims performance. While Dan is qualified, HF-02 applies regardless of qualification status — comparative value judgements in the absence of full factual basis are prohibited. **Recommend Dan review HF-02 boundaries with Trevor Gardiner.**

### Henry Godson — Structural Compliance Pattern
Henry Godson (Script pathway BDR) organised and is listed as host on 5 calls this week (Anjana, Voltalis, Model ML, Gabriela, and one other). On all assessed calls, Henry had zero spoken lines — qualified staff (Paul O'Hanlon, Callum Pearse) ran the substantive content. This is structurally compliant. However, the pattern warrants monitoring to confirm Henry is genuinely absent and not driving regulated conversations off-record before handover.

### Kate Fullen — Attendance on Regulated Calls
Kate Fullen (`kate@kota.io`) attended the PMI Via Employment Hero call but did not speak. Her presence on regulated product calls as an unregistered person (no MCC qualifications) is a compliance risk regardless of speech. **Recommend Compliance confirm Kate is not participating in regulated calls in any capacity and take immediate action per the April 2026 Action Log.**

---

## Open Questions for the Designer

1. The boundary between "platform demo" and "regulated advisory" is blurry when the same rep (Karl) conducts both types on the same day. Should there be a structural rule that script-pathway staff may only run demo calls with a qualified person present?
2. The Life Scientific call involved employees raising HMRC/pension ombudsman concerns (ES-02 trigger). The conversation was handled appropriately. Should ES-02 generate a task when the customer raises it but Kota staff handle it correctly?
