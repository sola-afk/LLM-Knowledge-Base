# CPC 2025 — Customer Quote Data Retention and Deletion

*Research on record retention requirements for quote data under the Revised Consumer Protection Code 2025 (effective 24 March 2026), together with the underlying GDPR position.*

**Sources:**
- S.I. No. 81/2025 — Central Bank (Supervision and Enforcement) Act 2013 (Section 48) (Consumer Protection) Regulations 2025
- DPC Guidance — How long can an insurance quote be held for?
- Insurance Ireland Guidance on Data Protection Requirements (Jan 2024)
- William Fry, Addleshaw Goddard, Mason Hayes Curran briefings on CPC 2025

---

## Key Rule — CPC 2025 Record Retention

The CPC 2025 distinguishes between two categories of consumer record:

| Consumer category | Retention period | Notes |
|-------------------|------------------|-------|
| Consumer **did become a customer** (product/service provided) | **6 years** | In line with existing CPC (unchanged) |
| Consumer **did NOT become a customer** (e.g., obtained a quote but didn't proceed) | **12 months** | Reduced from 6 years under previous Code |

The 12-month retention period for non-customer records is **subject to consumer consent** — if the consumer withdraws consent for data retention, the data must not be retained for the 12 months.

**Regulatory basis:** S.I. No. 81/2025 (Section 48 Consumer Protection Regulations 2025), general record-keeping provisions.

## Implication for Quote Data

A consumer who obtains an insurance quote and does not proceed to purchase is a **non-customer** under CPC 2025. Their quote data:

1. May be retained for **up to 12 months** from the date of the quote
2. The retention is **consent-based** — if the consumer asks for deletion, the data must be deleted
3. After 12 months, the data must be **deleted** (or anonymised) unless another lawful basis for continued retention applies

## The GDPR Overlay — Storage Limitation

Under Regulation (EU) 2016/679 (GDPR):

- **Art.5(1)(e)** — Storage limitation principle: personal data must be "kept in a form which permits identification of data subjects for no longer than is necessary for the purposes for which the personal data are processed"
- **Art.17** — Right to erasure ("right to be forgotten") where data is no longer necessary for the purpose

### DPC Guidance on Insurance Quote Data

The Irish Data Protection Commission has specifically addressed insurance quote retention:

> "Where the quotation process has concluded and there is no follow-up to complete a contract, the data controller should ensure that the data collected is securely deleted within a limited 'cooling off' period (for example 21 days) in case the individual changes their decision to take up the contractual offer."

This is a **shorter period** than the CPC 2025 12-month maximum and reflects the DPC's expectation that data minimisation under GDPR takes precedence.

### Reconciling CPC 2025 (12 months) vs GDPR (21 days)

These are not in conflict — they operate at different levels:

- **CPC 2025** sets the **maximum** period a firm may retain records for regulatory purposes
- **GDPR Art.5(1)(e)** requires the firm to justify retention for **only as long as necessary** for a specified purpose

A firm must:
1. Identify a **lawful basis** and **specific purpose** for retention (e.g., responding to complaints, demonstrating compliance, follow-up on abandoned quote)
2. Retain for no longer than **necessary for that purpose**
3. Delete when the purpose is exhausted — this may be well before the 12-month CPC maximum

For a quote that the consumer abandoned with no further contact, retention beyond the DPC's suggested "cooling off" period (~21 days) would likely require specific justification.

## Practical Implications for Insurance Distributors

### Systems and Processes
1. **Automated deletion workflow** — quote data must be automatically deleted/anonymised at the end of the retention period
2. **Retention tagging** — distinguish at record level between "customer" records (6 years) and "quote-only" records (12 months max)
3. **Consent capture** — at point of quote, capture consent for the 12-month retention; enable consent withdrawal
4. **Deletion on request** — enable consumers to request deletion at any time (GDPR Art.17)
5. **Privacy notice** — must clearly state retention periods and consumer rights

### Data Flows to Address
- **Quote engine** — quotes stored in underwriting or pricing systems
- **Partner API flows** — where third parties create quotes, retention obligations sit with Kota as controller/intermediary
- **Analytics/logs** — pricing data, application data, abandonment data
- **Backups** — deletion must propagate to backup systems within reasonable period

### Documentation
- **Retention schedule** — documented matrix of data categories and retention periods
- **Deletion evidence** — logs demonstrating deletion at end of retention period
- **Consent records** — evidence of consumer consent to 12-month retention

## Open Questions

1. What is Kota's current retention practice for non-customer quote data?
2. Is there a technical deletion mechanism in place, or is data retained indefinitely?
3. Does the privacy notice clearly state the 12-month retention period for quote-only data?
4. Is consumer consent captured at the point of quote?
5. For quotes generated via Embed partner APIs, how does the retention obligation flow between the partner and Kota?
6. Does Kota currently apply the DPC's ~21-day "cooling off" approach, or the full 12 months?

## Action Items (Pre 24 March 2026)

| Action | Owner | Timing |
|--------|-------|--------|
| Review current quote data retention periods and systems | Data Protection Officer | Now |
| Map data flows for quote-only records (Platform and Embed) | Engineering + Compliance | Q2 2026 |
| Design automated deletion workflow | Engineering | Q2–Q3 2026 |
| Update privacy notice to reflect 12-month retention | Legal / DPO | Before 24 March 2026 |
| Implement consent capture at point of quote | Engineering + UX | Before 24 March 2026 |
| Document retention schedule | Compliance | Before 24 March 2026 |
