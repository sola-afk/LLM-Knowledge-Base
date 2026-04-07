---
title: Compliance Overview
created: 2026-04-07
updated: 2026-04-07
type: overview
tags:
  - compliance/overview
status: active
---

# Compliance Overview

## Current Priorities

### 1. KYB Vendor Selection — High Priority
[[Kota]] lacks a dedicated KYB provider. The current tool ([[ComplyAdvantage]]) handles sanctions/PEP screening but does not cover full business verification, UBO identification, or registry checks. A comprehensive requirements document has been produced (see [[Kota KYB Software Requirements]]) covering both Platform and Embed verticals.

**Market research completed** — 10 developer-friendly KYB providers have been evaluated (see [[KYB Provider Comparison — Top 10 Developer-Friendly Providers]]). Top recommendations:
1. **[[Sumsub]]** — Best all-round (fast, unified KYC+KYB, webhooks, 200+ countries)
2. **[[Persona]]** — Best developer experience (clean APIs, dynamic flows)
3. **[[ComplyCube]]** — Best pricing transparency (published rates, UK-based)

**UX research also completed** — 10 providers evaluated for user experience and simplistic design (see [[KYB Provider UX Comparison — Top 10 for User Experience & Simplistic Design]]). Top UX picks:
1. **[[Spektr]]** — Best compliance team UX (AI tree view, no-code workflows)
2. **[[Vespia]] / [[Veriff]]** — Best onboarding UX (sub-30s, 300+ jurisdictions, one-click PDF export)
3. **[[Persona]]** — Best combined DX + UX

**Overall leaders across both dimensions:** [[Persona]] and [[Sumsub]] rank highly on developer experience AND user experience.

**Next steps:** Request demos from top providers (Persona, Sumsub, Spektr, ComplyCube), validate EU/EEA registry coverage, request SOC 2 / ISO 27001 evidence.

### 2. PEPP Product Risk Assessment — Medium Priority
The [[KYB Requirements by Product Type]] matrix shows director and UBO identification requirements for PEPP are **unknown**. A product-specific risk assessment must be completed before PEPP onboarding processes can be finalised.

### 3. ComplyAdvantage Pain Points — Medium Priority
[[ComplyAdvantage]] has ongoing issues with high false positive rates and test data contaminating production. These need to be resolved either through better configuration or vendor replacement.

## Key Regulatory Relationships
- **[[Central Bank of Ireland]]** — Primary regulator (Ireland). Drives AML/KYB obligations.
- **[[FCA]]** — UK regulator. Kota operates as appointed representative of Innovative Risk Labs Ltd.

## Compliance Framework
- [[AML Compliance]] — Overarching anti-money laundering programme
- [[KYB (Know Your Business)]] — Corporate customer due diligence
- [[Sanctions and PEP Screening]] — Entity and individual screening
- [[UBO Identification]] — Beneficial ownership verification

## Upcoming Deadlines
*No specific deadlines identified yet. Will be updated as regulatory sources are ingested.*

## Recent Activity
See [[log]] for the full chronological activity log.
