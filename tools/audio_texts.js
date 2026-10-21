// Collects every Valencian string that the app can speak -> stdout JSON [{text,key,h}]
const fs = require("fs"), path = require("path"), R = p => fs.readFileSync(path.join(__dirname, "..", p), "utf8");
eval(R("lessons.js").replace("const COURSE", "global.COURSE"));
const akey = t => String(t).toLowerCase().normalize("NFC").replace(/[’]/g, "'").replace(/[¿¡!?.,;:«»"()…]/g, " ").replace(/\s+/g, " ").trim();
const fnv = s => { let h = 0x811c9dc5; for (const b of Buffer.from(s, "utf8")) { h ^= b; h = Math.imul(h, 0x01000193) >>> 0; } return h.toString(16).padStart(8, "0"); };
const out = new Map(), add = t => { if (!t) return; const k = akey(t); if (k && !out.has(k)) out.set(k, { text: String(t).trim(), key: k, h: fnv(k) }); };
for (const l of COURSE) for (const u of l.units) for (const s of u.lessons) for (const lv of s.levels) for (const e of lv) {
  if (e.type === "learn") add(e.word);
  if (e.type === "mc" || e.type === "type" || e.type === "order") add(e.key);
  if (e.type === "match") e.pairs.forEach(p => add(p[0]));
}
for (const v of Object.values(JSON.parse(R("phrases.json")))) add(v);
const hs = new Set([...out.values()].map(x => x.h)); if (hs.size !== out.size) throw "hash collision";
process.stdout.write(JSON.stringify([...out.values()]));
