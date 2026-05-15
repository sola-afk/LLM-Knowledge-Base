---
title: Auto-Enrolment Source-of-Truth — My Future Fund (Ireland)
created: 2026-05-15
type: source-of-truth
source: https://www.gov.ie/en/department-of-social-protection/publications/auto-enrolment-retirement-savings-system-for-employees/
status: PLACEHOLDER — wording to be pasted by Compliance
---

# Auto-Enrolment Source-of-Truth — My Future Fund (Ireland)

This file is the comparison baseline the agent uses to check whether a speaker's auto-enrolment statement is accurate. Any AE claim on a customer-facing call that diverges from the wording here triggers **HF-05** (incorrect public-law statement), regardless of who made it.

## How the agent uses this file

1. When a speaker mentions Irish auto-enrolment / "My Future Fund" / "the government scheme" on a call, the agent extracts the verbatim quote.
2. The agent compares the quote against the facts captured below.
3. If the quote diverges (wrong percentage, wrong eligibility, wrong phasing, wrong opt-out rule), the agent raises **HF-05** with the verbatim transcript quote and the contradicting source-of-truth quote.
4. If the quote matches, no HF-05 (and HF-10 does not apply either, per the AE carve-out in `req-detection-criteria.md`).

## Source

**Primary source**: [Auto-enrolment retirement savings system for employees — gov.ie / Department of Social Protection](https://www.gov.ie/en/department-of-social-protection/publications/auto-enrolment-retirement-savings-system-for-employees/)

**Administering body**: National Automatic Enrolment Retirement Savings Authority (NAERSA)

**Legislation**: Automatic Enrolment Retirement Savings Act 2024

## Approved facts (verbatim wording to be pasted)

> ⚠️ **TO BE COMPLETED BY COMPLIANCE.** Paste the verbatim wording from the gov.ie page into the sections below. The agent will use this exact wording as the comparison baseline. If a section is blank, the agent treats statements on that topic as unverifiable — flag as HF-05 with the note "AE source-of-truth missing".

### 1. Scheme name and administering body
<!-- Paste verbatim gov.ie wording here -->

### 2. Commencement date
<!-- Paste verbatim gov.ie wording here -->

### 3. Eligibility criteria (age, earnings, exclusions, existing-pension carve-outs)
<!-- Paste verbatim gov.ie wording here -->

### 4. Contribution rates and phasing schedule
<!-- Paste verbatim gov.ie wording here. Cover years 1-3, 4-6, 7-9, 10+ with employer/employee/state top-up percentages -->

### 5. Contribution base (gross pay, capped earnings)
<!-- Paste verbatim gov.ie wording here -->

### 6. Opt-out and re-enrolment mechanics
<!-- Paste verbatim gov.ie wording here -->

### 7. Investment options
<!-- Paste verbatim gov.ie wording here -->

### 8. How employees interact with the scheme (enrolment, contribution view, contact)
<!-- Paste verbatim gov.ie wording here -->

## Known-wrong statements observed on Kota calls (training data for the agent)

The agent should flag any of the following statement families on customer calls. Each was observed on a Kota call in May 2026 and was either factually wrong or unverified against the source. Replace these with the correct wording once the gov.ie facts are pasted above.

- "AE has to be 3.5% minimum contribution between the employee and the employer" (Karl O'Brien — Andrew Moore call 2026-05-08, India Healy O Connor 2026-05-08)
- "1.5 employer, 1.5 employee and 0.5 state top" (Simon Ward — LearnUpon #2, 2026-05-15)
- "employees that are under 80k their pension contributions need to be based on their total taxable income" (Simon Ward — LearnUpon #1, 2026-05-12)

These statements may turn out to be correct against the official source — but the agent cannot confirm that until the verbatim gov.ie wording is in this file.

## Update protocol

When the gov.ie wording changes (e.g. percentage phasing kicks in to a new tier, eligibility threshold updates):
1. Compliance re-pastes the relevant section from gov.ie.
2. Update the `last_verified` line below with the date.
3. Commit with a message that captures what changed.

last_verified: ⚠️ NEVER — placeholder file, awaiting Compliance input
