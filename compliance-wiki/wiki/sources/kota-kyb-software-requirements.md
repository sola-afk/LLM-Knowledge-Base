---
title: "Kota KYB Software Requirements"
type: source
tags:
  - compliance/kyb
  - compliance/aml
  - compliance/sanctions-screening
  - compliance/data-protection
  - entity/vendor
  - process/due-diligence
  - regulation/cbi
  - regulation/fca
created: 2026-04-07
updated: 2026-04-07
source_file: raw/kota-kyb-software-requirements.md
status: active
---

# Kota KYB Software Requirements

## Key Takeaways
- Kota is a CBI-regulated insurance intermediary with two verticals: **Platform** (direct employer onboarding) and **Embed** (API-driven onboarding via partners like Remote, Employment Hero, Helios, Globalli).
- Currently uses **ComplyAdvantage** for sanctions screening but needs a comprehensive KYB solution covering company verification, UBO identification, sanctions/PEP/adverse media screening, and ongoing monitoring.
- Major pain points with ComplyAdvantage: **high false positive rates** (363+ cases at one point), **test data contaminating production**, and limited KYB-specific capability.
- The Embed product requires an **API-first, white-label** KYB provider with webhook support and bulk processing.
- GDPR compliance, EU data residency, and strong security certifications (SOC 2 / ISO 27001) are mandatory.

## Detailed Summary

### Core Business Verification
The KYB provider must verify employer entities across EU/EEA and UK jurisdictions — legal name, registration number, address, incorporation date, and jurisdiction. This applies to both Platform (direct onboarding) and Embed (partner-driven onboarding via API).

### UBO & Director Identification
Regulatory requirement under the CBI's AML framework and EU Anti-Money Laundering Directives. The provider must handle complex ownership structures (holding companies, trusts, multi-layered chains) and flag the 25% ownership threshold. Directors and key officers must also be identified for sanctions and PEP screening.

### Sanctions, PEP & Adverse Media Screening
- **Entity-level** sanctions screening (EU, UK, US OFAC, UN)
- **Individual-level** PEP and sanctions screening for UBOs and directors
- **Adverse media** scanning for financial crime, fraud, money laundering, terrorism financing
- **Ongoing monitoring** — continuous or periodic re-screening throughout the customer relationship
- Fuzzy matching configurable in the **70–85% range** to balance sensitivity and false positives

### Risk Assessment & Scoring
Configurable risk scoring based on jurisdiction, industry, ownership complexity, and screening results. Must support risk-based tiering (standard, enhanced, simplified due diligence) and automated low-risk approvals to reduce manual review burden.

### Embed-Specific Requirements
- **API-first architecture** — non-negotiable for partner integrations
- **Webhook/event-driven notifications** for status changes
- **White-label/invisible integration** — no provider branding visible to end users
- **Bulk onboarding** support for high-volume partner flows
- **Multi-entity handling** — due diligence at both partner level and employer level

### Platform-Specific Requirements
- Self-serve employer onboarding integration with KYB checks at onboarding stage
- Employee-level KYC connection — either handle both KYB and KYC or integrate with [[ComplyAdvantage]]

### Data & Privacy
- Full Regulation (EU) 2016/679 (GDPR) and UK GDPR compliance
- EU data residency preferred
- Data minimisation and clear sub-processor transparency

### Security & Vendor Due Diligence
- SOC 2 Type II and/or ISO 27001 certification required
- Regular penetration testing, encryption at rest and in transit, RBAC with MFA

### Case Management & Workflow
- Case management interface comparable to ComplyAdvantage Mesh
- Configurable alert thresholds to reduce false positives
- Analyst workflow support with auto-resolution for clear-cut cases
- Full audit trail satisfying [[Central Bank of Ireland]] and [[FCA]] record-keeping requirements

### Reporting
- Regulatory reporting outputs (SARs, periodic screening summaries)
- Management dashboards (volumes, resolution times, false positive rates)
- Transaction monitoring integration

### Practical Considerations
- Strict **test/production separation** (major ComplyAdvantage pain point)
- Reasonable false positive rates with smart entity resolution and deduplication
- Responsive support and dedicated account management

## Impact Assessment

> [!warning] Priority
> This is a **High** priority item. Kota's current KYB capability is limited — ComplyAdvantage handles sanctions screening but does not provide full KYB. Selecting and implementing a KYB provider is critical for regulatory compliance across both product verticals.

**Action items:**
1. Use this requirements document to create a formal vendor evaluation scorecard or RFP.
2. Assess whether ComplyAdvantage can be extended or should be replaced entirely.
3. Evaluate candidate providers against Embed API-first requirements specifically.
4. Ensure any selected provider meets CBI and FCA record-keeping standards.

## Cross-References
- Entity: [[Kota]]
- Entity: [[Central Bank of Ireland]]
- Entity: [[FCA]]
- Entity: [[ComplyAdvantage]]
- Concept: [[KYB (Know Your Business)]]
- Concept: [[Sanctions and PEP Screening]]
- Concept: [[UBO Identification]]
- Concept: [[AML Compliance]]

## Raw Source
`raw/kota-kyb-software-requirements.md`
