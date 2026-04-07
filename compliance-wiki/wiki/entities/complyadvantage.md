---
title: ComplyAdvantage
type: entity
tags:
  - entity/vendor
  - compliance/sanctions-screening
  - compliance/aml
  - process/due-diligence
created: 2026-04-07
updated: 2026-04-07
status: active
---

# ComplyAdvantage

## Overview
ComplyAdvantage is [[Kota]]'s current vendor for sanctions and PEP screening. Kota uses the ComplyAdvantage Mesh interface for case management and screening workflows.

## Current Usage
- **Sanctions screening** of new customers and employees before onboarding.
- **PEP screening** with configurable fuzzy matching (calibrated at 70–85%).
- **Case management** via ComplyAdvantage Mesh — review, escalate, close cases with audit trail.
- Documented SOP (Scribe) for reviewing and escalating customer cases.

## Known Pain Points
- **High false positive rates** — 363+ cases in the queue at one point, creating significant manual review burden.
- **Test data contamination** — Excess screenings from non-customers and test entities contaminated the production environment, making it difficult to distinguish real from test data.
- **Limited KYB capability** — ComplyAdvantage handles individual-level screening but does not provide full company-level KYB (business verification, UBO identification, registry checks).

## Evaluation Status
Kota is evaluating whether to:
1. Extend ComplyAdvantage with a complementary KYB provider, or
2. Replace ComplyAdvantage entirely with a provider offering both KYB and screening.

See [[Kota KYB Software Requirements]] for the full evaluation criteria.

## Sources
- [[Kota KYB Software Requirements]]
