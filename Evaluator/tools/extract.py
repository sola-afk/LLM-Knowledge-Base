#!/usr/bin/env python3
"""
Field projection for Fireflies call eval runs.

Why this exists: a 5-day `fireflies_get_transcripts` call returns ~139KB of TOON
across 48 meetings, and full transcripts are larger again. Loading that into an
assessment context is not viable. This projects out only what the run spec needs.

Mirrors `IntercomEvaluator/tools/extract.py`. Operates on MCP output already
saved to disk (the client persists oversized results and prints the path).

Usage
  extract.py triage <transcripts-list.txt>   # Step 1: customer-facing filter
  extract.py speakers <transcript.txt>       # Step 3: Kota-side speakers + authorisation

Field contract mirrors `Evaluator/spec-eval-daily-run.md`. Change both together.
"""
import re
import sys

# Kota-side domains. yonder.app is included because the 2026-08-31→09-04 run found
# calls organised by ceri@yonder.app and matthew@yonder.app, and BOTH Ceri Thomas and
# Matthew Brennan are on Kota's MCC register. Keying identity on "@kota.io" alone treats
# them as customers, so MCC detection is never applied to their speech — the same class of
# defect as Intercom's "staff appear as author.type: user". CONFIRM the Kota/Yonder
# relationship with Compliance; if Yonder is a separate legal entity the perimeter question
# changes, but treating registered staff as customers is wrong either way.
KOTA_DOMAINS = ("@kota.io", "@yonder.app")

# Not participants: calendar room resources and the notetaker bot itself. Counting these
# as external made 48/48 meetings "customer-facing" with zero internal-only discarded.
NON_HUMAN = ("resource.calendar.google.com", "fireflies.ai", "@group.calendar.google.com",
             "onmicrosoft.com")


def is_kota(email):
    return (email or "").lower().endswith(KOTA_DOMAINS)


def is_non_human(email):
    e = (email or "").lower()
    return any(d in e for d in NON_HUMAN)

# MCC register — research-mcc-fitness-probity.md is canonical (calibration rule R6).
# NOTE: spec-eval-daily-run.md Step 3 carries an inline copy that has DRIFTED from the
# register (it still lists Matthew Brennan as New Entrant, and omits Barbara Murray and
# Joana Crisostomo). This table follows the register, not the spec's copy.
QUALIFIED = {
    "trevor gardiner":  ("QUALIFIED", "all"),
    "patrick o'boyle":  ("QUALIFIED", "pensions, health, life"),
    "paul o'hanlon":    ("QUALIFIED", "all (QFA + APA PMI)"),
    "naoise baker":     ("QUALIFIED", "all (QFA + APA PMI)"),
    "daniel mcavinue":  ("QUALIFIED", "pensions, life; PMI via New Entrant"),
    "callum pearse":    ("QUALIFIED", "pensions; PMI via New Entrant"),
    "matthew brennan":  ("QUALIFIED", "pensions, life; PMI via New Entrant (upgraded 2026-05-26)"),
    "colin pon":        ("QUALIFIED", "PMI only"),
    "charlie blake":    ("QUALIFIED", "PMI only"),
    "barbara murray":   ("QUALIFIED*", "scope TBC by Compliance — do NOT fail closed"),
}
SCRIPT = {
    "henry godson", "katie garry", "will robbins", "simon ward",
    "claudia correa", "karl o'brien", "joana crisostomo", "joana crisóstomo",
}
UNREGISTERED = {"kate fullen", "ceri thomas", "luke mackey"}


# Diminutives seen in Fireflies speaker labels vs the register's formal names. The
# 2026-09-07→11 run labelled a speaker "Dan McAvinue" while the register says "Daniel
# McAvinue" (APA Pensions & Life). Exact matching returned UNRECOGNISED, which under
# fail-closed would have raised a spurious HF-00 against a QUALIFIED person — a false
# positive on the most serious criterion in the set.
ALIASES = {
    "dan mcavinue": "daniel mcavinue",
    "danny mcavinue": "daniel mcavinue",
    "matt brennan": "matthew brennan",
    "cal pearse": "callum pearse",
    "chas blake": "charlie blake",
    "charles blake": "charlie blake",
    "pat o'boyle": "patrick o'boyle",
    "paddy o'boyle": "patrick o'boyle",
    "barb murray": "barbara murray",
    "trev gardiner": "trevor gardiner",
    "kate garry": "katie garry",
    "si ward": "simon ward",
    "hen godson": "henry godson",
    "claudia correia": "claudia correa",
}


def authorisation(name):
    k = (name or "").strip().lower()
    k = ALIASES.get(k, k)
    if k in QUALIFIED:
        s, scope = QUALIFIED[k]
        return s, scope
    if k in SCRIPT:
        return "SCRIPT", "script only — Step 3.5 carve-out applies"
    if k in UNREGISTERED:
        return "UNREGISTERED", "cannot conduct regulated activity"
    return ("UNRECOGNISED",
            "fail closed (R6); but see R7. CHECK ALIASES before flagging HF-00 — a diminutive "
            "or spelling variant of a registered name is not an unregistered person")


def parse_transcripts(path):
    """Parse the TOON list format into records."""
    recs, cur, in_att = [], None, False
    for line in open(path):
        s = line.rstrip("\n")
        m = re.match(r"\s+- id:\s*(\S+)", s)
        if m:
            if cur:
                recs.append(cur)
            cur = {"id": m.group(1), "attendees": []}
            in_att = False
            continue
        if cur is None:
            continue
        for f in ("title", "dateString", "duration", "organizer_email"):
            m = re.match(rf"\s+{f}:\s*(.*)", s)
            if m:
                cur[f] = m.group(1).strip().strip('"')
                in_att = False
                break
        else:
            if re.match(r"\s+meeting_attendees\[", s):
                in_att = True
                continue
            if in_att and "," in s and not re.match(r"\s+\w+(\[\d+\])?[:{]", s):
                parts = s.strip().rsplit(",", 1)
                if len(parts) == 2 and "@" in parts[1]:
                    cur["attendees"].append((parts[0].strip(), parts[1].strip()))
    if cur:
        recs.append(cur)
    return recs


def cmd_triage(path):
    recs = parse_transcripts(path)
    keep, drop = [], []
    for r in recs:
        ext = [e for _, e in r["attendees"]
               if not is_kota(e) and not is_non_human(e)]
        kot = [e for _, e in r["attendees"] if is_kota(e)]
        (keep if ext else drop).append((r, kot, ext))

    print(f"{len(recs)} meetings returned; {len(keep)} customer-facing after filter "
          f"({len(drop)} internal-only discarded)\n")

    print("CUSTOMER-FACING")
    hdr = f"{'date':<12}{'id':<28}{'min':>5}  {'organizer':<22}{'ext domains':<26} title"
    print(hdr)
    print("-" * 128)
    for r, kot, ext in sorted(keep, key=lambda x: x[0].get("dateString", "")):
        doms = sorted({e.split("@")[-1] for e in ext})
        try:
            mins = f"{float(r.get('duration', 0)):.0f}"
        except (TypeError, ValueError):
            mins = "?"
        org = r.get('organizer_email', '-')
        flag = " [YONDER]" if org.lower().endswith("@yonder.app") else ""
        org = org.split("@")[0] + flag
        print(f"{r.get('dateString','')[:10]:<12}{r['id']:<28}{mins:>5}  "
              f"{org:<22}"
              f"{','.join(doms)[:25]:<26}{r.get('title','')[:44]}")

    print(f"\nINTERNAL-ONLY (discarded, {len(drop)})")
    for r, kot, ext in sorted(drop, key=lambda x: x[0].get("dateString", "")):
        print(f"  {r.get('dateString','')[:10]}  {r.get('title','')[:60]}")


def cmd_speakers(path):
    """Kota-side speakers in a fetched transcript, with authorisation resolved."""
    txt = open(path).read()
    speakers = {}
    for m in re.finditer(r"\[\d\d:\d\d - \d\d:\d\d\]\s*([^:]{1,60}?):", txt):
        n = m.group(1).strip()
        speakers[n] = speakers.get(n, 0) + 1
    emails = {e.lower() for e in re.findall(r"[\w.+-]+@[\w.-]+", txt)}
    kota_emails = sorted(e for e in emails if is_kota(e))

    print(f"kota.io addresses present: {kota_emails}\n")
    print(f"{'speaker':<28}{'turns':>6}  authorisation")
    print("-" * 92)
    for n, c in sorted(speakers.items(), key=lambda x: -x[1]):
        st, scope = authorisation(n)
        print(f"{n[:27]:<28}{c:>6}  {st:<14}{scope}")
    print("\nNon-kota speakers are customers — do NOT apply MCC detection to their speech (R1).")


if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] not in ("triage", "speakers"):
        print(__doc__)
        sys.exit(1)
    {"triage": cmd_triage, "speakers": cmd_speakers}[sys.argv[1]](sys.argv[2])
