---
title: "KYB Requirements by Product Type"
type: source
tags:
  - compliance/kyb
  - compliance/aml
  - compliance/sanctions-screening
  - process/due-diligence
created: 2026-04-07
updated: 2026-04-07
source_file: raw/kyb-requirements-by-product.md
status: active
---

# KYB Requirements by Product Type

## Key Takeaways
- Sanctions and PEP screening requirements vary by product type — **Health** products have lighter PEP requirements than **Pensions**, **Income Protection**, and **PEPP**.
- All product types require sanctions screening at every level: employees, employers, directors, and UBOs.
- Full KYB (company verification, UBO identification, director ID) is **required** for Pensions, Income Protection, and PEPP but **lighter** for Health.
- Source of Wealth and UBO/director identification are **risk-based** for Pensions but **mandatory** for Income Protection and PEPP.
- PEPP product requirements are partially **unknown** — a risk assessment is still needed.

## Detailed Summary

### Sanctions & PEP Screening Matrix

| Check | Health | Pensions | Income Protection | PEPP |
|-------|--------|----------|-------------------|------|
| Sanctions — Employees | Yes | Yes | Yes | Yes |
| Sanctions — Employers | Yes | Yes | Yes | Yes |
| Sanctions — Directors | Yes | Yes | Yes | Yes |
| Sanctions — UBOs | Yes | Yes | Yes | Yes |
| PEP — Employees | N/A | Yes | Yes | Yes |
| PEP — Directors | N/A | Yes | Yes | Yes |
| PEP — UBOs | N/A | Yes | Yes | Yes |

**Key observation:** Health products are exempt from PEP screening on employees, directors, and UBOs. All other products require full PEP screening.

### Customer Due Diligence (KYB) Matrix

| Requirement | Health | Pensions | Income Protection | PEPP |
|-------------|--------|----------|-------------------|------|
| Company Legal Name | Required | Required | Required | Required |
| Proof of Incorporation | Required | Required | Required | Required |
| Country of Incorporation | Required | Required | Required | Required |
| Registration Number | Required | Required | Required | Required |
| Date of Incorporation | Required | Required | Required | Required |
| Directors Names (min 2) | Nice to have | Required | Required | Required |
| UBOs | N/A | Required | Required | Required |
| Director ID (ID/VA) | N/A | High risk only | Required | Unknown |
| UBO ID over 25% (ID/VA) | N/A | High risk only | Required | Unknown |
| Source of Funds | N/A | Required (automatic via DD) | Required (automatic via DD) | Required (automatic via DD) |
| Source of Wealth | N/A | High risk only | Required | Required |
| Business Category | Nice to have | Nice to have | Nice to have | Nice to have |
| Adverse Media | Nice to have | Nice to have | Nice to have | Nice to have |
| Geographical Reach | Nice to have | Nice to have | Nice to have | Nice to have |
| Financial Status Check | Nice to have | Nice to have | Nice to have | Nice to have |

### Risk-Based Approach
- **Health**: Lightest requirements — basic company verification, sanctions only, no PEP/UBO obligations.
- **Pensions (Group)**: Mid-tier — full screening required, but director/UBO identification only for high-risk cases (PEP etc.).
- **Income Protection (Group)**: Full requirements — all identification, screening, and source of wealth checks mandatory.
- **PEPP**: Requirements largely mirror Income Protection, but **director ID and UBO ID thresholds are unknown** — a product-specific risk assessment is needed.

## Impact Assessment

> [!warning] Action Required
> **PEPP product risk assessment** is outstanding. Director and UBO identification requirements are marked as "Unknown" and need to be determined before PEPP onboarding processes can be finalised.

**Risk rating:** **Medium** — the matrix is well-defined for Health, Pensions, and Income Protection, but PEPP gaps must be closed.

**Action items:**
1. Complete PEPP product risk assessment to determine director/UBO ID requirements.
2. Ensure the KYB software provider (see [[Kota KYB Software Requirements]]) can support product-specific rule configurations.
3. Validate that current onboarding flows enforce these requirements per product type.

## Cross-References
- Source: [[Kota KYB Software Requirements]]
- Concept: [[KYB (Know Your Business)]]
- Concept: [[Sanctions and PEP Screening]]
- Concept: [[UBO Identification]]
- Entity: [[Kota]]

## Raw Source
`raw/kyb-requirements-by-product.md`
