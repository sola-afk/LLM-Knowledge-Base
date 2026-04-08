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
