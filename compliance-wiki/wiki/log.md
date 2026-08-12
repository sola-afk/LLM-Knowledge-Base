---
title: Activity Log
created: 2026-04-07
updated: 2026-04-07
type: overview
tags:
  - compliance/log
status: active
---

# Activity Log

## [2026-04-07] setup | Initial knowledge base creation
- Created: CLAUDE.md schema file
- Created: wiki/index.md, wiki/log.md, wiki/overview.md
- Created: Directory structure (raw/, wiki/entities/, wiki/concepts/, wiki/sources/, wiki/comparisons/, output/)
- Notes: Knowledge base initialised. Ready for source ingestion.

## [2026-04-07] ingest | Kota KYB Software Requirements
- Source: raw/kota-kyb-software-requirements.md (renamed from "Untitled document.md")
- Created: wiki/sources/kota-kyb-software-requirements.md
- Created: wiki/entities/kota.md, wiki/entities/central-bank-of-ireland.md, wiki/entities/fca.md, wiki/entities/complyadvantage.md
- Created: wiki/concepts/kyb.md, wiki/concepts/sanctions-and-pep-screening.md, wiki/concepts/ubo-identification.md, wiki/concepts/aml-compliance.md
- Updated: wiki/index.md, wiki/overview.md
- Notes: Comprehensive KYB vendor requirements for Kota's Platform and Embed verticals. Key gap identified: no dedicated KYB provider. ComplyAdvantage pain points documented.

## [2026-04-07] ingest | KYB Requirements by Product Type
- Source: raw/kyb-requirements-by-product.md (renamed from "KYB Requirements.md")
- Created: wiki/sources/kyb-requirements-by-product.md
- Updated: All concept and entity pages with product-specific matrix data
- Notes: Due diligence requirements vary significantly by product. PEPP risk assessment outstanding — director/UBO ID requirements unknown.

## [2026-04-07] ingest | Case Creation Workflow Notes
- Source: raw/case-creation-workflow-notes.md (renamed from "Conditions are mainly for case creation.md")
- Created: wiki/sources/case-creation-workflow-notes.md
- Notes: Brief internal notes on conditional logic for case creation workflows. Low priority — useful context for KYB platform configuration.

## [2026-04-07] research | KYB Provider Market Research — Top 10 Developer-Friendly Providers
- Source: Web research across multiple industry comparison guides and provider websites
- Created: wiki/sources/kyb-provider-research-2026-04.md
- Created: wiki/comparisons/kyb-provider-comparison.md
- Created: wiki/entities/sumsub.md, wiki/entities/signzy.md, wiki/entities/complycube.md, wiki/entities/ondato.md, wiki/entities/veriff.md, wiki/entities/idenfy.md, wiki/entities/aiprise.md, wiki/entities/persona.md, wiki/entities/alloy.md, wiki/entities/onfido.md
- Updated: wiki/index.md, wiki/overview.md
- Notes: Evaluated 10 KYB providers against Kota's requirements. Top 3 recommendations: Sumsub (best all-round), Persona (best DX), ComplyCube (best pricing transparency). Next steps: request demos, validate EU coverage, request security certifications.

## [2026-04-07] research | KYB Provider UX Research — Top 10 for User Experience & Simplistic Design
- Source: Web research across provider websites and industry guides
- Created: wiki/sources/kyb-provider-ux-research-2026-04.md
- Created: wiki/comparisons/kyb-provider-ux-comparison.md
- Created: wiki/entities/vespia.md, wiki/entities/spektr.md, wiki/entities/strise.md, wiki/entities/checkin-com.md, wiki/entities/shufti-pro.md, wiki/entities/compliancely.md, wiki/entities/middesk.md
- Updated: wiki/index.md, wiki/overview.md
- Notes: Evaluated 10 KYB providers on UX and design simplicity. Top 3 UX picks: Spektr (best compliance team UX), Vespia/Veriff (best onboarding UX), Persona (best combined DX+UX). Persona and Sumsub rank highly across both developer and UX dimensions.

## [2026-04-07] deliverable | KYB Provider Product Requirements Document
- Created: output/kyb-provider-product-requirements.md
- Notes: Formal PRD synthesising all knowledge base sources — functional requirements (40 items), technical requirements (20 items), security requirements (12 items), UX requirements (7 items), vendor requirements (8 items). Includes evaluation scorecard, shortlisted providers, decision framework (replace vs extend ComplyAdvantage), and 16-week implementation timeline.

## [2026-04-08] ingest | Q1 2026 Compliance Review — Embed Hubs
- Source: raw/Q1 2026 Compliance Review- Embed hubs.docx (converted to raw/q1-2026-compliance-review-embed-hubs.md)
- Notes: Terms of Reference for compliance audit of Embed Hubs — customer-facing information portals on kota.io subdomains. Scope: consumer protection, insurance distribution, data protection. Built on Lovable by Josh Ellwood.

## [2026-04-08] deliverable | Embed Hub Sampling Review Template
- Created: output/embed-hub-sampling-review-template.md
- Notes: 30-item checklist across 7 categories (clear presentation, product information, disclosures, IPIDs, data protection, consistency, governance) with regulatory references down to section/subsection level. Covers CBI Consumer Protection Code 2025, S.I. No. 229/2018, IDD, FCA Consumer Duty (PRIN 2A), ICOBS, GDPR.

## [2026-04-08] wiki | Product Governance and Insurance Distribution concept pages
- Created: wiki/concepts/product-governance.md
- Created: wiki/concepts/insurance-distribution.md
- Updated: wiki/index.md
- Notes: Product governance covers IDR Reg.38 manufacturer and distributor obligations, IDD Art.25, CPC 2025 Standards for Business, FCA PRIN 2A.3. Insurance distribution covers disclosures (Reg.23), pre-contractual info (Reg.26), IPIDs (Reg.27), CPC 2025 Parts 3–4, ICOBS, and FCA Consumer Duty.

## [2026-04-08] ingest | Product governance framework articles (4 sources)
- Sources: Skyjed, ESMA/A&L Goodbody, Ruleguard, KPMG Ireland (all adapted from MiFID II to insurance distribution)
- Created: raw/product-governance-framework-skyjed.md, raw/product-governance-target-market-esma-alg.md, raw/product-governance-quality-assessment-ruleguard.md, raw/product-governance-manufacturer-distributor-kpmg.md
- Created: wiki/sources/ pages for all 4
- Updated: wiki/concepts/product-governance.md — added lifecycle phases, five target market categories, feedback loop, self-assessment checklist, expanded open questions
- Updated: wiki/index.md

## [2026-04-08] research | EU product governance regulatory framework
- Sources: Delegated Regulation (EU) 2017/2358 (EUR-Lex), EIOPA POG Peer Review 2023, EU Retail Investment Strategy (Dec 2025)
- Created: raw/eu-delegated-regulation-2017-2358-pog.md, raw/eiopa-pog-peer-review-2023.md, raw/eu-retail-investment-strategy-pog-2025.md
- Created: wiki/sources/ pages for all 3
- Updated: wiki/concepts/product-governance.md — added Delegated Regulation 2017/2358 articles (product approval, target market, testing, monitoring, corrective action), EIOPA peer review findings, upcoming Retail Investment Strategy (value-for-money, undue costs)
- Updated: wiki/index.md
- Notes: Delegated Reg. 2017/2358 is the foundational EU regulation — Articles 4-8 (manufacturers) and 10 (distributors). EIOPA peer review found target markets too broad, product testing inconsistent, distributor feedback loops weak. RIS introduces value-for-money assessments (~2028).

## [2026-04-08] research | CPC 2025 quote data retention and deletion
- Source: S.I. 81/2025, DPC guidance, Insurance Ireland guidance, industry briefings
- Created: raw/cpc-2025-quote-data-retention.md
- Created: wiki/sources/cpc-2025-quote-data-retention.md
- Created: wiki/concepts/data-retention.md
- Updated: wiki/index.md
- Notes: CPC 2025 sets 12-month retention for non-customer records (quote-only) — reduced from 6 years. 6 years retained for active customers. 12 months is consent-based. GDPR Art.5(1)(e) overlay — DPC suggests ~21-day cooling-off for abandoned quotes. Effective 24 March 2026.

## [2026-08-12] monitoring | Embed Call Monitoring review — Q2 2026
- Source: Google Drive "Monitoring and Testing / Embed Call Monitoring" (5 recordings, June 2026)
- Created: output/embed-call-monitoring-2026-q2.md
- Reviewed: 1 of 5 calls (Kota X Smart, Pilot Cohort & Success Criteria, 10/06/2026) — overall PC, 6 findings
- Not reviewed: 4 of 5 — audio-only mp3s, no transcript available to Compliance and files above the 10 MB retrieval limit
- Notes: Findings are pre-contractual design gaps — no consent to record (3rd consecutive quarter), volume-linked rev share with no conflicts assessment, target market not applied to cohort design, data-sharing scope widened on second-hand privacy clearance, partner's perimeter status undetermined, success criteria carry no customer-outcome measure. Programme-level gap G1: Compliance cannot reach 80% of the Embed call population. Register rows drafted for Call Monitoring 2026 — cannot be written to the Sheet from here.
