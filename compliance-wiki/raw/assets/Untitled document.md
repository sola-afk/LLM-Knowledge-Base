Let me search for context about Kota and their KYB needs from our past conversations and your Google Drive.Now let me search for more specific KYB-related discussions in Slack and Drive.Now I have a comprehensive picture. Let me compile everything into a thorough requirements list.

Based on everything I know from our past conversations about Kota's business — a CBI-regulated insurance intermediary with two verticals (Platform for employers, and Embed/Developer for EORs, global payroll and HR companies), currently using ComplyAdvantage for sanctions screening — here's the complete list of what Kota would need from a perfect KYB software provider:

---

## **Core Business Verification**

**Company identity verification.** The provider must be able to verify the legal identity of employers being onboarded — company name, registration number, registered address, incorporation date, and jurisdiction. This applies across both Platform (where Kota onboards employers directly) and Embed (where partner platforms like Remote, Helios, and Employment Hero are creating employers via API or UI components). Kota operates across multiple European markets, so the provider needs registry coverage across EU/EEA and UK jurisdictions at a minimum.

**UBO (Ultimate Beneficial Owner) identification.** The provider must identify and verify the individuals who ultimately own or control each employer entity. This is a regulatory requirement under both the CBI's AML framework and the EU Anti-Money Laundering Directives. It needs to handle complex ownership structures — holding companies, trusts, multi-layered corporate chains — and flag where ownership thresholds (typically 25%) are met.

**Director and officer identification.** Beyond UBOs, the provider should identify company directors and key officers, since these individuals may also need to be screened for sanctions and PEP status. This connects directly to Kota's existing ComplyAdvantage workflow for individual-level screening.

---

## **Sanctions, PEP & Adverse Media Screening**

**Company-level sanctions screening.** The provider must screen the employer entity itself against global sanctions lists (EU, UK, US OFAC, UN, and others). Kota currently screens new customers and their employees via ComplyAdvantage before onboarding — the KYB tool needs to extend or complement this at the entity level.

**UBO and director PEP and sanctions screening.** Once UBOs and directors are identified, the provider should automatically screen each individual against PEP databases and sanctions lists. Kota's compliance team already processes PEP and sanctions cases in ComplyAdvantage Mesh (with over 363 cases in the queue at one point), so the KYB provider either needs to integrate with ComplyAdvantage or offer comparable screening with configurable fuzzy matching (Kota calibrates in the 70–85% range to balance sensitivity and false positives).

**Adverse media screening.** The provider should scan for negative news associated with the entity, its UBOs, and directors — particularly around financial crime, fraud, money laundering, terrorism financing, and regulatory enforcement actions.

**Ongoing monitoring.** One-time screening isn't enough. The provider must offer continuous or periodic re-screening for changes in sanctions lists, PEP status, ownership structure, and adverse media. This is critical for Kota's obligation to maintain up-to-date due diligence throughout the customer relationship.

---

## **Risk Assessment & Scoring**

**Configurable risk scoring.** The provider should assign risk scores to each entity based on factors like jurisdiction, industry, ownership complexity, screening results, and source of funds. Kota needs the ability to configure risk thresholds and scoring models to match its own risk appetite — one of the goals flagged with ComplyAdvantage was reducing false positive alerts, so smart risk calibration is essential.

**Risk-based tiering.** The provider should support different due diligence tiers (standard, enhanced, simplified) based on the assessed risk. For instance, a straightforward Irish employer with clear ownership is standard due diligence, while a company incorporated in a high-risk jurisdiction with complex ownership chains triggers enhanced due diligence.

**Automated low-risk approvals.** For clearly low-risk entities where all checks pass cleanly, the provider should support auto-approval workflows to reduce manual review burden on the compliance team. This was a specific pain point — the volume of false positives in ComplyAdvantage was generating unnecessary workload.

---

## **Embed-Specific Requirements**

**API-first architecture.** This is non-negotiable. Kota's Embed product is built around API and UI component integrations with partners like Remote, Employment Hero, Helios, and Globalli. The KYB provider must offer a robust, well-documented API so that KYB checks can be triggered programmatically when a new employer is created via the Embed flow — without requiring manual intervention.

**Webhook and event-driven notifications.** When a screening result changes, a case needs review, or an entity's risk profile shifts, the provider should push events to Kota's backend rather than requiring polling. This fits Kota's existing backend architecture where the API handles auth flows and partner-specific routing.

**White-label / invisible integration.** In the Embed model, employers are created inside partner platforms that carry the partner's branding — not Kota's. The KYB checks need to happen seamlessly in the background without exposing the KYB provider's brand or interface to the end user. The partner's employer and employee experience shouldn't be disrupted.

**Bulk onboarding support.** Embed partners can bring large volumes of employers at once. The provider needs to handle bulk screening and batch processing efficiently, not just one-at-a-time checks.

**Multi-entity handling.** The provider needs to understand the layered relationship: there's the Embed partner (e.g., Remote), and then there are the employers that the partner onboards through Kota. KYB needs to work at both levels — Kota performs due diligence on the partner itself, and then on each employer created through that partner's integration.

---

## **Platform-Specific Requirements**

**Self-serve employer onboarding integration.** On the Platform side, employers sign up more directly. The KYB provider should integrate into this onboarding flow so that verification happens at or before the point where the employer can access insurance products — Kota's policy is to complete due diligence at the onboarding stage and before transactions occur.

**Employee-level KYC connection.** While KYB focuses on the company, Kota also screens individual employees (KYC and sanctions). The provider should either handle both KYB and KYC or integrate cleanly with ComplyAdvantage (or a replacement) for the individual-level checks.

---

## **Jurisdictional Coverage**

**EU/EEA and UK coverage.** Kota is regulated by the CBI in Ireland and operates in the UK as an appointed representative of Innovative Risk Labs Ltd (FCA). The KYB provider must have company registry access and screening capability across all markets Kota serves — including Ireland, UK, Germany, Spain, Netherlands, France, and the broader EEA, at minimum.

**Country-specific statutory requirements.** Different jurisdictions have different thresholds and requirements for UBO disclosure, PEP definitions, and AML obligations. The provider must handle these variations rather than applying a one-size-fits-all approach.

---

## **Case Management & Workflow**

**Case management interface.** When alerts are triggered, the compliance team needs a clear case management workflow — similar to what they use in ComplyAdvantage Mesh today. This means the ability to review cases, add notes, escalate, mark as false positive, close cases, and maintain an auditable record of every decision.

**Configurable alert thresholds.** A major pain point with ComplyAdvantage has been the volume of false positive alerts (363+ cases at one point, plus excess test data contaminating the system). The perfect provider would let Kota configure alert thresholds, exclude low-risk screenings from becoming full cases, and apply risk-based routing so that high-risk cases get priority while low-risk ones can be bulk-processed.

**Analyst workflow support.** The provider should support workflows where clear-cut cases (e.g., name removed from a sanctions list, obvious entity mismatch) can be auto-resolved or resolved in bulk, while ambiguous cases are escalated for manual review. Kota's team already follows a procedure for this (documented in a Scribe SOP for reviewing and escalating customer cases).

**Audit trail and record-keeping.** Every screening, decision, escalation, and case closure needs to be logged in a way that satisfies CBI and FCA record-keeping requirements. The CBI can ask to see these logs, and Kota already maintains formal registers (errors register, complaints register) — KYB records need to be equally robust.

---

## **Data & Privacy**

**GDPR and UK GDPR compliance.** The provider must be fully compliant with EU GDPR and UK data protection law. Given that Kota processes personal data of employers, their UBOs, directors, and employees across multiple jurisdictions, the provider needs clear data processing agreements, lawful bases for processing, and data subject rights support.

**Data residency options.** Ideally the provider offers EU data residency to simplify Kota's data protection obligations and avoid cross-border transfer complications.

**Data minimisation.** The provider should only collect and retain what's necessary for the KYB checks — not hoover up excess data that increases Kota's GDPR exposure.

**Sub-processor transparency.** Kota performs vendor due diligence on all third-party providers, including reviewing sub-processors. The KYB provider needs to maintain and publish a clear sub-processor list and notify Kota of changes.

---

## **Security & Vendor Due Diligence**

**SOC 2 and/or ISO 27001 certification.** Kota's vendor due diligence process requires evidence of security certifications. The provider should hold at least SOC 2 Type II and ideally ISO 27001\.

**Penetration testing and vulnerability management.** The provider should be able to evidence regular pen testing and a mature vulnerability management programme.

**Encryption and access controls.** Data at rest and in transit must be encrypted, with role-based access controls and MFA for the case management interface.

---

## **Reporting & Regulatory Support**

**Regulatory reporting outputs.** The provider should support generating the reports Kota needs for regulatory submissions — suspicious activity reports, periodic screening summaries, and compliance dashboards.

**Management information.** Dashboards showing screening volumes, case resolution times, false positive rates, and risk distribution help the compliance team demonstrate effective oversight to the CBI and FCA.

**Transaction monitoring integration.** Kota's compliance team has finalised transaction monitoring procedures. The KYB provider should either include or integrate with transaction monitoring to flag suspicious patterns at the entity level.

---

## **Practical Considerations**

**Clean test/production separation.** A major issue with ComplyAdvantage was test data contaminating the production environment — excess screenings from non-customers and test entities that were difficult to distinguish from real data. The perfect provider would enforce strict separation between test and production environments.

**Reasonable false positive rates.** This keeps coming up. The provider's matching algorithms need to be sophisticated enough to minimise noise while still catching genuine risks. Configurable fuzzy matching, entity resolution, and smart deduplication are all essential.

**Responsive support and account management.** Given the regulatory stakes, Kota needs a provider with strong account management and responsive support — not just a self-serve platform where issues go into a ticket queue.

---

This covers the full picture based on what I know about how Kota operates across both Platform and Embed. Want me to turn this into a formal evaluation scorecard or RFP document?

