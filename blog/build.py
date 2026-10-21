#!/usr/bin/env python3
"""Genera el blog estático: blog/posts/*.md -> blog/<slug>.html + blog/index.html + /sitemap.xml.
Sin dependencias. Uso:  python3 blog/build.py

Formato de un post (cabecera entre líneas ---):
    ---
    title: Título del post
    description: Meta descripción (140-160 caracteres)
    slug: url-del-post            (opcional; por defecto, el nombre del archivo)
    date: 2026-10-21
    updated: 2026-10-21           (opcional)
    ---
    Texto en markdown: ## y ### títulos, párrafos, listas con - o 1., tablas con |,
    **negrita**, *cursiva*, [enlaces](/ruta). Una línea con solo [[cta]] inserta la caja de llamada a la acción.
"""
import html, json, pathlib, re, datetime
BASE = "https://diusialvalencia.com"
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent

def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", lambda m: f'<a href="{m.group(2)}">{m.group(1)}</a>', t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", t)
    return t

CTA = ('<aside class="cta"><img src="/app/mascot/cheer.png" width="72" height="72" alt="">'
       '<div><p><strong>Practica esto gratis en Diu sí al valencià.</strong> Lecciones cortas, audio con acento valenciano y rachas diarias. Sin cuenta y sin anuncios.</p>'
       '<a class="btn sm" href="/app/">Empieza a aprender</a></div></aside>')

def md(src):
    out, lines, i = [], src.strip("\n").split("\n"), 0
    while i < len(lines):
        l = lines[i]
        if not l.strip(): i += 1; continue
        if l.strip() == "[[cta]]": out.append(CTA); i += 1; continue
        m = re.match(r"(#{2,4}) (.+)", l)
        if m:
            n = len(m.group(1)); txt = m.group(2)
            anchor = re.sub(r"[^a-z0-9]+", "-", txt.lower().translate(str.maketrans("áéíóúàèòïüçñ·¿?¡!", "aeiouaeoiucn     "))).strip("-")
            out.append(f'<h{n} id="{anchor}">{inline(txt)}</h{n}>'); i += 1; continue
        if l.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-+:?", c) for c in cells): rows.append(cells)
                i += 1
            h = "".join(f"<th>{inline(c)}</th>" for c in rows[0])
            b = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in rows[1:])
            out.append(f"<table><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>"); continue
        m = re.match(r"(- |\d+\. )", l)
        if m:
            tag = "ul" if l.startswith("- ") else "ol"; items = []
            while i < len(lines) and re.match(r"(- |\d+\. )", lines[i]):
                items.append(re.sub(r"^(- |\d+\. )", "", lines[i])); i += 1
            out.append(f"<{tag}>" + "".join(f"<li>{inline(x)}</li>" for x in items) + f"</{tag}>"); continue
        para = []
        while i < len(lines) and lines[i].strip() and not re.match(r"(#{2,4} |\||- |\d+\. |\[\[cta\]\])", lines[i]):
            para.append(lines[i].strip()); i += 1
        out.append(f"<p>{inline(' '.join(para))}</p>")
    return "\n".join(out)

def parse(p):
    raw = p.read_text(encoding="utf-8")
    _, head, body = raw.split("---\n", 2)
    meta = dict(re.match(r"(\w+):\s*(.*)", x).groups() for x in head.strip().split("\n"))
    meta.setdefault("slug", p.stem); meta.setdefault("updated", meta["date"])
    meta["body"] = body; meta["words"] = len(re.findall(r"\w+", re.sub(r"[#|*\[\]()\-]", " ", body)))
    return meta

def page(title, desc, url, body, ld, og_type="website"):
    t, d = html.escape(title), html.escape(desc)
    return f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t}</title>
<meta name="description" content="{d}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#58cc02">
<link rel="icon" href="/app/icon-192.png"><link rel="apple-touch-icon" href="/app/icon-180.png">
<meta property="og:type" content="{og_type}"><meta property="og:locale" content="es_ES"><meta property="og:site_name" content="Diu sí al valencià">
<meta property="og:title" content="{t}"><meta property="og:description" content="{d}"><meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}/assets/og-image.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{t}"><meta name="twitter:description" content="{d}"><meta name="twitter:image" content="{BASE}/assets/og-image.png">
<link rel="stylesheet" href="/assets/site.css">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
<header class="nav"><a class="brand" href="/"><img src="/app/icon-192.png" width="36" height="36" alt="">Diu sí al valencià</a><nav><a href="/blog/">Blog</a><a class="btn sm" href="/app/">Empezar</a></nav></header>
<main>
{body}
</main>
<footer><div class="wrap">
<p><b>Diu sí al valencià</b> · herramienta gratuita para aprender valenciano</p>
<p><a href="/">Inicio</a><a href="/app/">App</a><a href="/blog/">Blog</a><a href="/privacy.html">Privacidad</a><a href="mailto:soporte@diusialvalencia.com">soporte@diusialvalencia.com</a></p>
</div></footer>
</body>
</html>
'''

def fdate(s):
    y, m, d = map(int, s.split("-"))
    return f"{d} de {['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre'][m-1]} de {y}"

def main():
    posts = sorted((parse(p) for p in (HERE / "posts").glob("*.md")), key=lambda x: (x["date"], x["title"]), reverse=True)
    for p in posts:
        url = f"{BASE}/blog/{p['slug']}.html"
        others = [o for o in posts if o is not p]
        rel = "".join(f'<li><a href="/blog/{o["slug"]}.html">{html.escape(o["title"])}</a></li>' for o in others)
        ld = {"@context": "https://schema.org", "@type": "Article", "headline": p["title"], "description": p["description"],
              "inLanguage": "es", "datePublished": p["date"], "dateModified": p["updated"], "image": f"{BASE}/assets/og-image.png",
              "mainEntityOfPage": url, "author": {"@type": "Organization", "name": "Diu sí al valencià", "url": BASE + "/"},
              "publisher": {"@type": "Organization", "name": "Diu sí al valencià", "logo": {"@type": "ImageObject", "url": f"{BASE}/app/icon-512.png"}}}
        body = (f'<article class="post"><p class="crumb"><a href="/">Inicio</a> › <a href="/blog/">Blog</a></p>'
                f'<h1>{html.escape(p["title"])}</h1><p class="meta">Publicado el {fdate(p["date"])}</p>\n{md(p["body"])}\n{CTA}'
                f'<h2>Sigue leyendo</h2><ul>{rel}</ul></article>')
        (HERE / f"{p['slug']}.html").write_text(page(p["title"] + " | Diu sí al valencià", p["description"], url, body, ld, "article"), encoding="utf-8")
        print(f"{p['slug']}.html  {p['words']} palabras")
    items = "".join(f'<li><a class="t" href="/blog/{p["slug"]}.html">{html.escape(p["title"])}</a><p>{html.escape(p["description"])}</p></li>' for p in posts)
    body = ('<div class="post"><h1>Blog para aprender valenciano</h1><p>Guías gratuitas en castellano para aprender valenciano: vocabulario, gramática básica y consejos para empezar desde cero.</p>'
            f'<ul class="list">{items}</ul>{CTA}</div>')
    ld = {"@context": "https://schema.org", "@type": "Blog", "name": "Blog de Diu sí al valencià", "url": f"{BASE}/blog/", "inLanguage": "es",
          "blogPost": [{"@type": "BlogPosting", "headline": p["title"], "url": f"{BASE}/blog/{p['slug']}.html", "datePublished": p["date"]} for p in posts]}
    (HERE / "index.html").write_text(page("Blog para aprender valenciano gratis | Diu sí al valencià",
        "Guías gratuitas para aprender valenciano: frases básicas, saludos, números, días y meses, y consejos para empezar desde cero.", f"{BASE}/blog/", body, ld), encoding="utf-8")
    today = datetime.date.today().isoformat()
    urls = [(f"{BASE}/", today), (f"{BASE}/app/", today), (f"{BASE}/blog/", today), (f"{BASE}/privacy.html", None)] + [(f"{BASE}/blog/{p['slug']}.html", p["updated"]) for p in posts]
    sm = "".join(f"<url><loc>{u}</loc>" + (f"<lastmod>{d}</lastmod>" if d else "") + "</url>\n" for u, d in urls)
    (ROOT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{sm}</urlset>\n', encoding="utf-8")
    print("index.html + sitemap.xml")

if __name__ == "__main__":
    main()
