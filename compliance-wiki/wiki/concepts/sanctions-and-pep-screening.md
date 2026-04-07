---
title: Sanctions and PEP Screening
type: concept
tags:
  - compliance/sanctions-screening
  - compliance/aml
  - regulation/cbi
  - regulation/fca
created: 2026-04-07
updated: 2026-04-07
source_count: 2
status: active
---

# Sanctions and PEP Screening

## Definition
Sanctions screening verifies that individuals and entities are not on prohibited lists (EU, UK, US OFAC, UN sanctions). PEP (Politically Exposed Person) screening identifies individuals who hold or have held prominent public functions, as they present higher money laundering risk. Both are mandatory components of AML compliance.

## Regulatory Framework
- **EU Sanctions Regulations** — directly applicable, require screening against EU consolidated sanctions list.
- **UK Sanctions and Anti-Money Laundering Act 2018** — UK-specific sanctions regime post-Brexit.
- **Central Bank of Ireland** AML/CFT guidance — requires ongoing sanctions and PEP monitoring for all regulated firms.
- **[[FCA]]** Money Laundering Regulations — parallel UK requirements.

## Key Requirements

### Screening Levels at Kota
Per [[KYB Requirements by Product Type]]:

| Level | Health | Pensions | Income Protection | PEPP |
|-------|--------|----------|-------------------|------|
| Sanctions — Employees | Yes | Yes | Yes | Yes |
| Sanctions — Employers | Yes | Yes | Yes | Yes |
| Sanctions — Directors | Yes | Yes | Yes | Yes |
| Sanctions — UBOs | Yes | Yes | Yes | Yes |
| PEP — Employees | N/A | Yes | Yes | Yes |
| PEP — Directors | N/A | Yes | Yes | Yes |
| PEP — UBOs | N/A | Yes | Yes | Yes |

### Adverse Media
Adverse media screening (financial crime, fraud, money laundering, terrorism financing, regulatory enforcement) is classified as "nice to have" across all products but is best practice and expected by the [[Central Bank of Ireland]].

### Ongoing Monitoring
One-time screening is insufficient. Continuous or periodic re-screening is required for changes in sanctions lists, PEP status, ownership structure, and adverse media.

## Our Approach
[[Kota]] uses [[ComplyAdvantage]] with:
- Fuzzy matching calibrated at **70–85%** range
- Case management via ComplyAdvantage Mesh
- Documented SOP for reviewing and escalating cases

**Pain points:** High false positive rates (363+ cases), test data contamination in production.

## Open Questions / Gaps
- Should adverse media screening be elevated from "nice to have" to mandatory?
- ComplyAdvantage replacement or extension decision pending (see [[Kota KYB Software Requirements]]).

## Sources
- [[Kota KYB Software Requirements]]
- [[KYB Requirements by Product Type]]
