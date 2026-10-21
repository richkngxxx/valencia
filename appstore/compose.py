"""Composes App Store screenshots from raw captures (/tmp/raw/*.png, 1320x2868 from 440x956@3x).
Needs /tmp/nunito900.ttf (fontTools: woff2 -> ttf from ../fonts/nunito-900.woff2)."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
RAW = "/tmp/raw"; FONT = "/tmp/nunito900.ttf"
SHOTS = [("1-path", "Aprende valenciano\npaso a paso"),
         ("2-learn", "Escucha la pronunciación\nvalenciana"),
         ("3-mc", "Ejercicios cortos\ny entretenidos"),
         ("4-match", "Une parejas y repasa\nvocabulario"),
         ("5-correct", "Celebra cada acierto\ncon el murciélago"),
         ("6-ask", "¿Cómo se dice…?\nPregunta y aprende")]
SIZES = {"6.9": (1320, 2868), "6.5": (1284, 2778)}
GREEN, DARK = (0x58, 0xCC, 0x02), (0x46, 0xA3, 0x02)
def frame(raw, caption, W, H):
    bg = Image.new("RGB", (W, H), GREEN)
    g = ImageDraw.Draw(bg)
    for y in range(H):  # gentle vertical gradient
        t = y / H; g.line([(0, y), (W, y)], fill=tuple(int(GREEN[i] * (1 - t * .35) + DARK[i] * t * .35) for i in range(3)))
    sw = int(W * 0.82); sh = round(sw * raw.height / raw.width)
    top = H - sh - int(H * 0.035)
    shot = raw.resize((sw, sh), Image.LANCZOS)
    r = int(sw * 0.07)
    mask = Image.new("L", (sw, sh), 0); ImageDraw.Draw(mask).rounded_rectangle([0, 0, sw - 1, sh - 1], r, fill=255)
    sh_l = Image.new("L", (W, H), 0); ImageDraw.Draw(sh_l).rounded_rectangle([(W - sw) // 2, top + 18, (W + sw) // 2, top + sh + 18], r, fill=110)
    sh_l = sh_l.filter(ImageFilter.GaussianBlur(28))
    bg = Image.composite(Image.new("RGB", (W, H), (30, 70, 0)), bg, sh_l)
    border = Image.new("RGB", (sw + 16, sh + 16), (255, 255, 255)); bm = Image.new("L", border.size, 0)
    ImageDraw.Draw(bm).rounded_rectangle([0, 0, sw + 15, sh + 15], r + 8, fill=255)
    bg.paste(border, ((W - sw) // 2 - 8, top - 8), bm)
    bg.paste(shot, ((W - sw) // 2, top), mask)
    d = ImageDraw.Draw(bg); size = int(W * 0.078)
    f = ImageFont.truetype(FONT, size)
    while max(d.textlength(l, font=f) for l in caption.split("\n")) > W * 0.9: size -= 4; f = ImageFont.truetype(FONT, size)
    bb = d.multiline_textbbox((0, 0), caption, font=f, spacing=int(size * .18), align="center")
    tx = (W - (bb[2] - bb[0])) / 2 - bb[0]; ty = (top - 8 - (bb[3] - bb[1])) / 2 - bb[1]
    d.multiline_text((tx, ty + 6), caption, font=f, fill=(55, 120, 0), spacing=int(size * .18), align="center")
    d.multiline_text((tx, ty), caption, font=f, fill=(255, 255, 255), spacing=int(size * .18), align="center")
    return bg.convert("RGB")
out = []
for k, (W, H) in SIZES.items():
    os.makedirs(f"screenshots/{k}", exist_ok=True)
    for i, (n, cap) in enumerate(SHOTS, 1):
        im = frame(Image.open(f"{RAW}/{n}.png").convert("RGB"), cap, W, H)
        p = f"screenshots/{k}/{i:02d}-{n.split('-',1)[1]}.png"; im.save(p, optimize=True); out.append(p)
# contact sheet
th = [Image.open(p) for p in out]; tw = 330
rows = []
for k in SIZES:
    rows.append([Image.open(p).resize((tw, round(tw * Image.open(p).height / Image.open(p).width))) for p in out if f"/{k}/" in p])
rh = max(im.height for r in rows for im in r)
sheet = Image.new("RGB", (len(rows[0]) * (tw + 20) + 20, len(rows) * (rh + 70) + 20), (240, 244, 248))
d = ImageDraw.Draw(sheet); lf = ImageFont.truetype(FONT, 30)
for ri, (k, r) in enumerate(zip(SIZES, rows)):
    y = 20 + ri * (rh + 70); d.text((20, y), f'{k}" · {SIZES[k][0]}x{SIZES[k][1]}', font=lf, fill=(60, 60, 60))
    for ci, im in enumerate(r): sheet.paste(im, (20 + ci * (tw + 20), y + 50))
sheet.save("screenshots/contact-sheet.png", optimize=True)
for p in out:
    im = Image.open(p); assert im.mode == "RGB" and im.size == SIZES[p.split("/")[1]], (p, im.mode, im.size)
print("\n".join(out))
