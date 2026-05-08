---
title: MCC, Fitness & Probity, and SMCR — Speaker Authorisation Framework
created: 2026-05-08
type: research
sources:
  - CBI Minimum Competency Code 2017
  - CBI Fitness & Probity regime (S.I. 60/2011 and successors; IAF 2024)
  - FCA SYSC 28 / SM&CR Certification Regime
  - Kota internal: "Financial Product Information to Customers" cheat sheet
  - Kota internal: "Advice to Customers" cheat sheet
  - Kota internal: "Regulatory Requirements" (UK/IE comparison)
  - Kota internal: Compliance & Risk FAQ (qualifications matrix)
---

# MCC, Fitness & Probity, and SMCR — Speaker Authorisation Framework

## Why this matters for the agent

The reviewers in the Call Supervision Audit do not just check **what was said** — they also check **who said it**. A phrase that is fine from a QFA can be a regulatory breach from an unqualified Customer Success rep. The Call Supervision Audit lives under the **MCC Supervision** parent page in Notion, alongside the Documentation Audit and Email Audit, which makes it explicit: the entire programme is anchored to the Minimum Competency Code, not just to advice rules.

The agent therefore needs a **speaker authorisation check** that runs before — or alongside — the language-pattern checks already in `req-detection-criteria.md`.

## What MCC actually covers

The Central Bank of Ireland's Minimum Competency Code 2017 (MCC) treats three things as **regulated activities** when conducted with a consumer in respect of a retail financial product:

1. **Providing advice OR information** on retail financial products
2. **Arranging or offering to arrange** retail financial products (including amendments to insurance cover and restructuring/rescheduling of loans)
3. **Exercise of a specified function**

The critical point that often surprises non-compliance staff: under MCC, **information is itself a regulated activity**, not just advice. "Information" means provision of information to a person, whether at the person's request or at the firm's initiative, that may assist them in the choice of a retail financial product.

There are narrow carve-outs. None of these is a "regulated activity":
- Pointing out where the customer can find information
- Mere provision of general information whose purpose is **not** to help the person conclude or fulfil a contract
- Providing a brochure/booklet without describing its contents
- Information in a newspaper, journal, lecture, or broadcast where the principal purpose is not to lead to a specific product
- Information given **incidentally** alongside a different professional activity not subject to MCC
- Information from **back-office** employees who do not have direct customer contact

Everything else — including saying which provider Kota uses, comparing two of Kota's plans, or describing what is or is not covered — falls inside the regulated activity definition under MCC.

### Required qualifications by product (per Kota's compliance FAQ)

| Product | Acceptable qualifications |
|---|---|
| **Life Assurance** | QFA · IIPM Member/Associate/Fellow (post-2006) · APA (Life Assurance) · Cert PFP w/ PFP designation · APP (Life Assurance) |
| **Pensions** | QFA · IIPM Member/Associate/Fellow (post-2006) · APA (Pensions) · Cert PFP w/ PFP designation · APP (Retirement Benefits) |
| **Personal General Insurance** | CIP · ACII/FCII · APA (Personal General Insurance) · APP (Personal General Insurance) |
| **Private Medical Insurance** | CIP · ACII/FCII · Diploma in PMI · APA (PGI) · APA (PMI) · APP (PMI) · APP (PGI) |

A QFA covers all four; APA and APP holders are scoped to the product the qualification names. **An unqualified rep must remain inside the carve-outs above.**

CPD: 15 hours per year is required, in both Ireland (MCC) and the UK (IDD via SYSC 28).

### Fitness & Probity overlay

Even when a person holds the right MCC qualification, the **F&P regime** (S.I. No. 60/2011 — Standards For Business; supplementary regulations; and the Individual Accountability Framework / IAF 2024) requires that they:

- Be **competent and capable**
- Act **honestly, ethically, and with integrity**
- Be **financially sound**

Pre-Approval Controlled Functions (PCFs) require CBI pre-approval; Controlled Functions (CFs) require firm-level certification. PCF17 (Head of Compliance with responsibility for AML/CFT) is referenced in the audit (e.g. case Q3-25-PC-04 directs the reviewer to "review those timestamps as PCF17"), confirming that the call supervision programme is part of the PCF17's accountability surface.

For the agent, the practical consequence is:
- A speaker's MCC qualification determines **what they may say about which product**.
- A speaker's F&P status determines **whether they may carry out the regulated activity at all**.
- A speaker who is qualified but acts outside their scope is just as much a breach as an unqualified speaker — the agent does not need to model F&P revocations, but the reviewer/escalation path does.

### UK overlay (FCA SYSC 28 + SM&CR)

For UK calls, the parallel regime is:
- **SYSC 28** — knowledge and ability requirements; firm assesses competence; 15 hours CPD per year (per IDD)
- **SM&CR Certification Regime** — annual certification for "significant harm" roles
- **Individual Conduct Rules** (Tier 1) — apply to **all** staff regardless of certification: act with integrity; with due skill, care and diligence; be open and cooperative with regulators; pay due regard to customer interests; observe proper standards of market conduct; act to deliver good outcomes for retail customers (Consumer Duty)

So even a UK-based platform-sales rep who never touches a regulated activity is bound by Tier 1 Conduct Rules — the agent's "tone" detections (SF-12, SF-13) hook into this.

## Kota's internal "info vs advice" boundary

Kota has published two short cheat sheets that operationalise MCC + F&P for non-qualified staff. These are the rules the agent should treat as the **internal policy backbone**.

### From "Financial Product Information to Customers"

Unqualified staff **must not**:
- Assist a customer to conclude or fulfil a contract in relation to insurance or pensions
- Assist a customer to fill out an insurance application
- Provide details on the **type of cover** or **excesses** that is provided in a particular plan
- Provide **comparisons** between the plans Kota provides, **or** between Kota's plans and other providers' plans

Unqualified staff **may**:
- Sell the platform & its benefits — not the insurance or pension product itself
- Provide links where the customer can find information
- Provide general (not plan-specific) information
- Provide a brochure or booklet without describing it
- Provide information from blogs/publications whose purpose isn't to push a product

### From "Advice to Customers"

Unqualified staff **must not**:
- Give advice or any personal recommendation — including expressing an opinion on whether cover is value for money / appropriate / has good coverage / is suitable
- "Sell" insurance by talking up benefits or constraints
- Discuss making changes to the level of cover
- Discuss alternatives

Unqualified staff **may**:
- Direct customers with specific questions to the insurance/pension documents, the provider, or the FAQs
- Direct potential claims to the provider
- Share factual policy information where necessary
- Answer specific questions about age limits or Lifetime Community Rating, pointing the customer to the FAQ

The internal note is unambiguous: *"if a customer believes we have given them insurance advice, then generally the Regulator and courts will conclude that we have."*

## How this changes the agent's design

Three concrete consequences for `req-detection-criteria.md` and the Designer's prompt:

1. **Speaker identity is an input, not just transcript text.** The agent needs the speaker's name, qualification status, and product scope. Source: a register maintained by Compliance/HR. Today there is no single Notion page that holds this; the Designer should expect the lookup as an external table or tool.
2. **Detections that are MCC-scoped behave differently for qualified vs unqualified speakers.** The same sentence ("our cash plan covers dental up to €500") is fine from an APA (PMI) holder and a breach from an unqualified rep.
3. **New hard rules need to come from the Kota cheat sheets, not just the audit findings.** The audit catches recommendations and capability claims; it under-catches the "describing the type of cover" and "comparing plans" patterns because reviewers focus on the headline issues. The agent should enforce the cheat sheet's Don'ts directly.

## The "MCC Register" gap

The user-referenced "Fitness and Probity / SMCR & MCC Register" is conceptually correct but not currently present in Notion as a single, structured page. What exists today:
- `Compliance & Risk` page — qualifications matrix by product (this note's source)
- `Hiring Process` → `Qualifications check` — confirms qualification at hire
- PCF Hiring Process — separate process for PCF/CF roles
- Governance Calendar — F&P board approval cadence

What the agent needs but does not have today:
- A live register: **Person → MCC qualifications held → product scope → F&P status → role (PCF/CF/other) → effective date**

The Researcher recommends this be created as a Notion database (or imported from the firm's HR/Compliance source of truth) so the agent can deterministically resolve speaker authorisation. Until then, the Designer should:
- Maintain a stub allowlist of known QFAs / APA holders
- Default to "unqualified" for any unrecognised speaker — fail closed, not open

## Cross-references

- `Researcher/research-call-supervision-audit.md` — the breach pattern this framework constrains
- `Researcher/req-detection-criteria.md` — to be updated with HF-00 (speaker authorisation), HF-10 (cover details), HF-11 (plan comparison) — see that doc for the detection rules
- `compliance-wiki/wiki/concepts/insurance-distribution.md` — IDD/IDR conduct overlay
- Open: `compliance-wiki/wiki/concepts/minimum-competency-code.md` does not yet exist — recommend the Researcher create it as a follow-up

## Open questions for the Designer / Reviewer

1. How is speaker identity captured in the Fireflies feed today — by name only, by email, or with a stable employee ID? The agent's lookup design depends on which is canonical.
2. For mixed-attendance calls (qualified + unqualified speakers), is the agent meant to flag only the unqualified speaker's lines, or the call as a whole when an unqualified speaker is present without a qualified colleague?
3. The Paligo case (Q2-25-F-01) finding said *"member of benefits needs to be present for renewals as this is regulated activity"* — should the agent enforce a positive rule (qualified speaker must be present for any pension/insurance renewal call), and if so, how is "renewal" detected?
4. UK calls under SYSC 28 use a "firm assesses competence" model rather than fixed qualifications. Does the agent treat all UK speakers as authorised by default, or apply Kota's UK competency assessment as a register too?
