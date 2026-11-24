// Usage : node tests/son_cache.js <page-test.html> <save.json>
// Thomas 24/11 10h34 : « le son continue après avoir fermé la page Safari » · page cachée = plus aucun son ; retour = le son reprend
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => { const page = path.resolve(process.argv[2]), save = JSON.parse(fs.readFileSync(process.argv[3], 'utf8'));
  const b = await chromium.launch({ args: ['--allow-file-access-from-files', '--use-gl=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--autoplay-policy=no-user-gesture-required'] });
  const ctx = await b.newContext({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true });
  await ctx.route(/^https?:/, r => r.abort());
  await ctx.addInitScript(s => { Object.defineProperty(Navigator.prototype, 'webdriver', { get: () => false }); window.__norender = 1; let vs = 'visible'; Object.defineProperty(Document.prototype, 'visibilityState', { get: () => vs, configurable: true }); Object.defineProperty(Document.prototype, 'hidden', { get: () => vs === 'hidden', configurable: true }); window.__setVis = v => { vs = v; document.dispatchEvent(new Event('visibilitychange')); }; try { if (!sessionStorage.getItem('lx')) { for (const k in s) localStorage.setItem(k, s[k]); sessionStorage.setItem('lx', '1'); } } catch (e) {} }, save);
  const p = await ctx.newPage(); const errs = []; p.on('pageerror', e => errs.push(e.message.slice(0, 200)));
  await p.goto('file://' + page + '?nostat=1&autostart=1');
  for (let k = 0; k < 200; k++) { await p.waitForTimeout(1000); const st = await p.evaluate(() => { try { const G = window.__W().G; const c = document.getElementById('cont'); if (c && c.getClientRects().length && !window.__lxc) { window.__lxc = 1; setTimeout(() => c.click(), 10); } const w = document.getElementById('wgo'); if (w) w.click(); return G.mode; } catch (e) { return 'x'; } }); if (/^(play|guide)/.test(st) && k > 3) break; }
  await p.mouse.click(200, 400); await p.waitForTimeout(1500);
  const r = await p.evaluate(async () => { const out = {}; const a = new Audio('assets/amb_city.mp3'); a.loop = true; await a.play().catch(e => out.playErr = String(e)); await new Promise(ok => setTimeout(ok, 800));
    const ctxA = window.__W && window.__W().SND ? window.__W().SND.ctx : null; out.avant = { audio: a.paused ? 'arrêté' : 'joue' };
    window.__setVis('hidden'); window.dispatchEvent(new Event('pagehide')); await new Promise(ok => setTimeout(ok, 600));
    out.cache = { audio: a.paused ? 'arrêté' : 'joue', joueurs: [...document.querySelectorAll('audio,video')].length };
    const b2 = new Audio('assets/amb_gull.mp3'); await b2.play().catch(() => {}); await new Promise(ok => setTimeout(ok, 300)); out.cache.nouveauSon = b2.paused ? 'bloqué' : 'joue';
    window.__setVis('visible'); await new Promise(ok => setTimeout(ok, 900)); out.retour = { audio: a.paused ? 'arrêté' : 'joue', nouveauSon: b2.paused ? 'arrêté' : 'joue' }; a.pause(); b2.pause(); return out; });
  console.log(JSON.stringify(r));
  const ok = r.avant.audio === 'joue' && r.cache.audio === 'arrêté' && r.cache.nouveauSon === 'bloqué' && r.retour.audio === 'joue';
  console.log(ok ? 'SON OK : coupé quand la page est cachée, repris au retour' : 'SON À CORRIGER');
  console.log('ERR', errs.slice(0, 3).join(' | ') || 'none'); await b.close(); })().catch(e => { console.log('ERREUR', e.message.slice(0, 300)); process.exit(1); });
