# Product Requirements Document: KYB Provider Selection

**Document owner:** Compliance Team, Kota  
**Date:** 7 April 2026  
**Status:** Draft  
**Classification:** Internal — Confidential

---

## 1. Executive Summary

Kota is a CBI-regulated insurance intermediary operating two product verticals — **Platform** (direct employer onboarding) and **Embed** (API-driven onboarding via partner platforms). Kota currently uses ComplyAdvantage for sanctions and PEP screening but has no dedicated Know Your Business (KYB) provider for corporate customer due diligence.

This document defines the product requirements for selecting a KYB provider that will:
- Close the KYB gap in Kota's AML compliance programme
- Support four product types with different due diligence depths (Health, Pensions, Income Protection, PEPP)
- Integrate seamlessly into both Platform and Embed onboarding flows
- Replace or complement ComplyAdvantage for sanctions/PEP screening
- Satisfy the record-keeping and audit requirements of the Central Bank of Ireland and FCA

---

## 2. Background & Problem Statement

### Current State
| Capability | Status | Tool |
|-----------|--------|------|
| Sanctions screening (individuals) | Active | ComplyAdvantage |
| PEP screening (individuals) | Active | ComplyAdvantage (70–85% fuzzy matching) |
| Case management | Active | ComplyAdvantage Mesh |
| Company identity verification | **Gap** | None |
| UBO identification & verification | **Gap** | None |
| Director identification & verification | **Gap** | None |
| Company-level sanctions screening | **Gap** | None |
| Ongoing entity monitoring | **Gap** | None |
| Risk-based tiering by product | **Gap** | None |

### Pain Points with ComplyAdvantage
1. **High false positive rates** — 363+ cases in the review queue at one point, creating unsustainable manual review burden.
2. **Test data contamination** — Test screenings and non-customer entities polluting the production environment.
3. **No KYB capability** — ComplyAdvantage handles individual-level screening only; no company verification, UBO identification, or registry checks.

### Regulatory Drivers
- **EU Anti-Money Laundering Directives** (AMLD4, AMLD5, AMLD6)
- **Criminal Justice (Money Laundering and Terrorist Financing) Act 2010** (Ireland)
- **Central Bank of Ireland** AML/CFT framework
- **FCA Money Laundering Regulations** (UK)

---

## 3. Product Verticals & Integration Points

### 3.1 Platform (Self-Serve Employer Onboarding)

Employers sign up directly through Kota's platform for group insurance products.

**Integration requirements:**
- KYB checks must complete at or before the point where the employer can access insurance products
- Self-serve flow — minimal friction for the employer
- Dashboard for compliance team to review flagged cases
- Employee-level KYC must be handled (by the KYB provider or via integration with existing tooling)

### 3.2 Embed (Partner API Integration)

Partner platforms (Remote, Employment Hero, Helios, Globalli) create employers via Kota's API or UI components.

**Integration requirements:**
- **API-first architecture** — non-negotiable
- **Webhook/event-driven notifications** for status changes and case updates
- **White-label/invisible integration** — no provider branding visible to partner end users
- **Bulk onboarding** — handle high-volume partner flows efficiently
- **Multi-entity handling** — KYB at both partner level and employer level

---

## 4. Functional Requirements

### 4.1 Company Identity Verification

| ID | Requirement | Priority | Notes |
|----|------------|----------|-------|
| F-01 | Verify company legal name against official registries | **Must** | All products |
| F-02 | Verify proof of incorporation / registration | **Must** | All products |
| F-03 | Verify country of incorporation | **Must** | All products |
| F-04 | Verify company registration number | **Must** | All products |
| F-05 | Verify date of incorporation | **Must** | All products |
| F-06 | Identify business category / type | **Should** | Nice to have across all products |
| F-07 | Check financial status of employer | **Should** | Nice to have across all products |
| F-08 | Determine geographical reach (group structure) | **Should** | Nice to have across all products |

### 4.2 UBO & Director Identification

| ID | Requirement | Priority | Notes |
|----|------------|----------|-------|
| F-09 | Identify UBOs with 25%+ ownership or control | **Must** | Required for Pensions, Income Protection, PEPP |
| F-10 | Handle complex ownership structures (holding companies, trusts, multi-layered chains) | **Must** | |
| F-11 | Identify minimum 2 directors by name | **Must** | Required for Pensions, Income Protection, PEPP; nice to have for Health |
| F-12 | Verify director identity (ID and address) | **Must** | Required for Income Protection; high-risk only for Pensions; TBC for PEPP |
| F-13 | Verify UBO identity for 25%+ owners (ID and address) | **Must** | Required for Income Protection; high-risk only for Pensions; TBC for PEPP |
| F-14 | Visual display of ownership structures (tree view) | **Should** | Reduces analyst review time |

### 4.3 Sanctions, PEP & Adverse Media Screening

| ID | Requirement | Priority | Notes |
|----|------------|----------|-------|
| F-15 | Screen employer entity against sanctions lists (EU, UK, US OFAC, UN) | **Must** | All products |
| F-16 | Screen employer directors against sanctions lists | **Must** | All products |
| F-17 | Screen UBOs against sanctions lists | **Must** | All products |
| F-18 | Screen employees against sanctions lists | **Must** | All products (may use existing ComplyAdvantage) |
| F-19 | PEP screening — directors | **Must** | Required for Pensions, Income Protection, PEPP |
| F-20 | PEP screening — UBOs | **Must** | Required for Pensions, Income Protection, PEPP |
| F-21 | PEP screening — employees | **Must** | Required for Pensions, Income Protection, PEPP |
| F-22 | Adverse media screening (entity, UBOs, directors) | **Should** | Currently "nice to have" but best practice |
| F-23 | Configurable fuzzy matching thresholds (target: 70–85% range) | **Must** | Critical for managing false positive rates |
| F-24 | Ongoing / continuous monitoring (sanctions, PEP, ownership changes, adverse media) | **Must** | Regulatory requirement |

### 4.4 Risk Assessment & Scoring

| ID | Requirement | Priority | Notes |
|----|------------|----------|-------|
| F-25 | Configurable risk scoring (jurisdiction, industry, ownership complexity, screening results) | **Must** | |
| F-26 | Risk-based tiering: standard, enhanced, simplified due diligence | **Must** | Must map to product tiers (Health/Pensions/IP/PEPP) |
| F-27 | Automated approval for low-risk entities where all checks pass | **Must** | Key to reducing manual review burden |
| F-28 | Dynamic verification flows that adapt by product type, jurisdiction, and risk level | **Should** | Different depths for Health vs Income Protection |
| F-29 | Source of Funds capture | **Must** | Required for Pensions, Income Protection, PEPP (automatic via DD) |
| F-30 | Source of Wealth assessment | **Must** | Required for Income Protection, PEPP; high-risk only for Pensions |

### 4.5 Case Management & Workflow

| ID | Requirement | Priority | Notes |
|----|------------|----------|-------|
| F-31 | Case management interface (review, annotate, escalate, close) | **Must** | Comparable to ComplyAdvantage Mesh |
| F-32 | Configurable alert thresholds to reduce false positives | **Must** | Major pain point to solve |
| F-33 | Bulk case processing for clear-cut cases | **Must** | Auto-resolve obvious mismatches |
| F-34 | Escalation workflows for ambiguous cases | **Must** | |
| F-35 | Full audit trail of every screening, decision, escalation, and closure | **Must** | CBI and FCA record-keeping requirements |
| F-36 | Analyst notes and decision documentation per case | **Must** | |

### 4.6 Reporting & Regulatory Support

| ID | Requirement | Priority | Notes |
|----|------------|----------|-------|
| F-37 | Regulatory reporting outputs (SARs, periodic screening summaries) | **Must** | |
| F-38 | Management dashboards (screening volumes, resolution times, false positive rates, risk distribution) | **Must** | Demonstrate effective oversight to CBI/FCA |
| F-39 | One-click case export for regulatory requests (PDF or structured format) | **Should** | Vespia offers this — strong UX pattern |
| F-40 | Transaction monitoring integration | **Should** | Kota's TM procedures are finalised |

---

## 5. Product-Specific Due Diligence Matrix

The selected provider **must** support configurable verification depths per product type:

| Requirement | Health | Pensions (Group) | Income Protection (Group) | PEPP |
|-------------|--------|-------------------|---------------------------|------|
| Company verification (F-01 to F-05) | Required | Required | Required | Required |
| Director names (F-11) | Nice to have | Required | Required | Required |
| UBO identification (F-09) | N/A | Required | Required | Required |
| Director identity verification (F-12) | N/A | High risk only | Required | TBC |
| UBO identity verification (F-13) | N/A | High risk only | Required | TBC |
| Sanctions — all levels (F-15 to F-18) | Required | Required | Required | Required |
| PEP screening (F-19 to F-21) | N/A | Required | Required | Required |
| Source of Funds (F-29) | N/A | Required (auto) | Required (auto) | Required (auto) |
| Source of Wealth (F-30) | N/A | High risk only | Required | Required |
| Adverse media (F-22) | Nice to have | Nice to have | Nice to have | Nice to have |

> **Note:** PEPP director and UBO identity verification requirements are pending a product risk assessment. The provider must be configurable enough to accommodate the outcome.

---

## 6. Technical Requirements

### 6.1 API & Integration

| ID | Requirement | Priority | Notes |
|----|------------|----------|-------|
| T-01 | RESTful API with comprehensive documentation | **Must** | Non-negotiable for Embed |
| T-02 | Webhook/event-driven notifications | **Must** | Push events for status changes, case updates, risk changes |
| T-03 | SDKs (Web, iOS, Android) | **Should** | For Platform onboarding flows |
| T-04 | White-label / brandless integration | **Must** | Embed partners must not see KYB provider branding |
| T-05 | Bulk / batch processing API | **Must** | Embed partners bring high volumes |
| T-06 | Multi-entity hierarchy support (partner → employer) | **Must** | KYB at both partner and employer level |
| T-07 | Sandbox / test environment with strict separation from production | **Must** | Major ComplyAdvantage pain point |
| T-08 | No-code workflow builder for compliance team | **Should** | Reduces engineering dependency |
| T-09 | Integration time under 4 weeks | **Should** | Based on market benchmarks |

### 6.2 Jurisdictional Coverage

| ID | Requirement | Priority | Notes |
|----|------------|----------|-------|
| T-10 | Company registry access: Ireland | **Must** | Primary market |
| T-11 | Company registry access: United Kingdom | **Must** | UK operations via FCA |
| T-12 | Company registry access: Germany | **Must** | Active market |
| T-13 | Company registry access: Spain | **Must** | Active market |
| T-14 | Company registry access: Netherlands | **Must** | Active market |
| T-15 | Company registry access: France | **Must** | Active market |
| T-16 | Company registry access: broader EU/EEA | **Must** | All current and planned markets |
| T-17 | Country-specific UBO thresholds and PEP definitions | **Must** | Cannot be one-size-fits-all |

### 6.3 Performance

| ID | Requirement | Priority | Notes |
|----|------------|----------|-------|
| T-18 | Verification response time < 30 seconds for standard checks | **Should** | Market leaders achieve 15–30s |
| T-19 | 99.9% API uptime SLA | **Must** | |
| T-20 | Throughput to handle bulk onboarding (1,000+ entities/day) | **Must** | Embed partner volumes |

---

## 7. Data, Privacy & Security Requirements

| ID | Requirement | Priority | Notes |
|----|------------|----------|-------|
| S-01 | Full Regulation (EU) 2016/679 (GDPR) compliance | **Must** | |
| S-02 | UK GDPR / Data Protection Act 2018 compliance | **Must** | |
| S-03 | EU data residency (data stored within EU) | **Should** | Simplifies data transfer obligations |
| S-04 | Data minimisation — collect only what's necessary for KYB | **Must** | |
| S-05 | Published and maintained sub-processor list | **Must** | Kota performs vendor due diligence on sub-processors |
| S-06 | Data Processing Agreement (DPA) available | **Must** | |
| S-07 | SOC 2 Type II certification | **Must** | At least one of SOC 2 or ISO 27001 |
| S-08 | ISO 27001 certification | **Should** | Preferred alongside SOC 2 |
| S-09 | Regular penetration testing (annual minimum) with reports available | **Must** | |
| S-10 | Encryption at rest and in transit | **Must** | |
| S-11 | Role-based access controls (RBAC) with MFA | **Must** | For case management interface |
| S-12 | Vulnerability management programme | **Must** | |

---

## 8. User Experience Requirements

| ID | Requirement | Priority | Notes |
|----|------------|----------|-------|
| U-01 | Clean, intuitive dashboard for compliance analysts | **Must** | Low learning curve |
| U-02 | Visual UBO / ownership structure display | **Should** | AI-assisted tree view preferred (Spektr, Vespia pattern) |
| U-03 | Minimal-input employer onboarding (auto-populate from registries) | **Should** | Reduces friction, improves conversion |
| U-04 | Exceptions-only workflow (auto-approve clear cases, surface only flagged) | **Must** | Solves false positive review burden |
| U-05 | Conditional / adaptive forms based on product type and risk | **Should** | Different depths for Health vs Income Protection |
| U-06 | One-click regulatory export (full case log as PDF) | **Should** | For CBI/FCA requests |
| U-07 | Mobile-responsive interface for compliance team | **Should** | |

---

## 9. Vendor & Commercial Requirements

| ID | Requirement | Priority | Notes |
|----|------------|----------|-------|
| V-01 | Transparent pricing model (per-verification or tiered) | **Should** | Opaque pricing is a risk |
| V-02 | Free trial or sandbox for evaluation | **Should** | Test before committing |
| V-03 | Dedicated account manager | **Must** | Not just self-serve support |
| V-04 | SLA with defined response times for support tickets | **Must** | |
| V-05 | Proven track record with regulated financial services firms | **Must** | Preferably EU/UK regulated |
| V-06 | Clear product roadmap and investment trajectory | **Should** | Avoid platforms at risk of sunsetting |
| V-07 | Ability to replace ComplyAdvantage entirely (unified KYB+KYC+AML) | **Should** | Simplifies vendor management |
| V-08 | Alternatively: clean integration with ComplyAdvantage if retained | **Should** | If extend strategy chosen |

---

## 10. Evaluation Scorecard

Use this scorecard to rate each shortlisted provider. Score each criterion 1–5 (1 = does not meet, 5 = exceeds requirements). Weight reflects importance to Kota.

| Category | Weight | Criteria | Score (1–5) | Weighted |
|----------|--------|----------|-------------|----------|
| **Core KYB** | 20% | Company verification, UBO/director identification, registry coverage (F-01 to F-14) | | |
| **Screening** | 15% | Sanctions, PEP, adverse media, ongoing monitoring, false positive management (F-15 to F-24) | | |
| **Risk & Tiering** | 10% | Configurable risk scoring, product-specific flows, auto-approvals (F-25 to F-30) | | |
| **Case Management** | 10% | Case workflow, audit trail, bulk processing, reporting (F-31 to F-40) | | |
| **API & Integration** | 15% | API quality, webhooks, white-label, bulk processing, sandbox (T-01 to T-09) | | |
| **Coverage** | 10% | EU/EEA + UK registry coverage, country-specific rules (T-10 to T-17) | | |
| **Security & Privacy** | 10% | GDPR, certifications, encryption, pen testing (S-01 to S-12) | | |
| **User Experience** | 5% | Dashboard, UBO visualisation, minimal input, exceptions workflow (U-01 to U-07) | | |
| **Commercial** | 5% | Pricing, support, track record, roadmap (V-01 to V-08) | | |
| **Total** | 100% | | | **/5.00** |

---

## 11. Shortlisted Providers

Based on market research (April 2026), the following providers are recommended for formal evaluation:

### Tier 1 — Request Demo & Pricing
| Provider | Strengths | Concerns |
|----------|-----------|----------|
| **Sumsub** | Best all-round: 15s verification, unified KYC+KYB, webhooks, workflow builder, 200+ countries. Could fully replace ComplyAdvantage. | Pricing not published. Validate specific EU/EEA registry depth. |
| **Persona** | Best developer experience + UX: clean APIs, dynamic flows by region/product, unified KYB+KYC. Ideal for Embed. | 150 registries (fewer than competitors). Pricing not published. |
| **ComplyCube** | Best pricing transparency: $0.05–$0.80/check, developer-first, UK-based, no-code builder. | Validate white-label and bulk processing capabilities. |

### Tier 2 — Evaluate if Tier 1 Falls Short
| Provider | Strengths | Concerns |
|----------|-----------|----------|
| **Spektr** | Best compliance team UX: AI tree view, no-code workflows, integrated case management. | Only 31 registries currently — verify EU/EEA coverage. |
| **Signzy** | Most modular: 340+ APIs, white-label, 1M calls/hr throughput. | Per-call billing (incl. 404s). Enterprise pricing only. |
| **iDenfy** | 99.8% accuracy claim, no-code rule builder, tiered pricing. | Validate accuracy claims independently. |
| **Vespia / Veriff** | 300+ jurisdictions, sub-30s, one-click PDF export. Veriff acquisition = unified KYB+KYC+IDV. | Post-acquisition integration in progress (mid-2026). |

---

## 12. Decision Framework

### Key Decision: Replace or Extend ComplyAdvantage?

| Option | Pros | Cons |
|--------|------|------|
| **Replace** — single vendor for KYB + KYC + AML | Simpler vendor management, unified data, single case management interface, eliminates ComplyAdvantage pain points | Migration risk, potential feature gaps, retraining compliance team |
| **Extend** — add KYB provider alongside ComplyAdvantage | Lower migration risk, retain working sanctions screening, incremental improvement | Two vendor relationships, potential data silos, ongoing ComplyAdvantage pain points |

**Recommendation:** Evaluate Tier 1 providers for **replace** capability first. If none can fully replace ComplyAdvantage, fall back to **extend** strategy with clean integration requirements.

---

## 13. Evaluation Process & Timeline

| Step | Action | Owner | Target |
|------|--------|-------|--------|
| 1 | Share PRD with Tier 1 providers and request proposals | Compliance + Engineering | Week 1 |
| 2 | Receive demos and pricing from Tier 1 | Compliance | Week 2–3 |
| 3 | Complete evaluation scorecard for each provider | Compliance + Engineering | Week 3–4 |
| 4 | Validate EU/EEA registry coverage (IE, UK, DE, ES, NL, FR) | Compliance | Week 3 |
| 5 | Request and review SOC 2 / ISO 27001 / pen test reports | Compliance | Week 3 |
| 6 | GDPR review: DPA, sub-processors, data residency | Legal / DPO | Week 4 |
| 7 | Sandbox / POC with top 1–2 providers | Engineering | Week 5–6 |
| 8 | Final selection and contract negotiation | Compliance + Legal | Week 7–8 |
| 9 | Implementation and integration | Engineering | Week 9–12 |
| 10 | Parallel run with ComplyAdvantage (if replacing) | Compliance | Week 11–14 |
| 11 | Go-live | All | Week 14–16 |

---

## 14. Success Criteria

The selected KYB provider will be considered successful if, within 90 days of go-live:

1. **False positive rate** is measurably lower than ComplyAdvantage baseline
2. **All four product types** (Health, Pensions, Income Protection, PEPP) are onboarded with correct due diligence depths
3. **Embed partners** can trigger KYB checks via API without manual intervention
4. **Platform employers** experience no increase in onboarding drop-off
5. **Compliance team** can manage cases, generate audit reports, and respond to regulatory requests from a single interface
6. **Test and production environments** are strictly separated with no data contamination
7. **Audit trail** satisfies CBI and FCA record-keeping standards (verified by internal audit)

---

## Appendices

- **Appendix A:** Full KYB requirements by product type — see wiki: KYB Requirements by Product Type
- **Appendix B:** Developer-friendly provider comparison — see wiki: KYB Provider Comparison — Top 10 Developer-Friendly Providers
- **Appendix C:** UX-focused provider comparison — see wiki: KYB Provider UX Comparison — Top 10 for User Experience & Simplistic Design
- **Appendix D:** Detailed Kota KYB software requirements — see wiki: Kota KYB Software Requirements

---

*This document was generated from the Kota Compliance Knowledge Base. All source materials, provider research, and cross-references are maintained in the wiki for ongoing updates.*
