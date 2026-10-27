# Builds phrases.json (clean key:value map, keys = normalised Spanish) + phrases_meta.json (es, cat, note, alt) from: hand-written phrasebook + every sentence taught in the course.
import json, sys, unicodedata, re
sys.path.insert(0, 'tools'); from phrases_src import P; from content import C; from vocab_az_src import V
norm = lambda t: re.sub(r"\s+", " ", re.sub(r"[^\w\s]", " ", ''.join(c for c in unicodedata.normalize('NFD', t.lower()) if unicodedata.category(c) != 'Mn'))).strip()
out, seen = [], set()
for cat, items in P.items():
    for it in items:
        es, va = it[0], it[1]; note = it[2] if len(it) > 2 else ""
        k = norm(es)
        if k in seen: continue
        seen.add(k); alts = [a.strip() for a in va.split("|")]
        out.append({"es": es, "va": alts[0], "alt": alts[1:], "cat": cat, "note": note})
for lv, (lt, units) in C.items():
    for ut, col, lessons, *_ in units:
        for title, words, phrases in lessons:
            for ph in phrases:
                k = norm(ph[1])
                if k in seen: continue
                seen.add(k)
                out.append({"es": ph[1], "va": ph[0], "alt": [], "cat": "Del curso", "note": (ph[2] + " " if len(ph) > 2 else "") + f"Curso {lv} · {title}."})
vseen = {norm(a) for o in out for a in [o["va"]] + o["alt"]}
for es, va, note in V:
    k = norm(es); alts = [a.strip() for a in va.split("|")]
    if k in seen or norm(alts[0]) in vseen: continue
    seen.add(k); vseen.add(norm(alts[0]))
    out.append({"es": es, "va": alts[0], "alt": alts[1:], "cat": "Vocabulario A–Z", "note": note})
cap = lambda t: t[:1].upper() + t[1:]
main = {norm(o["es"]): cap(o["va"]) for o in out}
meta = {norm(o["es"]): {k: v for k, v in {"es": o["es"], "cat": o["cat"], "note": o["note"], "alt": [cap(a) for a in o["alt"]]}.items() if v} for o in out}
assert len(main) == len(out)
json.dump(main, open('phrases.json', 'w'), ensure_ascii=False, indent=0)
json.dump(meta, open('phrases_meta.json', 'w'), ensure_ascii=False, separators=(",", ":"))
from collections import Counter
print(len(out), Counter(o["cat"] for o in out))
