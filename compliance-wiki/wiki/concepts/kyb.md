---
title: KYB (Know Your Business)
type: concept
tags:
  - compliance/kyb
  - compliance/aml
  - regulation/cbi
  - regulation/fca
created: 2026-04-07
updated: 2026-04-07
source_count: 3
status: active
---

# KYB (Know Your Business)

## Definition
Know Your Business (KYB) is the process of verifying the identity, ownership, and legitimacy of a corporate entity before establishing a business relationship. It is a core component of Anti-Money Laundering (AML) compliance, required under EU Anti-Money Laundering Directives and enforced by the [[Central Bank of Ireland]] and [[FCA]].

KYB extends beyond individual-level KYC (Know Your Customer) to cover the legal entity itself — its registration, beneficial ownership structure, directors, and financial standing.

## Regulatory Framework
- **EU Anti-Money Laundering Directives** (AMLD4, AMLD5, AMLD6) — set the framework for customer due diligence including business verification.
- **Central Bank of Ireland** AML/CFT framework — requires regulated firms to identify and verify corporate customers, their UBOs, and directors.
- **FCA Money Laundering Regulations** (UK MLRs) — parallel requirements for UK operations.
- **Criminal Justice (Money Laundering and Terrorist Financing) Act 2010** (Ireland) — domestic legislation transposing EU AML directives.

## Key Requirements
1. **Company identity verification** — Legal name, registration number, address, incorporation date, jurisdiction.
2. **[[UBO Identification]]** — Identify individuals with 25%+ ownership or control.
3. **Director identification** — Names and, where required, identity verification of at least 2 directors.
4. **[[Sanctions and PEP Screening]]** — Screen entity, UBOs, and directors against sanctions lists and PEP databases.
5. **Source of funds / source of wealth** — Required for higher-risk products (Pensions, Income Protection, PEPP).
6. **Ongoing monitoring** — Continuous or periodic re-screening throughout the relationship.
7. **Record-keeping** — Full audit trail of all checks and decisions.

## Our Approach
[[Kota]] currently uses [[ComplyAdvantage]] for sanctions/PEP screening but lacks a dedicated KYB solution. Requirements vary by product type:

| Product | KYB Depth |
|---------|-----------|
| Health | Light (basic company verification, sanctions only) |
| Pensions | Mid (full screening, risk-based director/UBO ID) |
| Income Protection | Full (all checks mandatory) |
| PEPP | Full (TBC — risk assessment pending) |

See [[KYB Requirements by Product Type]] for the detailed matrix.

A vendor evaluation is underway — see [[Kota KYB Software Requirements]] for full criteria.

## Open Questions / Gaps
- **PEPP risk assessment outstanding** — Director and UBO identification requirements are unknown for PEPP.
- **KYB vendor selection pending** — No dedicated provider in place.
- **ComplyAdvantage limitations** — Current tool does not cover full KYB; decision needed on extend vs. replace.

## Sources
- [[Kota KYB Software Requirements]]
- [[KYB Requirements by Product Type]]
- [[Case Creation Workflow Notes]]
