#!/usr/bin/env python3
"""
Field projection for Intercom eval runs.

Why this exists: a 10-conversation search returns ~93KB and a single 51-part
conversation ~65KB, with some conversations reaching 117 parts. Loading whole
payloads into an assessment context is not viable. This projects out only the
fields the criteria actually need, so a run is repeatable rather than ad-hoc.

Operates on MCP tool output already saved to disk (the MCP client persists
oversized results to a file and prints the path).

Usage
  extract.py triage  <search-result.json>      # Step 1-5: population + triage table
  extract.py content <get-conversation.json>   # Step 4/7: graded vs context parts
  extract.py clock   <get-conversation.json>   # Step 7: HF-24 timeline arithmetic

Field contract mirrors `Researcher/req-intercom-detection-criteria.md`
§ Output requirements. Change both together.
"""
import json
import re
import sys
from datetime import datetime, timezone

# --- scoping (criteria § Population in scope) ---------------------------------
CX_TEAM_IDS = {5690482}          # PL: CX Platform- Customer. Extend as CS teams are enumerated.
CX_TICKET_TYPES = {"PL-CX: Customer Ticket"}
KOTA_DOMAIN = "@kota.io"

# part_type: only `comment` is graded. `note` is read as context (HF-27). Everything
# else is a state change, not communication.
GRADED, CONTEXT = "comment", "note"

# CPC / DISP deadlines — research-complaints-handling.md
CPC_ACK_DAYS, CPC_UPDATE_DAYS, CPC_FINAL_DAYS = 5, 20, 40
DISP_FINAL_WEEKS = 8


def load(path):
    """MCP results arrive either bare or wrapped in [{"type":"text","text":"<json>"}]."""
    raw = json.load(open(path))
    if isinstance(raw, list) and raw and isinstance(raw[0], dict) and "text" in raw[0]:
        return json.loads(raw[0]["text"])
    return raw


def strip_html(s):
    if not s:
        return ""
    s = re.sub(r"<br[^>]*>|</p>|</div>|</li>", "\n", s)
    s = re.sub(r"<[^>]*>", "", s)
    for a, b in (("&nbsp;", " "), ("&amp;", "&"), ("&#39;", "'"),
                 ("&quot;", '"'), ("&lt;", "<"), ("&gt;", ">"), ("&hellip;", "...")):
        s = s.replace(a, b)
    return re.sub(r"\n{3,}", "\n\n", s).strip()


def is_kota(author):
    """Identity resolves on email domain, NOT author.type.

    Kota staff appear as author.type == "user" when recorded as an Intercom contact —
    the 2026-08-04 dry run found conversations authored by a registered QFA holder
    that way. Keying on author.type silently skips staff content.
    """
    if not author:
        return False
    if author.get("type") == "admin":
        return True
    return (author.get("email") or "").lower().endswith(KOTA_DOMAIN)


def actor(author):
    if not author:
        return "unknown"
    if author.get("type") == "bot":
        return "bot"            # never registrable — unqualified by construction
    return "kota" if is_kota(author) else "customer"


def ts(epoch):
    if not epoch:
        return None
    return datetime.fromtimestamp(epoch, tz=timezone.utc)


def business_days(a, b):
    if not a or not b:
        return None
    lo, hi = sorted((a.date(), b.date()))
    days = (hi - lo).days
    # Approximate: calendar days minus weekends. Public holidays are NOT excluded,
    # so a value at/near a deadline needs manual confirmation before escalation.
    full_weeks, rem = divmod(days, 7)
    n = full_weeks * 5
    d = lo
    for _ in range(rem):
        d += __import__("datetime").timedelta(days=1)
        if d.weekday() < 5:
            n += 1
    return n


def in_scope(c):
    """team_assignee_id + ticket_type govern; Brand is advisory (they can disagree)."""
    team = c.get("team_assignee_id")
    tt = (c.get("ticket") or {}).get("ticket_type")
    brand = (c.get("custom_attributes") or {}).get("Brand", "")
    ok = team in CX_TEAM_IDS or tt in CX_TICKET_TYPES
    note = " [brand/ticket-type disagree]" if ok and "BenOps" in str(brand) else ""
    return ok, note


def cmd_triage(path):
    d = load(path)
    convs = d.get("conversations", [d])
    print(f"total matching filter: {d.get('total_count', '?')}   returned: {len(convs)}\n")
    hdr = f"{'id':<18}{'issue':<24}{'topic':<26}{'provider':<18}{'user':<10}{'sla':<9}{'parts':>6}{'state':<10} flags"
    print(hdr)
    print("-" * len(hdr))
    for c in convs:
        ca = c.get("custom_attributes") or {}
        ok, note = in_scope(c)
        flags = []
        if not ok:
            flags.append("OUT-OF-SCOPE")
        if note:
            flags.append(note.strip())
        if c.get("ai_agent_participated"):
            flags.append("fin")
        if not ca.get("PL:Topic"):
            flags.append("NO-TOPIC(fail-closed)")
        if ca.get("Type of user") == "Internal":
            flags.append("EXCLUDE:internal")
        if (c.get("source", {}).get("author", {}).get("email") or "").endswith(KOTA_DOMAIN):
            flags.append("KOTA-AUTHORED-as-user")
        if "Complaint" in str(ca.get("PL: Issue Type", "")):
            flags.append("COMPLAINT")
        st = c.get("statistics") or {}
        print(f"{c.get('id',''):<18}{str(ca.get('PL: Issue Type','-'))[:23]:<24}"
              f"{str(ca.get('PL:Topic','-'))[:25]:<26}{str(ca.get('Provider','-'))[:17]:<18}"
              f"{str(ca.get('Type of user','-'))[:9]:<10}"
              f"{str((c.get('sla_applied') or {}).get('sla_status','-')):<9}"
              f"{st.get('count_conversation_parts',0):>6}  {str(c.get('state','-')):<10}"
              f" {' '.join(flags)}")


def cmd_content(path):
    d = load(path)
    parts = (d.get("conversation_parts") or {}).get("conversation_parts", [])
    src = d.get("source") or {}
    print(f"conversation {d.get('id')}  |  {strip_html(src.get('subject'))[:70]}")
    print(f"opened by: {actor(src.get('author'))} <{(src.get('author') or {}).get('email','-')}>")
    print(f"permalink: {(d.get('ticket') or {}).get('url','-')}\n")

    kota_names = {p["author"].get("name") for p in parts
                  if p.get("part_type") in (GRADED, CONTEXT) and actor(p.get("author")) == "kota"}
    print(f"Kota authors (resolve against MCC register): {sorted(n for n in kota_names if n)}")
    print(f"bot authored graded parts: "
          f"{sum(1 for p in parts if p.get('part_type') == GRADED and actor(p.get('author')) == 'bot')}\n")

    for label, want in (("GRADED — customer-facing (part_type=comment)", GRADED),
                        ("CONTEXT ONLY — internal notes (part_type=note), never graded", CONTEXT)):
        print("=" * 78)
        print(label)
        print("=" * 78)
        for p in parts:
            if p.get("part_type") != want:
                continue
            body = strip_html(p.get("body"))
            if not body:
                continue
            a = p.get("author") or {}
            print(f"\n[{actor(a)}] {a.get('name','-')}  part_id={p.get('id')}")
            print(body)
        print()


def cmd_clock(path):
    d = load(path)
    st = d.get("statistics") or {}
    ca = d.get("custom_attributes") or {}
    created = ts(d.get("created_at"))
    first = ts(st.get("first_admin_reply_at"))
    close = ts(st.get("first_close_at"))
    classified = "Complaint" in str(ca.get("PL: Issue Type", ""))

    print(f"conversation {d.get('id')}")
    print(f"platform classification : {ca.get('PL: Issue Type','-')}"
          f"  -> complaint={'YES' if classified else 'no'}")
    print(f"internal SLA            : {(d.get('sla_applied') or {}).get('sla_status','-')}"
          f"  ({(d.get('sla_applied') or {}).get('sla_name','-')})")
    print("  ^ commercial target, NOT a regulatory deadline. Report alongside, never instead of.\n")
    print(f"created                 : {created}")
    print(f"first admin reply       : {first}   ({business_days(created, first)} business days)")
    print(f"first close             : {close}   ({business_days(created, close)} business days)")

    if not classified:
        print("\nHF-24 not evaluated — conversation is not classified as a complaint.")
        print("If HF-23 finds complaint substance, re-run this after reclassification.")
        return
    ack, fin = business_days(created, first), business_days(created, close)

    # `ack is None` means no reply at all. `ack == 0` means a same-day reply — the best
    # possible case. Testing truthiness conflates them and reports "NO REPLY YET" for a
    # same-day acknowledgement, which would be a false positive on well-handled complaints.
    def verdict(days, limit, pending):
        if days is None:
            return pending
        return "BREACH" if days > limit else "ok"

    print("\nHF-24 (CPC):")
    print(f"  acknowledgement <= {CPC_ACK_DAYS}bd : "
          f"{verdict(ack, CPC_ACK_DAYS, 'NO REPLY YET — breach if now past 5bd')}")
    print(f"  final response  <= {CPC_FINAL_DAYS}bd : "
          f"{verdict(fin, CPC_FINAL_DAYS, 'STILL OPEN — clock running')}")
    print(f"  update interval <= {CPC_UPDATE_DAYS}bd : requires per-part gap analysis (not automated)")
    print("\nNote: business-day count excludes weekends only, not public holidays.")
    print("A result at or near a deadline must be confirmed manually before escalation.")


if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] not in ("triage", "content", "clock"):
        print(__doc__)
        sys.exit(1)
    {"triage": cmd_triage, "content": cmd_content, "clock": cmd_clock}[sys.argv[1]](sys.argv[2])
