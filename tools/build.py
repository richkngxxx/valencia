# Builds lessons.js: every lesson gets 3 levels (sessions) generated from its vocab and sentences.
import json, random, re, sys
sys.path.insert(0, __file__.rsplit('/', 1)[0]); from content import C
cap = lambda s: s[:1].upper() + s[1:]

def es_variants(es):
    base = re.sub(r"\s*\(.*?\)", "", es).strip()
    out = {es, base} | {p.strip() for p in base.split(" / ")}
    return sorted(x for x in out if x)

def learn(w, label=None):
    e = {"type": "learn", "word": cap(w[0]), "meaning": w[1]}
    if label: e["label"] = label
    if len(w) > 2 and w[2]: e["note"] = w[2]
    return e

def mc(w, pool, rnd, to_val):
    others = [x for x in pool if x[0].lower() != w[0].lower() and x[1].lower() != w[1].lower()]
    d = rnd.sample(others, 3)
    if to_val: q, a, opts = f"¿Cómo se dice «{w[1]}»?", w[0], [x[0] for x in d]
    else: q, a, opts = f"¿Qué significa «{w[0]}»?", w[1], [x[1] for x in d]
    opts = opts + [a]; rnd.shuffle(opts)
    return {"type": "mc", "key": w[0], "question": q, "options": opts, "answer": a, "explanation": f"{w[0]} = {w[1]}."}

def type_val(w):
    return {"type": "type", "key": w[0], "question": f"Escribe en valenciano: «{w[1]}»", "answer": w[0],
            "accept": [w[0]] + (w[3] if len(w) > 3 else []), "explanation": f"{w[1]} = {w[0]}."}

def type_es(w):
    return {"type": "type", "key": w[0], "lang": "es", "question": f"Escribe en castellano: «{w[0]}»", "answer": es_variants(w[1])[0] if "(" in w[1] else w[1].split(" / ")[0],
            "accept": es_variants(w[1]), "explanation": f"{w[0]} = {w[1]}."}

def type_phrase(p):
    return {"type": "type", "key": p[0], "question": f"Traduce: «{p[1]}»", "answer": p[0], "accept": [p[0]], "explanation": p[1]}

def order(p, vocab, rnd):
    import unicodedata
    strip = lambda t: ''.join(c for c in unicodedata.normalize('NFD', t.lower()) if unicodedata.category(c) != 'Mn').strip(".,?!'")
    toks = p[0].split(); low = {strip(t) for t in toks}
    cand = sorted({t for x in vocab for t in x[0].split() if strip(t) not in low and "'" not in t})
    return {"type": "order", "key": p[0], "question": f"Traduce: «{p[1]}»", "answer": p[0], "words": toks, "distractors": rnd.sample(cand, 3)}

def match(ws, rnd):
    return {"type": "match", "key": "match:" + "|".join(w[0] for w in ws), "question": "Selecciona los pares", "pairs": [[w[0], w[1]] for w in ws]}

def pick_pairs(cands, rnd, n=5):
    out, sv, se = [], set(), set()
    for w in cands:
        if w[0].lower() in sv or w[1].lower() in se or w[0].lower() == w[1].lower(): continue
        out.append(w); sv.add(w[0].lower()); se.add(w[1].lower())
        if len(out) == n: break
    return out

def no_adjacent(seq, rnd):
    # reshuffle until no two consecutive exercises share the same key
    for _ in range(500):
        if all(a.get("key") is None or a.get("key") != b.get("key") for a, b in zip(seq, seq[1:])): return seq
        rnd.shuffle(seq)
    raise SystemExit("could not avoid adjacent duplicates")

out = []
for lv, (ltitle, units) in C.items():
    rnd = random.Random(lv)
    pool = [w for u in units for l in u[2] for w in l[1]]
    earlier_w1 = []   # words taught in level 1 of earlier lessons of this level
    U = []
    for ui, (utitle, color, lessons) in enumerate(units):
        L = []
        for li, (title, words, phrases) in enumerate(lessons):
            n = len(words); k = max(4, round(n * 0.6))
            W1, W2 = words[:k], words[k:]
            # Level 1: learn W1 in chunks, each chunk followed by easy mc on it; then a short mixed review
            l1 = []
            for c in range(0, len(W1), 2):
                ch = W1[c:c + 2]
                l1 += [learn(w) for w in ch]
                tests = [mc(w, pool, rnd, to_val=False) for w in ch]; rnd.shuffle(tests); l1 += tests
            last = {w[0] for w in W1[-2:]} if len(W1) % 2 == 0 else {W1[-1][0]}
            first = [w for w in W1 if w[0] not in last]
            rev = rnd.sample(first, min(2, len(first)))
            rest = [w for w in W1 if w not in rev]
            while len(l1) + len(rev) < 12 and rest: rev.append(rest.pop(rnd.randrange(len(rest))))
            revx = [mc(w, pool, rnd, to_val=True) for w in rev]
            revx = [revx[0]] + no_adjacent(revx[1:], rnd) if len(revx) > 1 else revx
            l1 += revx
            # Level 2: new vocab (W2) + phrases taught, then match pairs and word order
            l2 = []
            for w in W2: l2 += [learn(w)]
            l2tests = [mc(w, pool, rnd, to_val=True) for w in W2]
            p2 = phrases[:max(2, len(phrases) - 1)]; p3 = phrases[len(p2):]
            for p in p2: l2.append(learn(p, "Frase nueva"))
            m1 = pick_pairs(rnd.sample(words, len(words)) + earlier_w1[::-1], rnd)
            l2tests += [match(m1, rnd)] + [order(p, pool, rnd) for p in p2]
            if len(words) >= 8: l2tests.append(match(pick_pairs(rnd.sample(words, len(words)), rnd), rnd))
            l2tests += [mc(w, pool, rnd, to_val=True) for w in rnd.sample(W1, 2)]
            extra = rnd.sample(words, len(words))
            while len(l2) + len(l2tests) < 12 and extra: l2tests.append(mc(extra.pop(), pool, rnd, to_val=False))
            rnd.shuffle(l2tests); l2 += no_adjacent(l2tests, rnd)
            # Level 3: mostly typing in both directions + harder recall
            l3 = [learn(p, "Frase nueva") for p in p3]
            l3tests = [type_phrase(p) for p in p3]
            byshort = sorted(words, key=lambda w: len(w[0]))
            l3tests += [type_val(w) for w in byshort[:min(6, n)]]
            es_ok = [w for w in words if len(w[1]) <= 22 and not w[1][:1].isupper()]
            l3tests += [type_es(w) for w in rnd.sample(es_ok, min(3, len(es_ok)))]
            l3tests += [type_phrase(rnd.choice(p2)), order(rnd.choice(p2), pool, rnd), match(pick_pairs(rnd.sample(words, len(words)) + earlier_w1, rnd), rnd)]
            extra = [w for w in words if w not in byshort[:6]]
            while len(l3) + len(l3tests) < 12 and extra: l3tests.append(type_val(extra.pop(rnd.randrange(len(extra)))))
            rnd.shuffle(l3tests); l3 += no_adjacent(l3tests, rnd)
            L.append({"id": f"{lv.lower()}-{ui+1}-{li+1}", "title": title, "xp": 10, "levels": [l1, l2, l3]})
            earlier_w1 += W1
        U.append({"title": utitle, "color": color, "lessons": L})
    out.append({"id": lv, "title": ltitle, "units": U})
open(sys.argv[1], "w").write("// Generado por tools/build.py desde tools/content.py\nconst COURSE = " + json.dumps(out, ensure_ascii=False, separators=(",", ":")) + ";\nif (typeof module !== 'undefined') module.exports = COURSE;\n")
