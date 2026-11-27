# V310.97 · POKI : SDK Poki v2 + rien de lourd chargé avant le premier toucher (exigence Poki : moins de 8 Mo avant de jouer)
# Porte pk seulement. constancy.fr et les autres portes identiques. Usage : python3 tools/patch_v310_97.py
import os, re
R = os.getcwd(); p = os.path.join(R, "index.html"); s = open(p, encoding="utf-8").read(); n = 0
def rep(a, b):
    global s, n
    if s.count(a) != 1: raise SystemExit("REFUS : %d fois : %s" % (s.count(a), a[:90]))
    s = s.replace(a, b); n += 1
# 1. SDK Poki chargé sur la porte pk
rep('(function () { try { if (PORTAL !== "cg" && PORTAL !== "pg") return;',
    '/* V310.97 · Poki (commande BUSINESS 26/11 20h58 : « Poki prêt le 27/11 ») : SDK Poki v2 sur la porte pk · gameLoadingFinished quand l\'écran « Play » est prêt, gameplayStart et gameplayStop comme les autres plateformes · aucune pub */\n'
    '(function () { try { if (PORTAL !== "pk") return; const sc = document.createElement("script"); sc.async = true; sc.src = "https://game-cdn.poki.com/scripts/v2/poki-sdk.js"; sc.onload = () => { try { window.PokiSDK.init().then(() => { PSDK.pk = window.PokiSDK; window.__pkSDK = 1; try { if (window.__pkTitle) PSDK.pk.gameLoadingFinished(); } catch (e) {} }).catch(() => { PSDK.pk = window.PokiSDK; }); } catch (e) {} }; sc.onerror = () => {}; document.head.appendChild(sc); } catch (e) {} })();\n'
    '(function () { try { if (PORTAL !== "cg" && PORTAL !== "pg") return;')
rep('function psdkTick() { if (!PORTAL || (!PSDK.cg && !PSDK.pg)) return;',
    'function psdkTick() { if (PSDK.pk) { const on = G.mode === "play" && !document.hidden; if (on !== PSDK.pkPlay) { PSDK.pkPlay = on; try { on ? PSDK.pk.gameplayStart() : PSDK.pk.gameplayStop(); } catch (e) {} } } if (!PORTAL || (!PSDK.cg && !PSDK.pg)) return;')
# 2. rien de lourd avant le premier toucher sur Poki : écran « Play » léger, puis la ville se charge (écran de chargement animé)
rep('const mediaP = loadMedia(DLD); if (DLD) mediaP.then(() => { try { loadHumans(); } catch (e) {} });',
    '/* V310.97 · Poki : la ville, les modèles et les sons ne partent qu\'après le premier toucher sur l\'écran « Play » (moins de 8 Mo avant de jouer) */\n'
    '  const PKH = (PORTAL === "pk" && !CREATOR) ? new Promise(ok => { window.__pkWait = 1; const d = document.createElement("div"); d.id = "pkTitle"; d.style.cssText = "position:fixed;inset:0;z-index:2147483600;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px;background:radial-gradient(circle at 50% 38%,#3b1166 0%,#14062a 62%,#08020f 100%);color:#fff;font-family:\'EB Garamond\',Georgia,serif;cursor:pointer;-webkit-tap-highlight-color:transparent"; d.innerHTML = `<div style="font-size:clamp(48px,11vw,96px);letter-spacing:.01em;text-shadow:0 0 30px rgba(255,45,149,.55)">Constancy</div><div style="font:600 13px Inter,system-ui,sans-serif;letter-spacing:.32em;color:#ff8fd0">FREE OPEN-WORLD CITY</div><button type="button" style="margin-top:18px;border:0;border-radius:999px;padding:16px 46px;font:800 20px Inter,system-ui,sans-serif;color:#14062a;background:linear-gradient(90deg,#ff2d95,#ffb3dd);box-shadow:0 10px 40px rgba(255,45,149,.45);cursor:pointer">▶ PLAY</button><div style="font:500 12px Inter,system-ui,sans-serif;opacity:.6">Drive, deliver, buy your dream car.</div>`; const put = () => { if (document.body) { document.body.appendChild(d); window.__pkTitle = 1; stat("pk-titre"); try { PSDK.pk && PSDK.pk.gameLoadingFinished(); } catch (e) {} } else setTimeout(put, 30); }; put(); const go = e => { if (go.d) return; go.d = 1; try { e && e.preventDefault && e.preventDefault(); } catch (er) {} try { audioInit(); } catch (er) {} window.__pkWait = 0; window.__pkT = Date.now(); stat("pk-play"); d.style.transition = "opacity .35s"; d.style.opacity = "0"; setTimeout(() => d.remove(), 380); ok(); }; d.addEventListener("click", go); d.addEventListener("touchend", go); addEventListener("keydown", go, { once: true }); }) : Promise.resolve();\n'
    '  const mediaP = PKH.then(() => loadMedia(DLD)); if (DLD) mediaP.then(() => { try { loadHumans(); } catch (e) {} });')
rep('const built = Promise.all([DLD ? Promise.resolve(false) : loadHumans(), mediaP, fontsReady])',
    'const built = PKH.then(() => Promise.all([DLD ? Promise.resolve(false) : loadHumans(), mediaP, fontsReady]))')
# 3. l'écran de chargement compte depuis le toucher sur Poki, et ne se retire jamais pendant l'attente du toucher
rep('fake = Math.min(.95, (Date.now() - t0) / 25000)', 'fake = window.__pkWait ? 0 : Math.min(.95, (Date.now() - (window.__pkT || t0)) / 25000)')
rep('if (G.mode !== "play" && (real >= .95 || Date.now() - t0 > 45000))', 'if (G.mode !== "play" && !window.__pkWait && (real >= .95 || Date.now() - (window.__pkT || t0) > 45000))')
open(p, "w", encoding="utf-8").write(s)
w = os.path.join(R, "sw.js"); ws = open(w, encoding="utf-8").read(); ws2 = re.sub(r"const V = 'constancy-\d+';", "const V = 'constancy-202611271430';", ws, count=1); assert ws2 != ws; open(w, "w", encoding="utf-8").write(ws2)
print("OK", n, "remplacements")
