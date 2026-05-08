---
title: Detection Criteria — Call Monitoring Agent v1
created: 2026-05-08
updated: 2026-05-08
type: requirements
derived_from:
  - Researcher/research-call-supervision-audit.md
  - Researcher/research-mcc-fitness-probity.md
---

# Detection Criteria — Call Monitoring Agent v1

What the call monitoring agent must detect, ranked by priority and mapped to the regulation or risk that motivates each detection. Each criterion is grounded in either (a) a breach actually flagged by the human compliance reviewer in the **☎️ Call Supervision Audit** (June 2025 – March 2026), or (b) an explicit Don't in Kota's internal **Financial Product Information to Customers** / **Advice to Customers** cheat sheets — so the Designer can build prompts against documented policy and documented behaviour, not hypothetical risk.

## Master frame: MCC + F&P + SM&CR

The Call Supervision Audit lives under the **MCC Supervision** parent page in Notion. The whole programme is anchored to the Central Bank of Ireland's **Minimum Competency Code 2017** and the **Fitness & Probity** regime (S.I. 60/2011 + IAF 2024) for IE staff, and to **FCA SYSC 28 + SM&CR** for UK staff.

Two consequences for every criterion below:

1. **Information is a regulated activity under MCC**, not just advice. An unqualified speaker who describes the type of cover or excesses in a Kota plan, or compares two Kota plans, is conducting a regulated activity outside their authorisation — even with neutral language. Several of the existing detections (HF-01, HF-02) therefore have a stricter form when the speaker is unqualified.
2. **Speaker identity is an input to the agent**, not just transcript text. The agent must resolve each speaker against an MCC/F&P register (Person → qualifications → product scope → F&P/PCF status). Where no register lookup is available, the agent must **fail closed**: treat the speaker as unqualified.

See `Researcher/research-mcc-fitness-probity.md` for the full framework and the qualifications-by-product matrix (QFA, APA, APP, CIP, ACII/FCII, IIPM, etc.).

Conventions:
- **Hard rule** = always flag if matched (HF-prefix).
- **Soft signal** = flag only when N≥2 in the same call, or when co-occurring with a hard rule (SF-prefix).
- Priority: **High** = perimeter / regulatory authorisation breach or material customer harm; **Medium** = disclosure/process gap that is correctable with scripting; **Low** = tone/language hygiene.
- Where a criterion behaves differently by speaker authorisation, it is annotated **[Speaker-scoped]**.
- Examples are anonymised paraphrases of audit excerpts, not verbatim customer transcript.

> **Excluded from agent detection — recording/call consent**: Kota collects recording consent from participants before each call begins (pre-call consent flow). The agent must **not** flag the absence of a verbal recording disclosure at the start of a call transcript. This is not a detection criterion.

---

## Tier 1 — High priority, hard rules

### HF-00 — Unqualified speaker conducting MCC-regulated activity [Speaker-scoped]
**Description**: The speaker is not on the MCC/F&P register for the product they are discussing, and they are doing one of the three regulated activities defined by MCC 2017:
- (a) providing **advice or information** on a retail financial product (life assurance, pensions, personal general insurance, private medical insurance, mortgages, deposits)
- (b) **arranging or offering to arrange** a retail financial product (including amendments to insurance cover and restructuring/rescheduling of loans)
- (c) exercising a **specified function**

The carve-outs in MCC 2017 (pointing out where info can be found; mere general info; brochure pass-through; back-office; incidental info alongside an unrelated professional activity) are **not** breaches and must not be flagged.
**Why High**: This is the umbrella rule that motivates the rest of Tier 1. It is the rule the human reviewers operate under (the audit lives under "MCC Supervision"), and Kota's internal "Financial Product Information to Customers" cheat sheet treats it as binding policy.
**Trigger logic** (Designer to implement):
- Resolve the speaker against the MCC register; obtain `qualifications: [...]`, `product_scope: [...]`, `f&p_status`.
- If the speaker is not registered, default to `qualifications: []`.
- For each utterance about a retail financial product, classify the activity (info / advice / arranging / out-of-scope-carve-out).
- Flag if the activity is in scope AND the speaker's product_scope does not include the product.
**Positive example**: a Sales Development rep with no MCC qualification describes the dental and optical limits inside Kota's PMI cash plan to a prospect.
**Negative example**: the same rep says "we offer cash plans and PMI through Kota; here's the link to the FAQ and the IPID — happy to introduce you to a colleague who can walk through the cover detail."
**Regulation / risk mapping**:
- **CBI Minimum Competency Code 2017** — definition of regulated activity (advice OR information; arranging; specified function); qualification requirements
- **Fitness & Probity Standards** (S.I. 60/2011 + Individual Accountability Framework 2024) — competence and capability standard
- **FCA SYSC 28** — knowledge and ability requirements for UK staff
- **FCA SM&CR Certification Regime** — annual certification for significant-harm roles
- **FCA Individual Conduct Rules** (Tier 1) — apply to **all** UK staff regardless of certification
- **Kota internal**: `Financial Product Information to Customers` cheat sheet; `Advice to Customers` cheat sheet
**Source incidents**: structurally underlies every HF in Tier 1; explicit reviewer references include Q4-25-FR-01 ("reserved for a QFA (Ireland) or UK authorised adviser"), Q2-25-F-01 ("member of benefits needs to be present for renewals as this is regulated activity"), Q3-25-PC-04 ("review those timestamps as PCF17").

---

### HF-01 — Explicit personal recommendation [Speaker-scoped]
**Description**: The speaker makes an explicit recommendation to act, choose, increase/decrease, switch, or transfer in relation to a financial product (pension, PMI, life, income protection, PRSA).
**Why High**: This is the single most common breach in the audit (≥9/13 calls). It directly crosses the regulated-advice perimeter and exposes the firm to enforcement.
**Trigger families** (Designer to expand):
- "I recommend…", "I'd recommend…", "what I would recommend"
- "you should…", "the best thing to do is…", "the right choice is…"
- "what might be best for you", "best option for your team"
**Positive example (flag)**: rep tells customer "what I would recommend is set the maximum employer contribution to 1.5%."
**Negative example (don't flag)**: rep says "the platform allows you to set a maximum employer contribution; companies typically pick a level that suits their payroll."
**Regulation / risk mapping**:
- CBI Consumer Protection Code (CPC) — advice / personal recommendation rules
- MiFID II Art. 24–25 — investment advice
- Insurance Distribution Regulations 2018 (S.I. 229/2018) Reg. 23(1)(e) — disclosure of whether advice is given
- FCA COBS 9 / PERG 8.24–8.30 — personal recommendation perimeter
- Internal: Kota policy that non-advised staff must not give a recommendation
**Source incidents**: Q2-25-F-01, Q3-25-PC-02, Q4-25-FR-01 (Severe — repeated across two calls), Q4-25-PC-04, Q4-25-NF-02, Q1-26-SF-01

---

### HF-02 — Comparative value judgement on regulated products or schemes [Speaker-scoped]
**Description**: The speaker asserts that one regulated product, scheme, provider, or configuration is **better / superior / more advantageous** for the customer (or their employees) than another.
**Why High**: The audit shows this is functionally indistinguishable from a recommendation in CBI/FCA terms, even when the speaker frames it as opinion or general experience.
**Trigger families**:
- "so superior to…", "much better than…", "more advantageous", "real benefit"
- "their scheme falls down on…", "where they're weak is…"
- "98% of clients do this" (social proof anchoring)
**Positive example**: "the occupational scheme is so superior to My Future Fund — I'd be stunned if any employee chose otherwise."
**Negative example**: "here's how the occupational scheme and My Future Fund differ on contributions, access age, and AVCs — happy to walk through trade-offs."
**Regulation / risk mapping**:
- CPC 2025 Part 3 — clear, fair, accurate, not misleading
- IDD Art. 17(2) / ICOBS 2.2.2R — communications fair, clear, not misleading
- Same advice-perimeter regulations as HF-01 once the comparison is paired with a customer-specific frame
**Source incidents**: Q4-25-FR-01, Q4-25-NF-02, Q4-25-PC-04, Q4-25-PC-05

---

### HF-03 — Misrepresented firm role, capability, or regulatory status
**Description**: The speaker states or implies the firm or staff member has a capability, authorisation, or scope it does not have.
**Why High**: Severe Fail Q1-26-SF-01 was graded 5/5 entirely on this basis. Misrepresentation is both a CPC "clear/fair/not misleading" breach and a potential consumer-detriment trigger.
**Trigger families**:
- Calling sales/CS staff "qualified financial advisors" when they are not
- Claiming geographic or product scope the firm does not hold (e.g. "we go to market for the most competitive quotes" when only one provider is on panel; "we're global" when EEA-only)
- Implying intermediary or advisory permissions the firm does not hold ("everything I say is regulated")
**Positive example**: rep says "we go out to the market and get the most competitive quotes" when the firm only deals with one pension provider.
**Negative example**: "we currently work with [one provider]; we're working to expand panel coverage over time."
**Regulation / risk mapping**:
- CPC 2025 Part 3 (clear/fair/accurate)
- IDR S.I. 229/2018 Reg. 23(1)(a)–(d) — accurate identification and regulatory status
- IDD Art. 18 / Art. 17(2)
- FCA PRIN 2A.5 (Consumer Understanding); Financial Promotion regime
**Source incidents**: Q1-26-SF-01 (Severe Fail — misled on global coverage and going-to-market for quotes), Q4-25-PC-01 ("Dan's team are qualified financial advisors"), Q4-25-PC-03 ("we're regulated… everything I say is regulated"), Q3-25-PC-04 (whole-of-market future tense)

---

### HF-04 — Cross-selling or arranging a regulated product without authorisation [Speaker-scoped]
**Description**: A non-advised speaker introduces, promotes, or offers to arrange a quote/setup for a regulated product (life assurance, income protection, PMI, pension transfer) outside of an advised channel.
**Why High**: This is the activity-level breach the FCA general prohibition (FSMA s. 19) and IDR Reg. 5 are written to prevent. Q2-25-F-01 was graded Fail specifically for this.
**Trigger families**:
- "I'll put my benefits colleagues in the loop and request a quote"
- "we can also offer life assurance and income protection — should I set that up?"
- Discussing pension transfers ("they can bring those funds in") without an advised disclaimer
**Positive example**: CS rep offers "I'll get a quote for life assurance and income protection."
**Negative example**: "I'm not authorised to handle quotations, but I can refer you to our authorised benefits team."
**Regulation / risk mapping**:
- IDR S.I. 229/2018 Reg. 5 — distribution authorisation
- IDD Art. 3 — registration
- FCA FSMA s. 19 — general prohibition; FSMA s. 21 — financial promotion
- Internal: separation of advised vs non-advised channel
**Source incidents**: Q2-25-F-01

---

### HF-05 — Tax, social-welfare, or pensions-law guidance to a specific person/scenario [Speaker-scoped]
**Description**: The speaker gives a conclusion about how tax, auto-enrolment eligibility, or other public-law rules apply to a named individual or specific scenario.
**Why High**: Outside the firm's authorisation; reviewers consistently mark these as Red.
**Trigger families**:
- "If she's married she'll be sharing tax credits with her husband"
- "She won't be included in auto-enrolment because she's on unpaid leave"
- "There's no P11D anymore very soon"
**Positive example**: rep tells customer "if she's married, tax credits work like X."
**Negative example**: "tax treatment depends on personal circumstances — best to confirm with the customer's tax adviser or Revenue."
**Regulation / risk mapping**:
- CPC 2025 — advice perimeter
- Tax legislation — only Tax Advisers / appropriately qualified persons may advise
- Auto-Enrolment Retirement Savings Act 2024 (Ireland) — eligibility determined in legislation, not by intermediary
- QFA requirement (Ireland) for pension advice
**Source incidents**: Q4-25-PC-04, Q4-25-PC-05 (auto-enrolment exemption claim), Q4-25-NF-02 (P11D claim)

---

### HF-06 — Unsecured handoff of customer personal data
**Description**: The speaker proposes, agrees to, or completes transferring identifiable employee data (PPS numbers, DOB, salary, address, health information) outside an in-product secure flow — typically by email or unencrypted file.
**Why High**: GDPR breach risk is material and irreversible; reviewer graded this Red.
**Trigger families**:
- "Send me the spreadsheet by email"
- "Just attach it and I'll upload on your behalf"
- Sending password-protected Excel + emailing the password
**Positive example**: rep agrees to receive a spreadsheet of employee PPS numbers via email.
**Negative example**: "for GDPR reasons we can't accept personal data over email — please use the secure upload in the app, or we can open a secure transfer link."
**Regulation / risk mapping**:
- GDPR Art. 5(1)(f) — integrity and confidentiality
- GDPR Art. 32 — security of processing
- GDPR Art. 28 — processor obligations / DPA
- DPC guidance on insurance-quote data
- See [[Data Retention]] for retention overlay
**Source incidents**: Q4-25-PII-01

---

### HF-10 — Unqualified speaker describes type of cover, excesses, or plan-specific benefits [Speaker-scoped]
**Description**: An unqualified speaker (per HF-00) describes the **type of cover**, **excesses**, **limits**, **inclusions**, or **plan-specific benefits** of a Kota-distributed insurance or pension product, beyond high-level platform features.
**Why High**: Direct, named breach in Kota's `Financial Product Information to Customers` cheat sheet — listed as a Don't. The audit reviewers under-flag this pattern relative to advice-style language, but the internal policy is unambiguous.
**Trigger families**:
- Naming specific cover lines: "the cash plan covers dental up to €X", "PMI includes mental-health and EAP"
- Quoting excesses, limits, deductibles, waiting periods: "no excess on optical", "6-month dental waiting period"
- Confirming or denying coverage of a scenario: "yes that's covered", "no that wouldn't be claimable"
**Positive example**: an unqualified rep tells a prospect "the cash plan covers dental up to €500 and includes EAP, optical, and mental health add-ons."
**Negative example**: same rep says "the IPID and policy doc list cover details and limits — I'll send them, and our authorised benefits colleague can walk through specifics."
**Regulation / risk mapping**:
- **MCC 2017** — "information" on a retail financial product is a regulated activity
- **IDR S.I. 229/2018 Reg. 23(1)(e)** — disclosure of whether advice is given
- **IDD Art. 17(2) / ICOBS 2.2.2R** — clear, fair, not misleading
- **Kota internal**: `Financial Product Information to Customers` ("Don't provide details on the type of cover or details on excesses that is provided in a particular plan")
**Source incidents**: Q3-25-PC-03 (multiple absolute coverage statements); Q3-25-PC-01 (cash-plan/PMI feature description by unqualified rep flagged as "soft recommendation"); Q3-25-PC-02 (PMI add-ons described as "what's going to drive tangible value").

---

### HF-11 — Unqualified speaker compares plans (Kota↔Kota or Kota↔competitor) [Speaker-scoped]
**Description**: An unqualified speaker compares two or more retail financial products — between Kota's own plans, or between a Kota plan and a competitor's. Comparison is the second named Don't in the internal cheat sheet and reliably tips a call from "information" into "advice" under MCC and CPC.
**Why High**: Direct, named breach in Kota's `Financial Product Information to Customers` cheat sheet. Co-occurs with HF-02 in the audit, but is a distinct rule: comparison without a value judgement is still a breach when the speaker is unqualified.
**Trigger families**:
- "Plan A vs Plan B" feature/price contrasts within Kota
- "We're cheaper than X / better than X" against a named competitor
- "Their service falls down on X" / "they don't do Y like we do"
- Pension scheme comparisons (occupational vs My Future Fund, PRSA vs occupational)
**Positive example**: unqualified rep walks the prospect through "the difference between our Bronze and Silver PMI is the dental allowance and outpatient limit."
**Negative example**: "we offer multiple PMI tiers; the IPIDs have full feature comparisons — happy to introduce you to our authorised colleague to walk through the trade-offs."
**Regulation / risk mapping**:
- **MCC 2017** — comparison is information about a specific retail financial product
- **CPC 2025 Part 3** — clear, fair, accurate, not misleading
- **IDD Art. 17(2)**
- **FCA COBS 4.2.4R** (clear, fair, not misleading promotions)
- **Kota internal**: `Financial Product Information to Customers` ("Don't provide comparisons between the plans Kota provide OR between the plans Kota provide versus other plans")
**Source incidents**: Q4-25-PC-01 (broker comparison + "where they fall down"), Q4-25-FR-01 (occupational vs My Future Fund), Q4-25-NF-02 (occupational vs AE comparison), Q4-25-PC-04 (PRSA vs occupational), Q4-25-PC-05 (occupational vs state scheme).

---

### HF-12 — Unqualified speaker discusses changing the level of cover or alternatives [Speaker-scoped]
**Description**: An unqualified speaker discusses changing a customer's level of cover (up, down, or sideways) or proactively raises alternatives to the customer's current arrangement. Listed as a Don't in `Advice to Customers`.
**Why High**: This is the policy-level equivalent of a recommendation: even raising alternatives, by an unqualified speaker, is a regulated activity outside scope.
**Trigger families**:
- "You could increase cover to…", "you might want to drop the dental add-on"
- "An alternative would be…", "another option you have is…"
- Discussing pension transfers, consolidation, or restructuring
**Positive example**: unqualified rep suggests "you could drop the dental add-on if cost is an issue."
**Negative example**: "if you'd like to look at alternatives or change the level of cover, our authorised benefits colleague can walk through that with you."
**Regulation / risk mapping**:
- **MCC 2017** — arranging or offering to arrange amendments to insurance cover is a regulated activity (limb (b))
- **IDR S.I. 229/2018 Reg. 5** — distribution authorisation
- **CPC 2025** — advice perimeter
- **Kota internal**: `Advice to Customers` ("do not discuss making any changes to the level of cover"; "avoid discussing alternatives")
**Source incidents**: Q2-25-F-01 (offered to arrange life/IP quotes), Q4-25-FR-01 (recommended changing minimum employer contribution), Q4-25-PC-05 (suggested specific contribution-level changes).

---

## Tier 2 — Medium priority, hard rules

### HF-07 — Regulatory-circumvention or "ways around" language
**Description**: The speaker frames a configuration or process as a way to avoid, evade, or work around a regulator, regulation, or scheme.
**Why Medium-High**: Rare but very damaging if found in audit; the language is itself a finding even where the underlying conduct is compliant.
**Trigger families**:
- "Finding ways around that"
- "Stops anyone going into the government scheme"
- "It's within the rules at the moment" (suggests time-limited gaming)
**Positive example**: "the regulators won't approve it, so we're finding ways around that."
**Negative example**: "where direct integration isn't possible, we use a compliant alternative workflow."
**Regulation / risk mapping**:
- CPC 2025 / CBI Standards for Business — Core Standard (act fairly and professionally)
- IDD Art. 17(1) — best interest of customer
- Reputational / supervisory risk
**Source incidents**: Q4-25-PC-01 ("finding ways around that"), Q4-25-NF-02 ("within the rules at the moment"), Q4-25-PC-05 (configuration to keep employees out of state scheme)

---

### HF-08 — Recording / consent disclosure missing or wrongly framed
**Description**: The call has no explicit consent ask for recording/transcription, or uses an incorrect basis (e.g. "we record because we're regulated").
**Why Medium**: Common across the sample but correctable with scripting; not by itself a customer-harm event but a clear compliance gap.
**Trigger families**:
- No opener line at all in first 90 seconds
- "I'm making the assumption that's all okay"
- "We record because we're regulated"
**Positive example**: rep starts the call without any reference to recording, or says "we record because we're regulated by central bank."
**Negative example**: "we record and transcribe to keep an accurate note — happy to proceed?"
**Regulation / risk mapping**:
- GDPR Art. 6 — lawful basis (consent or legitimate interest, properly framed)
- ePrivacy / PECR (UK)
- CPC 2025 — consent and customer information
- See [[Data Retention]] for retention rules
**Source incidents**: Q3-25-PC-03, Q3-25-NF-01, Q4-25-PC-03

---

### HF-09 — Inducement / commission disclosed in promotional terms
**Description**: Commission, override, or other remuneration is mentioned in a way that frames it as a benefit to the firm/rep rather than as neutral disclosure paired with a written schedule.
**Why Medium**: Direct IDR/IDD requirement; reviewers consistently flag the **wording**, not the disclosure itself.
**Trigger families**:
- "We get commission so you can start to make some money"
- "It's good for us if you go with X"
**Positive example**: "Irish Life takes 0.75% and pays us 0.15% — start to make some money."
**Negative example**: "in addition to the platform fee, we may receive commission from insurers; I'll send our schedule of fees and remuneration."
**Regulation / risk mapping**:
- IDR S.I. 229/2018 Reg. 23(1)(h) — nature of remuneration
- IDD Art. 19(1)(d)–(e)
- FCA SYSC 19F — inducements
- CPC 2025 disclosure
**Source incidents**: Q4-25-PC-03

---

## Tier 3 — Soft signals (flag if multiple co-occur or paired with a hard rule)

### SF-10 — Absolutes about coverage, premium, or outcome
**Description**: Use of absolute or near-absolute language about insurance cover, premium movements, or regulatory outcomes without "subject to terms / typically / may" qualifiers.
**Why Soft**: A single absolute is rarely a breach; a pattern of absolutes in the same call is.
**Trigger families**: "everything's covered", "full cover", "won't lose cover", "minuscule [premium impact]", "we can be certain", "regulators are generally understanding"
**Positive example**: "everything's covered, full refund on repatriation, premiums will be minuscule."
**Negative example**: "covered as per policy terms; any premium change is usually small but is subject to insurer repricing."
**Regulation / risk mapping**: CPC 2025 Part 3; IDD Art. 17(2); ICOBS 2.2.2R; FCA PRIN 2A.5
**Source incidents**: Q3-25-PC-03 (Poolside-equivalent), Q3-25-NF-01 (Loveable-equivalent)

### SF-11 — Specific penalty/figure claims for regulator behaviour
**Description**: The speaker quotes specific fines, daily penalties, or predicts regulator leniency.
**Why Soft**: Often well-meant ("don't panic"); becomes a hard issue when the figure is wrong or unsupported.
**Trigger families**: "Fines might be £50 a day", "the regulator is generally understanding", "TPR won't fine you"
**Positive example**: "fines might be something like £50 a day; they'll probably be lenient."
**Negative example**: "the Pensions Regulator may apply penalties; amounts depend on circumstances — let's get reporting in now."
**Regulation / risk mapping**: CPC 2025 Part 3; FCA PRIN 2A.5
**Source incidents**: Q3-25-NF-01

### SF-12 — Emotive or marketing language in regulated comms
**Description**: Use of "good news story", "Wild West", "real benefit", "compelling" when describing a regulated product, scheme outcome, or provider behaviour.
**Why Soft**: Tone-only; rarely a standalone breach but reviewers flag it consistently in Pass-with-comments calls.
**Positive example**: "it's all good news — the new scheme is a good news story for employees."
**Negative example**: "the outcome is: employer 1.5% is available without mandatory employee contributions."
**Regulation / risk mapping**: CPC 2025 Part 3; CBI Standards for Business (act fairly, professionally); FCA COBS 4.2 (financial promotions)
**Source incidents**: Q4-25-PC-02, Q4-25-PC-04

### SF-13 — Disparagement of competitors / unsupported comparative claims
**Description**: Unsupported negative claims about a competitor's processes, service, or governance.
**Why Soft**: Borderline; reviewers flag the assertion-without-evidence pattern, not comparison itself.
**Trigger families**: "their service falls down", "traditional broker nature can leave it open to mistakes"
**Positive example**: "where they fall down is service — traditional broker nature leaves it open to mistakes."
**Negative example**: "some customers tell us competitor service can feel renewal-led; we can show how our model differs."
**Regulation / risk mapping**: CPC 2025 Part 3; FCA COBS 4.2.4R (clear, fair, not misleading promotions)
**Source incidents**: Q4-25-PC-01

### SF-14 — Discouraging regulated advice
**Description**: The speaker tells the customer they don't need to consult an authorised adviser.
**Why Soft-but-watch**: Reviewers explicitly red-flag this when it occurs (Q3-25-PC-04). Add to soft signals only because it is rare; if matched, escalate.
**Trigger families**: "you don't need an IFA", "no need to talk to a financial adviser for this"
**Positive example**: "I don't think you need an independent financial advisor a lot of the time."
**Negative example**: "many companies also seek independent financial advice to ensure suitability; we don't provide that."
**Regulation / risk mapping**: CPC 2025 — best interest of customer; IDD Art. 17(1); FCA Consumer Duty (PRIN 2A)
**Source incidents**: Q3-25-PC-04

### SF-15 — Behavioural nudge to a specific contribution / opt-out outcome
**Description**: Speaker steers an individual employee's contribution decision (raise contributions on a pay rise, "you could go to zero but it's beneficial if…").
**Why Soft**: Often paired with HF-01; if HF-01 is matched, this is redundant. If HF-01 is not matched, the nudge alone is a Medium issue.
**Positive example**: "it's good to increase her percent when she gets a pay rise — feels less painful."
**Negative example**: "if employees ask about contribution levels, we direct them to provider resources or independent advice."
**Regulation / risk mapping**: CPC — personal recommendation; FCA COBS 9 / PERG 8
**Source incidents**: Q4-25-PC-05

---

## Tier 4 — Escalation triggers (route to human SME, do not auto-flag)

### ES-01 — Customer expresses vulnerability or distress
A complaint, financial-difficulty mention, mental health reference, bereavement, or pressure-to-act statement. The agent should not classify this — it should escalate to a human reviewer with the timestamp.

### ES-02 — Regulator, complaint, or litigation reference
Customer references a complaint to CBI, FCA, FOS, FSPO, or threatens litigation. Auto-escalate.

### ES-03 — New product, market, or regulator mentioned that the agent has no rule for
Out-of-distribution input. Better to escalate than to silently miss.

---

## Out of scope for v1

These were considered and excluded from the first version, to keep precision high:
- Sentiment / tone analysis beyond SF-12
- Speaker-level pattern tracking across calls (Compliance will track this manually from the Asana queue)
- Multi-language calls (if the call isn't English, escalate per ES-03)
- Action items mentioned on the call but executed elsewhere (e.g. an emailed spreadsheet sent after the call) — agent's perimeter is the transcript only

---

## Output requirements summary (handoff to Designer)

For each detection, the agent must output:
1. **Criterion ID** (HF-00 … HF-12, SF-10 … SF-15, ES-01 …)
2. **Severity** (High / Medium / Low / Escalate)
3. **Hard or Soft** (so Designer can apply the co-occurrence rule)
4. **Speaker** — the speaker's name (or stable ID) and resolved authorisation status: `qualified | unqualified | unknown`, with the product scope that authorisation covers
5. **Evidence quote** — the exact transcript span that triggered the detection
6. **Timestamp** — start/end as given by the transcript (matches reviewer convention)
7. **Recommended action** — one of: "Coach (language)", "Coach (perimeter)", "Refer to compliance", "Escalate to SME"

The Designer owns the prompt and schema; this document defines the **what**, not the **how**.

## Dependencies the Designer needs from outside this workspace

1. **MCC / F&P / SM&CR register** — a lookup of `speaker → qualifications → product scope → F&P/PCF status`. Not currently a single Notion page; the firm holds the source of truth in HR/Compliance. See `research-mcc-fitness-probity.md` for what fields are required. Until a register is wired in, the Designer must default any unrecognised speaker to `unqualified` (fail closed).
2. **Speaker-identity feed** — Fireflies provides speaker labels per turn; the Designer should confirm whether the labels are stable enough (name vs email vs employee ID) for register lookup.
3. **Product taxonomy** — the agent needs to classify each utterance against the four MCC product families (Life Assurance, Pensions, Personal General Insurance, Private Medical Insurance) so that speaker-product-scope checks resolve correctly.
