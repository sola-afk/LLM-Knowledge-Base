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

## Kota's "Fitness and Probity/SMCR & MCC Register" (Google Drive)

Kota maintains a detailed MCC/F&P register in Google Drive ("Fitness and Probity/SMCR & MCC Register" spreadsheet) with two main sections:
1. **PCF/CF Register** — Senior management roles (PCF = Pre-approval Controlled Function; CF = Controlled Function)
2. **MCC-regulated customer-facing staff** — Qualifications, script pathway, supervisor, training status

As of the latest register snapshot (May 2026), the call monitoring agent should treat speakers as follows:

### ✅ Fully Qualified MCC Persons (Can conduct regulated activity independently)

| Name | Role | Qualifications | Product Scope |
|------|------|---|---|
| **Trevor Gardiner** | Head of Insurance Distribution (CF7, PCF17) | QFA & APA PGI & RPA | All products (Pensions, Health, Life, General Insurance) |
| **Patrick O'Boyle** | CTO (PCF) | APA Pensions & Insurance & APA PMI | Pensions, Health, Life |
| **Paul O'Hanlon** | Account Executive (CF4) | QFA & APA PMI | Health Insurance (PMI), plus pursuing full QFA |
| **Daniel McAvinue** | Benefits Co-Ordinator (CF4) | APA Pensions & Life; New Entrant for PMI | Pensions, Life (supervised for PMI) |
| **Naoise Baker** | Benefits Co-Ordinator (CF4) | QFA & APA PMI | Health Insurance (PMI) |
| **Colin Pon** | Expansions Lead (CF4) | APA PMI | Health Insurance (PMI) |
| **Charlie Blake** | Benefits Sales Lead (CF4) | APA PMI | Health Insurance (PMI) |
| **Callum Pearse** | Account Executive (CF4) | APA Pensions; New Entrant for PMI | Pensions (independent); Health (supervised) |

### ⚠️ New Entrants (Do NOT meet MCC Standards; must act under immediate direction of qualified supervisor)

| Name | Role | Pursuing | Supervisor | Status |
|------|------|----------|---|---|
| **Matthew Brennan** | GTM Lead (CF4) | QFA (Life, Pensions, Regulations) | Trevor Gardiner | Cannot supervise others; cannot conduct independent regulated activity |

### ❌ Script Pathway (Unqualified; must follow prescribed script under supervision of qualified person)

| Name | Role | Supervisor | Notes |
|------|------|---|---|
| **Henry Godson** | BDR | Trevor Gardiner | Must remain on script; script compliance must be evidenced by call recording |
| **Katie Garry** | BDR | Trevor Gardiner | Must remain on script; script compliance must be evidenced by call recording |
| **Will Robbins** | Growth Lead | Trevor Gardiner | Prescribed script pathway |
| **Simon Ward** | Customer Success | Trevor Gardiner | Prescribed script pathway |
| **Claudia Correa** | Customer Support | Trevor Gardiner | Prescribed script pathway |
| **Karl O'Brien** | Account Executive | Trevor Gardiner | Prescribed script pathway; **unmonitored mobile phone use flagged** |
| **Joana Crisóstomo** | CS Co-ordinator | Trevor Gardiner | Moved roles Sept 2025 |
| **Gabriella Pistol** | (unspecified) | Trevor Gardiner | Resigned Sept 2025 |
| **Grace Lynch** | Benefits Co-ordinator | Trevor Gardiner | Removed from register Dec 2025 |

### ❌ No MCC Registration / Cannot Conduct Regulated Activity

| Name | Role | Reason | Notes |
|------|------|---|---|
| **Kate Fullen** | CF4 | No MCC qualifications recorded | Should NOT be on customer calls regarding insurance/pensions; needs immediate action |
| **Ceri Thomas** | (UK-only role) | No qualifications | Non-Ireland scope; no MCC entry required |
| **Luke Mackey** | CEO | Removed Sept 2024 | Was APA Pensions; now removed from register |

### Key Supervisory Chain
- **Trevor Gardiner** (CF7, Head of Insurance Distribution) is the single MCC supervisor for all script-pathway and new-entrant staff.
- **Concentration risk**: Trevor is sole CF7 for 12+ MCC-regulated staff.
- **Script supervision gap**: BDRs' (Henry Godson, Katie Garry) call recordings are essential to evidence script adherence; without recordings, compliance cannot be documented.

### Compliance Gaps Identified (April 2026 Action Log)
1. **Unmonitored channels**: Karl O'Brien and Colin Pon using personal mobile phones — cannot evidence regulatory compliance
2. **Kate Fullen**: CF4 with no MCC registration — must cease regulated activity or obtain qualification
3. **Call recording**: BDR calls not recorded; script supervision cannot be evidenced
4. **Script review**: All scripts require updated review and approval before deployment

## Implementation for the Agent

The Designer should:

1. **Integrate with the MCC Register** — Import the Kota "Fitness and Probity/SMCR & MCC Register" (Google Drive spreadsheet) as a read-only lookup table. Speaker identity + product discussed → lookup qualifications and product scope.

2. **Build a speaker-authorisation matrix** based on the register snapshot above:
   - ✅ **Fully qualified** — Can discuss any aspect of their product scope (advice, information, arranging)
   - ⚠️ **New Entrant** — Can only discuss within supervision relationship; flag any independent recommendations or statements
   - ❌ **Script pathway** — Must match documented script; any deviation is a breach; requires call recording to evidence compliance
   - ❌ **Unregistered** — Cannot conduct regulated activity; flag all product discussion as out-of-scope
   - ⚠️ **Unmonitored channel** — Mobile phone communication; flag for compliance review

3. **Fail-closed default** — If speaker not found in register, treat as unqualified. If product discussed not listed in speaker's scope, flag as HF-00 breach.

4. **Monitor the register** — The register is updated periodically. Request new snapshots from Compliance quarterly or when new staff onboard/exit.

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
