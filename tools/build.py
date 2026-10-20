import json, random, re, sys
sys.path.insert(0, __file__.rsplit('/',1)[0]); from content import C
cap = lambda s: s[:1].upper()+s[1:]
out=[]
for lv,(ltitle,units) in C.items():
    rnd=random.Random(lv); pool=[w for u in units for l in u[2] for w in l[1]]
    U=[]
    for ui,(utitle,color,lessons) in enumerate(units):
        L=[]
        for li,(title,words,phrases) in enumerate(lessons):
            ex=[]
            for w in words: ex.append({"type":"learn","word":cap(w[0]),"meaning":w[1],**({"note":w[2]} if len(w)>2 else {})})
            for p in phrases: ex.append({"type":"learn","label":"Frase nueva","word":p[0],"meaning":p[1],**({"note":p[2]} if len(p)>2 else {})})
            for i,w in enumerate(words):
                others=[x for x in pool if x[0]!=w[0] and x[1]!=w[1]]
                d=rnd.sample(others,3)
                if i%2==0: q,a,opts=f"¿Qué significa «{w[0]}»?",w[1],[x[1] for x in d]
                else: q,a,opts=f"¿Cómo se dice «{w[1]}»?",w[0],[x[0] for x in d]
                opts=opts+[a]; rnd.shuffle(opts)
                ex.append({"type":"mc","question":q,"options":opts,"answer":a,"explanation":f"{w[0]} = {w[1]}."})
            for w in sorted(words,key=lambda w:len(w[0]))[:2]:
                acc=[w[0]]+(w[3] if len(w)>3 else [])
                ex.append({"type":"type","question":f"Escribe en valenciano: «{w[1]}»","answer":w[0],"accept":acc,"explanation":f"{w[1]} = {w[0]}."})
            for p in phrases:
                toks=p[0].split(); prev=[t for x in pool for t in x[0].split() if t.lower() not in [y.lower().strip('.,?!') for y in toks]]
                ex.append({"type":"order","question":f"Traduce: «{p[1]}»","answer":p[0],"words":toks,"distractors":rnd.sample(sorted(set(prev)),3)})
            L.append({"id":f"{lv.lower()}-{ui+1}-{li+1}","title":title,"xp":10,"exercises":ex})
        U.append({"title":utitle,"color":color,"lessons":L})
    out.append({"id":lv,"title":ltitle,"units":U})
open(sys.argv[1],"w").write("// Generado por tools/build.py desde tools/content.py\nconst COURSE = "+json.dumps(out,ensure_ascii=False,indent=0)+";\nif (typeof module !== 'undefined') module.exports = COURSE;\n")
