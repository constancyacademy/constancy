// V310.132 · Playgama : bouton pub du menu Pause, petit bouton en jeu sans délai en test, « Close (No Reward) » sans récompense, jeu et son qui repartent, textes encore en français
// node tests/pg_pub.js dossier_build_pg sortie_
const { chromium } = require('playwright'); const path = require('path');
(async () => { const dir = path.resolve(process.argv[2]), out = process.argv[3] || '/tmp/pgp_';
  const b = await chromium.launch({ args: ['--allow-file-access-from-files', '--use-gl=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--mute-audio'] });
  const ctx = await b.newContext({ viewport: { width: 1280, height: 720 } }); await ctx.route(/^https?:/, r => r.abort());
  const p = await ctx.newPage(); const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.goto('file://' + dir + '/index.html?nostat=1');
  await p.waitForFunction(() => (window.__stats || []).includes('partie-lancee'), null, { timeout: 900000 }); await p.waitForTimeout(8000);
  const ev = (f, a) => p.evaluate(f, a);
  await p.evaluate(() => { const X = window.__PGT(); for (const k of ["PSDK","plTest","adRewarded","pgAdBtn","G","P","SND","DAILY","notify","stopMenu","resume"]) Object.defineProperty(window, k, { configurable: true, get: () => X[k] }); });
  console.log('PLATEFORME', await ev(() => { try { return String(PSDK.pg && PSDK.pg.platform && PSDK.pg.platform.id) + ' test=' + plTest(); } catch (e) { return 'x ' + e.message; } }));
  // fausse régie : on joue la séquence de Playgama
  await ev(() => { window.__seq = 'ok'; bridge.advertisement.on = (e, fn) => { if (e === 'rewarded_state_changed') window.__rsc = fn; }; bridge.advertisement.showRewarded = () => { const f = window.__rsc, sq = window.__seq === 'ok' ? ['opened', 'rewarded', 'closed'] : ['opened', 'closed']; window.__modeAd = null; window.__log = []; sq.forEach((st, i) => setTimeout(() => { f(st); window.__log.push(st + ':' + G.mode + '|' + (SND.ctx ? SND.ctx.state : '-')); if (st === 'opened') window.__modeAd = G.mode + '|' + (SND.ctx ? SND.ctx.state : '-'); }, 500 + i * 900)); }; adRewarded.on = 0; });
  const etat = () => ev(() => JSON.stringify({ mode: G.mode, cash: P.cash, son: SND.ctx ? SND.ctx.state : '-', ecran: !document.getElementById('screen').classList.contains('hidden'), help: ((document.getElementById('help') || {}).innerText || '').slice(0, 60), petit: (() => { const x = document.getElementById('pgAd'); return x ? x.style.display !== 'none' : 'absent'; })(), pendantPub: window.__modeAd, log: (window.__log || []).join(' ') }));
  const fin = () => p.waitForFunction(() => !pgAdBtn.busy && G.mode === 'play' && (window.__log || []).some(x => /^closed/.test(x)) && !adRewarded.pz, null, { timeout: 60000 }).then(() => p.waitForTimeout(1500)).catch(() => console.log('  (pas fini en 60 s)'));
  await ev(() => { G.mission = null; document.getElementById('menuBtn').click(); }); await p.waitForTimeout(1200); await p.screenshot({ path: out + 'pause.png' });
  console.log('MENU', await ev(() => { const x = document.getElementById('pgAdM'); return x ? x.innerText + ' · à côté de : ' + (x.previousElementSibling || {}).innerText : 'ABSENT'; }));
  const c0 = await ev(() => P.cash); await ev(() => document.getElementById('pgAdM').click()); await fin();
  console.log('PUB REGARDEE', await etat(), 'gain', (await ev(() => P.cash)) - c0);
  await p.waitForTimeout(4000); console.log('PETIT BOUTON JUSTE APRES', await etat());
  await ev(() => { window.__seq = 'ko'; }); const c1 = await ev(() => P.cash); await ev(() => document.getElementById('pgAd').click()); await fin();
  console.log('CLOSE NO REWARD', await etat(), 'gain', (await ev(() => P.cash)) - c1);
  await p.waitForTimeout(2500); await ev(() => { document.getElementById('menuBtn').click(); }); await p.waitForTimeout(800);
  await ev(() => { window.__seq = 'ok'; }); const c2 = await ev(() => P.cash); await ev(() => document.getElementById('pgAdM').click()); await fin();
  console.log('2E PUB DU MENU', await etat(), 'gain', (await ev(() => P.cash)) - c2);
  // en mission : pas de bouton
  await ev(() => { G.mission = { k: 'test' }; }); await p.waitForTimeout(2500); console.log('EN MISSION petit bouton', await ev(() => { const x = document.getElementById('pgAd'); return x ? x.style.display !== 'none' : 'absent'; })); await ev(() => { document.getElementById('menuBtn').click(); }); await p.waitForTimeout(800); console.log('EN MISSION menu', await ev(() => !!document.getElementById('pgAdM'))); await ev(() => { G.mission = null; resume(); });
  // textes : écran « Quit game » et défis du jour
  const m0 = await ev(() => window.__i18nMiss().length);
  await ev(() => stopMenu()); await p.waitForTimeout(800); await p.screenshot({ path: out + 'quit.png' });
  console.log('QUIT', JSON.stringify(await ev(() => document.querySelector('#screen .panel').innerText.replace(/\s+/g, ' '))));
  await ev(() => resume());
  for (let i = 0; i < 6; i++) { await ev(i => { const D = DAILY[i]; notify('info', `<b>Défi du jour · ${D.t}.</b> <span>${D.d}</span> <span>Il change chaque jour. 7 jours d'affilée = gros bonus.</span>`, 8); notify('gold', `<b>Défi du jour réussi.</b> ${D.w} <b style="color:var(--cash)">+$250</b>`, 8); }, i); await p.waitForTimeout(400); }
  await p.waitForTimeout(600); await p.screenshot({ path: out + 'defi.png' });
  const fr = await ev(() => { const t = document.body.innerText; return t.split('\n').filter(l => /(Défi du jour|chaque jour|Réussis|Arrête-toi|Fais |Roule|cartons|d'affilée)/.test(l)).slice(0, 12); });
  console.log('LIGNES FR RESTANTES', JSON.stringify(fr));
  console.log('MANQUES', JSON.stringify(await ev(m0 => window.__i18nMiss().slice(m0), m0)));
  console.log('ERR', errs.length ? errs.slice(0, 3).join(' | ') : 'none'); await b.close(); })();
