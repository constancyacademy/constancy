// persistent capture daemon: node capd.js jobsdir  (jobs: *.json {out, shots:[...] , w,h}) ; writes <job>.done
const { chromium } = require('playwright'); const fs = require('fs'); const path=require('path');
(async () => { const [,, JD] = process.argv;
  const b = await chromium.launch({ args: ['--allow-file-access-from-files', '--use-gl=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--mute-audio'] });
  const ctx = await b.newContext({ viewport: { width: 1080, height: 1920 } }); const p = await ctx.newPage();
  const VD = process.env.VD; const MAP = {}; for (const l of fs.readFileSync(VD + '/map.txt', 'utf8').trim().split('\n')) { const [u, f] = l.split(' '); MAP[u] = VD + '/' + f; } MAP['https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js'] = VD + '/three.min.js';
  await ctx.route(/^https?:/, r => { const u = r.request().url(); if (MAP[u]) return r.fulfill({ path: MAP[u], contentType: 'application/javascript' }); return r.abort(); });
  await p.addInitScript(() => { const rP = performance.now.bind(performance), rD = Date.now, rRAF = window.requestAnimationFrame.bind(window); let fz = false, vt = 0, q = []; const d0 = rD(), p0 = rP();
    performance.now = () => fz ? vt : rP(); Date.now = () => fz ? Math.round(d0 + (vt - p0)) : rD();
    window.requestAnimationFrame = cb => { if (!fz) return rRAF(cb); q.push(cb); return q.length; };
    window.__freeze = () => { vt = rP(); fz = true; }; window.__unfreeze = () => { fz = false; const c=q; q=[]; for (const f of c) rRAF(f); }; window.__step = ms => { vt += ms; const c = q; q = []; for (const f of c) { try { f(vt); } catch (e) { console.log('STEPERR ' + e.message); } } return c.length; }; });
  p.on('crash',()=>console.log('CRASH renderer'));b.on('disconnected',()=>console.log('BROWSER DISCONNECTED'));p.on('pageerror', e => console.log('PAGEERR', e.message)); p.on('console', m => { const t=m.text(); if (t.startsWith('LOG')) console.log(t); }); const t0 = Date.now();
  await p.goto('file:///home/claude/constancy/index_cap.html?nostat=1', { timeout: 300000 }); await p.waitForSelector('#quick', { timeout: 400000 }); console.log('quick', (Date.now() - t0) / 1000);
  const _iv=setInterval(()=>{p.screenshot({path:'/root/cap/dbg.png',timeout:60000}).catch(()=>{});},20000); await p.click('#quick', { force: true, noWaitAfter: true, timeout: 600000 }); console.log('clicked',(Date.now()-t0)/1000); await p.waitForSelector('#ok, .choice', { timeout: 600000 }); if (await p.$('#ok')) { await p.waitForTimeout(400); await p.evaluate(() => document.getElementById('ok').click()); } console.log('okstep',(Date.now()-t0)/1000); const _ch = await Promise.race([p.waitForSelector('.choice', { timeout: 600000 }).then(()=>1).catch(()=>0), p.waitForFunction(()=>{try{const W=window.__W();return W&&W.G&&W.G.started&&!document.querySelector('#ok');}catch(e){return false;}}, null, {timeout:600000, polling:2000}).then(()=>2).catch(()=>0)]); console.log('choice',_ch,(Date.now()-t0)/1000); if (_ch===1) await p.click('.choice', { force: true, noWaitAfter: true, timeout: 600000 }); await p.waitForTimeout(2500); if (await p.$('#gSkip')) await p.click('#gSkip', { force: true, noWaitAfter: true, timeout: 600000 }); await p.waitForTimeout(500);
  await p.evaluate(() => { const W = window.__W(); if (W.P) { W.P.storyI = 99; } W.G.mission = null; window.__outHome = 1; W.G.inside = false; W.G.intro = null; W.G.afterCar = null; });
  await p.waitForTimeout(3000); await p.addStyleTag({ content: 'body *:not(#game){visibility:hidden!important} #game{visibility:visible!important}' });
  clearInterval(_iv); console.log('READY', (Date.now() - t0) / 1000); fs.writeFileSync(JD + '/READY', '1');
  let frozen=false;
  while (true) {
    const js = fs.readdirSync(JD).filter(f => f.endsWith('.json')).sort();
    if (!js.length) { await new Promise(r => setTimeout(r, 1000)); continue; }
    const jf = JD + '/' + js[0]; let J; try { J = JSON.parse(fs.readFileSync(jf, 'utf8')); } catch (e) { await new Promise(r => setTimeout(r, 500)); continue; }
    fs.renameSync(jf, jf + '.run'); const out = J.out; fs.mkdirSync(out, { recursive: true }); const ts0=Date.now();
    try {
      await p.setViewportSize({ width: J.w || 1080, height: J.h || 1920 });
      if (J.eval) { const r = await p.evaluate(J.eval); fs.writeFileSync(jf + '.res', JSON.stringify(r)); }
      for (const v of (J.shots||[])) {
        if (frozen) { await p.evaluate(() => window.__unfreeze()); frozen=false; }
        await p.evaluate(v => { const W = window.__W(); window.__outHome = 1; W.G.inside = false; W.G.intro = null; W.G.afterCar = null; W.G.mission = null; W.G.started = true; if (W.P) { W.P.day = 2; W.P.nightStart = 0; W.P.dayT = v.dayT || 600; } window.__wx = 0; W.WX.rain = v.rain||0;
          if (v.js) eval(v.js); window.__T0 = null; window.__camK = eval(v.camjs); W.camera.far = Math.max(W.camera.far, v.far || 0); }, v);
        await p.waitForTimeout(v.wait || 4000); await p.evaluate(() => window.__freeze()); frozen=true; await p.evaluate(() => { window.__T0 = performance.now(); });
        const n = v.n || 1;
        for (let i = 0; i < (v.pre || 3); i++) await p.evaluate(fs_ => window.__step(fs_), 1000/(v.fps||30));
        const FS=1000/(v.fps||30); for (let i = 0; i < n; i++) { if (i>0 || true) await p.evaluate(fs_ => window.__step(fs_), FS); if (v.toff && i==0) { for(let k=0;k<Math.round(v.toff*30);k++) await p.evaluate(() => window.__step(1000 / 30)); }
          await p.screenshot({ path: `${out}/${v.name}_${String(i).padStart(3, '0')}.png`, timeout: 240000 }); if (i % 15 == 0) console.log(v.name, i, (Date.now() - ts0) / 1000); }
      }
    } catch (e) { console.log('JOBERR', e.message); fs.writeFileSync(jf + '.err', String(e.stack)); }
    fs.writeFileSync(jf + '.done', String((Date.now()-ts0)/1000)); console.log('done', js[0], (Date.now()-ts0)/1000);
  }
})();
