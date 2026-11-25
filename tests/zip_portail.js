// Lance un zip de plateforme servi en local (comme dans l'iframe de la plateforme) : node zip_portail.js <dossier du zip décompressé> <port> <capture.png>
// Vérifie : le jeu démarre sans rien charger d'internet (three.js embarqué), la porte du zip, aucun mur de mail, les erreurs
const { chromium } = require('playwright'); const { spawn } = require('child_process');
(async () => { const dir = process.argv[2], port = +process.argv[3] || 8765, shot = process.argv[4] || '/tmp/zip.png';
  const srv = spawn('python3', ['-m', 'http.server', String(port), '--bind', '127.0.0.1'], { cwd: dir, stdio: 'ignore' }); await new Promise(r => setTimeout(r, 1500));
  const b = await chromium.launch({ args: ['--use-gl=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--mute-audio'] });
  const ctx = await b.newContext({ viewport: { width: 800, height: 450 }, deviceScaleFactor: 1 }); const ext = [];
  await ctx.route(/^https?:/, r => { const u = r.request().url(); if (u.startsWith('http://127.0.0.1:' + port)) return r.continue(); ext.push(u.split('?')[0].slice(0, 80)); return r.abort(); });
  await ctx.addInitScript(() => { Object.defineProperty(Navigator.prototype, 'webdriver', { get: () => false }); });
  const p = await ctx.newPage(); const errs = []; p.on('pageerror', e => errs.push(e.message.slice(0, 160)));
  const t0 = Date.now(); await p.goto('http://127.0.0.1:' + port + '/index.html?nostat=1');
  let st = null; for (let k = 0; k < 400; k++) { await p.waitForTimeout(1500); st = await p.evaluate(() => { try { const W = window.__W && window.__W(); const q = document.getElementById('quick'); if (q && q.offsetParent && !window.__qc) { window.__qc = 1; q.click(); } const b2 = document.querySelector('.boot'); if (b2 && b2.offsetParent && !window.__bc) { window.__bc = 1; b2.click(); } const ok = document.getElementById('ok'); if (ok && ok.offsetParent && !window.__okc) { window.__okc = 1; setTimeout(() => ok.click(), 300); } const ch = document.querySelector('.choice, .objc button, [data-obj]'); if (ch && ch.offsetParent && !window.__chc) { window.__chc = 1; setTimeout(() => ch.click(), 300); } return { mode: W && W.G.mode, portail: window.__PORTAL, em: !!document.getElementById('em'), three: typeof THREE !== 'undefined' && THREE.REVISION }; } catch (e) { return { err: e.message }; } }); if (st.em) break; if (st.mode === 'play' && k > 10) break; }
  await p.waitForTimeout(4000); await p.screenshot({ path: shot });
  const fin = await p.evaluate(() => ({ mode: window.__W().G.mode, mur: !!document.getElementById('em'), stats: (window.__stats || []).filter(s => /portail|ecran-email|partie-lancee|arrivee-|perso-cree$/.test(s)).join(' ') }));
  console.log(JSON.stringify({ secondes: Math.round((Date.now() - t0) / 1000), st, fin, externes: [...new Set(ext)], erreurs: errs }, null, 1)); await b.close(); srv.kill(); })();
