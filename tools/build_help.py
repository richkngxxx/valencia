# Builds help.json (per-item explanations + grammar topics) and qa.json (learner Q&A).
import json, re, sys, unicodedata
sys.path.insert(0, 'tools'); from content import C; from help_src import T, L, X; from qa_src import Q
def norm(t): return re.sub(r"\s+", " ", re.sub(r"[^\w\s]", " ", ''.join(c for c in unicodedata.normalize('NFD', t.lower()) if unicodedata.category(c) != 'Mn'))).strip()
def ikey(va): return norm(va.replace("'", " "))
PRON = [(r"x", "x suena como «sh» [ʃ]"), (r"ix", "ix suena [jʃ] (i + sh)"), (r"ll", "ll suena [ʎ]"), (r"ny", "ny suena como ñ"), (r"ç", "ç suena como s"),
        (r"tx|ig\b", "tx / ig final suenan como «ch»"), (r"[gj][eiéèí]|j", "j y g + e/i suenan [dʒ] (como la j inglesa)"), (r"tg|tj", "tg / tj suenan [dʒ]"),
        (r"z", "z suena como s sonora [z]"), (r"[aeiouàèéíòóú]s[aeiouàèéíòóú]", "s entre vocales suena sonora [z]"), (r"l·l", "l·l es una l doble"),
        (r"[àèò]", "à/è/ò: vocal abierta"), (r"[éó]", "é/ó: vocal cerrada"), (r"ï|ü", "la diéresis separa sílabas")]
def pron_hints(va):
    v = va.lower(); out = []
    for rx, h in PRON:
        if re.search(rx, v) and h not in out: out.append(h)
    return out[:3]
items, idx = {}, {}
lessons = [(lv, ut, l) for lv, (lt, units) in C.items() for ut, col, ls, *_ in units for l in ls]
allphr = [(p[0], p[1]) for _, _, l in lessons for p in l[2]]
def examples(va, own):
    toks = set(ikey(va).split()) - {"el", "la", "de", "i", "a", "un", "una", "es", "em", "et"}
    ex = [p for p in own if toks & set(ikey(p[0]).split())]
    ex += [p for p in allphr if p not in ex and toks and toks <= set(ikey(p[0]).split())]
    return [{"va": a, "es": b} for a, b in ex[:2]]
for lv, ut, (title, words, phrases) in lessons:
    topic = L.get(title, "")
    thorough = lv in ("A1", "A2")
    for w in list(words) + [(p[0], p[1], p[2] if len(p) > 2 else "") for p in phrases]:
        k = ikey(w[0])
        if k in items: continue
        x = X.get(w[0].lower(), ("", ""))
        e = {"va": w[0], "es": w[1], "level": lv, "lesson": title, "topic": topic}
        if len(w) > 2 and w[2]: e["note"] = w[2]
        ph = [x[0]] if x[0] else []
        if thorough or not ph: ph += pron_hints(w[0])
        if ph: e["pron"] = ph[:3]
        if x[1]: e["mistake"] = x[1]
        exs = examples(w[0], [(p[0], p[1]) for p in phrases if p[0] != w[0]])
        if exs: e["examples"] = exs
        items[k] = e
topics = {k: {"title": t, "text": a, "mistake": m} for k, (t, a, m) in T.items()}
missing = sorted({L.get(l[0]) for _, _, l in lessons} - set(T)) + [l[0] for _, _, l in lessons if l[0] not in L]
assert not missing, missing
json.dump({"items": items, "topics": topics}, open("help.json", "w"), ensure_ascii=False, separators=(",", ":"))
qa = [{"id": i, "q": q, "a": a, "tags": t, "syn": s, "k": norm(" ".join([q] + s + t))} for i, (q, a, t, s) in enumerate(Q)]
json.dump(qa, open("qa.json", "w"), ensure_ascii=False, separators=(",", ":"))
A = [k for k, v in items.items() if v["level"] in ("A1", "A2")]
print("help items", len(items), "(A1/A2", len(A), ", with mistake", sum(1 for k in A if "mistake" in items[k]), ", with examples", sum(1 for k in A if "examples" in items[k]), ") topics", len(topics), "| qa", len(qa))
