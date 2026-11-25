const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => { const page = path.resolve(process.argv[2]), save = JSON.parse(fs.readFileSync(process.argv[3], 'utf8')), out = process.argv[4]; fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch({ args: ['--allow-file-access-from-files', '--use-gl=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--mute-audio'] });
  const ctx = await b.newContext({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true, deviceScaleFactor: 1 });
  await ctx.route(/^https?:/, r => r.abort());
  await ctx.addInitScript(s => { window.__farDebug = 1; Object.defineProperty(Navigator.prototype, 'webdriver', { get: () => false }); try { if (!sessionStorage.getItem('lx')) { for (const k in s) localStorage.setItem(k, s[k]); sessionStorage.setItem('lx', '1'); } } catch (e) {} }, save);
  const res = {};
  for (const por of ['itch', 'cg', 'y8']) {
    const p = await ctx.newPage(); const errs = []; p.on('pageerror', e => errs.push(e.message.slice(0, 160)));
    await p.goto('file://' + page + '?nostat=1&autostart=1&accueil=1&portail=' + por);
    await p.waitForSelector('#cont', { timeout: 900000 }); const r = {};
    r.titre = await p.evaluate(() => ({ login: !!document.getElementById('tlogin2') || !!document.getElementById('tlogin'), portail: window.__T().PORTAL }));
    await p.evaluate(() => document.getElementById('cont').click());
    for (let k = 0; k < 240; k++) { await p.waitForTimeout(1000); const m = await p.evaluate(() => window.__W().G.mode); if (m === 'play') break; const w = await p.evaluate(() => { const b = document.getElementById('wgo') || document.querySelector('#screen .btn'); if (b && window.__W().G.mode !== 'play') { b.click(); return 1; } return 0; }); }
    await p.waitForTimeout(3000);
    r.menu = await p.evaluate(async () => { const T = window.__T(); T.openMenu(); await new Promise(o => setTimeout(o, 400)); const o = { keep: !!document.getElementById('keepM'), save: !!document.getElementById('saveM'), txt: /constancy\.fr/.test(document.getElementById('screen').innerText) }; window.__W().resume(); return o; });
    r.tel = await p.evaluate(async () => { const T = window.__T(); T.openPhone(); await new Promise(o => setTimeout(o, 400)); const o = { share: !!document.querySelector('[data-app="share"]'), apps: [...document.querySelectorAll('[data-app]')].map(b => b.dataset.app).join(',') }; window.__W().resume(); return o; });
    r.rdv = await p.evaluate(async () => { window.__T().rdvCard(); await new Promise(o => setTimeout(o, 500)); const c = document.querySelector('.rdvc'); const o = { keep: !!document.getElementById('rdvKeep'), share: !!document.getElementById('rdvShare'), txt: c ? c.innerText.replace(/\s+/g, ' ').slice(0, 160) : null }; return o; });
    if (por === 'itch') { await p.screenshot({ path: out + '/rdv_itch.png' }); r.url = await p.evaluate(() => { const u = window.__T().portalSaveURL(); const b = u.split('#partie=')[1]; const j = JSON.parse(decodeURIComponent(escape(atob(b.replace(/-/g, '+').replace(/_/g, '/') + '==='.slice((b.length + 3) % 4))))); return { debut: u.slice(0, 40), long: u.length, jour: j.day, cash: j.cash }; }); res.lien = r.url; }
    r.carte7 = await p.evaluate(async () => { const T = window.__T(); if (T.portalKeepCard) T.portalKeepCard('jeu'); await new Promise(o => setTimeout(o, 500)); const c = document.querySelector('.pkeep'); return c ? c.innerText.replace(/\s+/g, ' ').slice(0, 120) : null; });
    r.finJour1 = await p.evaluate(async () => { const T = window.__T(), W = window.__W(); T.gateFn(); await new Promise(o => setTimeout(o, 600)); const sc = document.getElementById('screen'); const o = { mode: W.G.mode, garder: !!document.getElementById('pgGo'), insta: !!document.getElementById('fIg'), txt: sc ? sc.innerText.replace(/\s+/g, ' ').slice(0, 100) : '' }; return o; });
    r.liens = await p.evaluate(() => [...document.querySelectorAll('a[href^="http"]')].map(a => a.href).slice(0, 5));
    r.err = errs; res[por] = r; await p.close(); }
  // import sur constancy.fr (sans portail, appareil vierge)
  { const ctx2 = await b.newContext({ viewport: { width: 390, height: 844 } }); await ctx2.route(/^https?:/, r => r.abort()); const p = await ctx2.newPage();
    const u = res.lien ? null : null; const lien = await (async () => { return null; })();
    await p.goto('file://' + page + '?nostat=1&autostart=1&accueil=1&s=itch' + '#partie=' + Buffer.from(JSON.stringify({ v: 2, acct: 1, objective: 'cash', muscle: 'bras', day: 3, cash: 23456, earned: 30000, cars: ['citadine', 'coupe'], car: 'coupe' })).toString('base64').replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, ''));
    await p.waitForSelector('#cont', { timeout: 900000 }); res.import = await p.evaluate(() => ({ bouton: document.getElementById('cont').innerText, hash: location.hash, flag: window.__partieImport })); await ctx2.close(); }
  console.log(JSON.stringify(res, null, 1)); await b.close(); })();
