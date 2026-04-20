---
title: Data Retention
type: concept
tags:
  - compliance/data-protection
  - regulation/cbi
  - regulation/gdpr
  - status/upcoming
created: 2026-04-08
updated: 2026-04-08
source_count: 1
status: active
---

# Data Retention

## Definition
Data retention covers the rules on how long personal data, customer records, and quote data may be held by a regulated firm — and when that data must be deleted. For [[Kota]], this is governed by the Revised Consumer Protection Code 2025, GDPR, and related Irish/UK data protection legislation.

## Regulatory Framework

### Revised Consumer Protection Code 2025 (effective 24 March 2026)

Record retention distinguishes between two consumer categories:

| Consumer category | Retention period | Notes |
|-------------------|------------------|-------|
| Consumer became a customer (product/service provided) | **6 years** | Unchanged from prior CPC |
| Consumer did NOT become a customer (quote only, enquiry only) | **12 months** | Reduced from 6 years |

The 12-month period is **subject to consumer consent** — if consent is withdrawn, data must be deleted immediately.

**Regulatory basis:** S.I. No. 81/2025 — Consumer Protection Regulations 2025, record retention provisions (exact regulation number to be confirmed against full statutory instrument — Regulation 48 of this S.I. covers prominence of key information, not retention)

### GDPR — Regulation (EU) 2016/679

- **Art.5(1)(e)** — Storage limitation: data kept only "for no longer than is necessary"
- **Art.17** — Right to erasure ("right to be forgotten")

### DPC Guidance on Insurance Quote Data

> "Where the quotation process has concluded and there is no follow-up to complete a contract, the data controller should ensure that the data collected is securely deleted within a limited 'cooling off' period (for example 21 days)."

The DPC's suggested ~21 days is **shorter** than the CPC 2025 12-month maximum.

### CJA 2010 (AML Records)

- **s.55** — AML records retained for **5 years** after the end of the business relationship (separate regime, applies where KYB/KYC has been performed)

## Key Principles

1. **CPC 2025 caps, GDPR governs** — The CPC sets the maximum, but GDPR requires retention only as long as necessary for the specified purpose
2. **Purpose-based retention** — Firms must articulate why data is being kept, for what purpose, and for how long
3. **Consent for non-customer data** — 12-month retention requires consumer consent; must be capturable and revocable
4. **Delete at end of period** — automated workflows must delete/anonymise data when the retention period ends
5. **Right to erasure** — consumers can request deletion at any time (GDPR Art.17)

## Retention Schedule (Draft)

| Data type | Retention period | Basis | Trigger for deletion |
|-----------|-----------------|-------|---------------------|
| Customer records (active relationship) | 6 years after relationship ends | CPC 2025 | End of relationship + 6 years |
| Quote-only / non-customer records | Up to 12 months (with consent); DPC suggests ~21 days | CPC 2025 / GDPR Art.5(1)(e) | End of retention period or consent withdrawal |
| AML/KYB records (where CDD performed) | 5 years after business relationship ends | CJA 2010 s.55 | End of relationship + 5 years |
| Complaint records | Subject to CPC record-keeping + GDPR | CPC 2025 / GDPR | Per documented schedule |
| Financial transaction data | 6 years (tax/audit) | Tax and accounting rules | End of period |

## Our Approach
[[Kota]] must implement retention controls across:
- Quote engine and pricing systems
- Partner API flows (Embed) — quote data flowing through third-party platforms
- Analytics, logs, and backups
- Privacy notice and consent capture at point of quote

## Open Questions / Gaps
- What is Kota's current retention practice for non-customer quote data?
- Is there an automated deletion mechanism in place, or is data retained indefinitely?
- Does the privacy notice state the 12-month retention period?
- Is consumer consent captured at point of quote?
- For Embed partner flows, how does retention obligation flow between partner and Kota?
- Does Kota apply the DPC's ~21-day "cooling off" approach, or the full 12 months?

## Action Items (Pre 24 March 2026)

| Action | Owner |
|--------|-------|
| Review current quote data retention periods and systems | DPO |
| Map data flows for quote-only records (Platform and Embed) | Engineering + Compliance |
| Design automated deletion workflow | Engineering |
| Update privacy notice to reflect 12-month retention | Legal / DPO |
| Implement consent capture at point of quote | Engineering + UX |
| Document retention schedule | Compliance |

## Sources
- [[CPC 2025 — Customer Quote Data Retention and Deletion]]
- S.I. No. 81/2025 — Section 48 Consumer Protection Regulations 2025
- GDPR Art.5(1)(e), Art.17
- DPC Guidance on insurance quote retention
- CJA 2010 s.55 (AML record-keeping)
