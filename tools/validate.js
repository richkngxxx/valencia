const COURSE = require('../lessons.js');
const norm = t => t.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g,'').replace(/[.,!?¿¡«»]/g,'').trim();
const toks = s => norm(s).split(/[\s'’-]+/).filter(Boolean);
let taught = new Set(), errors = [], ids = new Set(), stats = {};
for (const lv of COURSE) { stats[lv.id] = {units: lv.units.length, lessons: 0, items: 0, types: {}};
 for (const u of lv.units) for (const l of u.lessons) {
  if (ids.has(l.id)) errors.push('dup id '+l.id); ids.add(l.id);
  stats[lv.id].lessons++; stats[lv.id].items += l.exercises.length;
  if (l.exercises.length < 8) errors.push(l.id+': fewer than 8 items');
  l.exercises.forEach((e, i) => { const where = `${l.id}#${i}`; stats[lv.id].types[e.type] = (stats[lv.id].types[e.type]||0)+1;
   if (e.type === 'learn') { toks(e.word).forEach(t => taught.add(t)); return; }
   const need = (s) => toks(s).filter(t => !taught.has(t) && !/^\d+$/.test(t)).forEach(t => errors.push(`${where}: "${t}" tested before taught (${s})`));
   if (e.type === 'mc') {
     if (!e.options.includes(e.answer)) errors.push(where+': answer not in options');
     if (new Set(e.options.map(norm)).size !== e.options.length) errors.push(where+': duplicate options');
     const m = e.question.match(/«(.+)»/); if (/Qué significa/.test(e.question)) need(m[1]); else need(e.answer);
   } else if (e.type === 'type') { need(e.answer);
   } else if (e.type === 'order') { need(e.answer);
     if (e.words.join(' ') !== e.answer) errors.push(where+': words do not rebuild answer');
     e.distractors.forEach(d => { if (e.words.map(norm).includes(norm(d))) errors.push(where+': distractor equals answer token '+d); });
   } else errors.push(where+': unknown type '+e.type);
  });
 }}
console.log(JSON.stringify(stats));
console.log(errors.length ? errors.join('\n') : 'VALIDATION OK: 0 errors'); process.exit(errors.length ? 1 : 0);
