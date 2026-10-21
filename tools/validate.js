// Content validator: run with `node tools/validate.js`
// Rule: a word may only be tested (type/order/match/mc answer in Valencian) after it was taught.
// Taught set for lesson N, level k = level-1 learn cards of all earlier lessons (the next node unlocks
// after level 1) + learn cards of lesson N's levels 1..k seen before the exercise.
const COURSE = require('../app/lessons.js');
const norm = t => t.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '').replace(/[.,!?¿¡«»;:]/g, '').trim();
const toks = s => norm(s).split(/[\s'’-]+/).filter(Boolean);
const errors = [], ids = new Set(), stats = {};
let base = new Set();                        // taught by level 1 of earlier lessons
for (const lv of COURSE) {
  const st = stats[lv.id] = { units: lv.units.length, lessons: 0, items: 0, perLevel: [0, 0, 0], types: {} };
  for (const u of lv.units) for (const l of u.lessons) {
    if (ids.has(l.id)) errors.push('dup id ' + l.id); ids.add(l.id);
    st.lessons++;
    if (!Array.isArray(l.levels) || l.levels.length !== 3) { errors.push(l.id + ': needs 3 levels'); continue; }
    const taught = new Set(base);
    l.levels.forEach((exs, k) => {
      st.items += exs.length; st.perLevel[k] += exs.length;
      if (exs.length < 8 || exs.length > 20) errors.push(`${l.id} L${k + 1}: ${exs.length} items (want ~12–15)`);
      if (k > 0 && exs.filter(e => e.type === 'learn').length > 8) errors.push(`${l.id} L${k + 1}: too many learn cards`);
      exs.forEach((e, i) => {
        const where = `${l.id} L${k + 1}#${i}`;
        st.types[e.type] = (st.types[e.type] || 0) + 1;
        if (i > 0 && e.key && exs[i - 1].key === e.key) errors.push(where + ': back-to-back duplicate ' + e.key);
        if (e.type === 'learn') { toks(e.word).forEach(t => taught.add(t)); if (k === 0) toks(e.word).forEach(t => l._b = (l._b || []).concat(t)); return; }
        const need = s => toks(s).filter(t => !taught.has(t) && !/^\d+$/.test(t)).forEach(t => errors.push(`${where}: "${t}" tested before taught (${s})`));
        if (e.type === 'mc') {
          if (!e.options.includes(e.answer)) errors.push(where + ': answer not in options');
          if (new Set(e.options.map(norm)).size !== e.options.length) errors.push(where + ': duplicate options');
          const m = e.question.match(/«(.+)»/); if (/Qué significa/.test(e.question)) need(m[1]); else need(e.answer);
        } else if (e.type === 'type') {
          if (e.lang === 'es') need(e.question.match(/«(.+)»/)[1]); else need(e.answer);
          if (!(e.accept || []).map(norm).includes(norm(e.answer))) errors.push(where + ': answer not in accept list');
        } else if (e.type === 'order') {
          need(e.answer);
          if (e.words.join(' ') !== e.answer) errors.push(where + ': words do not rebuild answer');
          e.distractors.forEach(d => { if (e.words.map(norm).includes(norm(d))) errors.push(where + ': distractor equals answer token ' + d); });
        } else if (e.type === 'match') {
          if (e.pairs.length < 4) errors.push(where + ': fewer than 4 pairs');
          const v = e.pairs.map(p => norm(p[0])), s = e.pairs.map(p => norm(p[1]));
          if (new Set(v).size !== v.length || new Set(s).size !== s.length) errors.push(where + ': duplicate pair sides');
          e.pairs.forEach(p => need(p[0]));
        } else errors.push(where + ': unknown type ' + e.type);
      });
    });
    (l._b || []).forEach(t => base.add(t)); delete l._b;
  }
}
console.log(JSON.stringify(stats, null, 1));
console.log(errors.length ? errors.slice(0, 60).join('\n') + `\n${errors.length} ERRORS` : 'VALIDATION OK: 0 errors');
process.exit(errors.length ? 1 : 0);
