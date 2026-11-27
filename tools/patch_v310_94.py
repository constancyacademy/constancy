# V310.94 · Playgama Bridge v2.4.4 (commande BUSINESS 26/11 15h58 et 20h55, publication Playgama bloquée sans « jeu prêt »)
# Usage, depuis la racine du dépôt : python3 tools/patch_v310_94.py   (prérequis : npm, accès au registre npm)
# Fait : 1. playgama-bridge.js (v2.4.4, npm @playgama/bridge) + playgama-bridge-config.json à la racine
#        2. porte pg : Bridge local v2.4.4, secours CDN v2 · « jeu prêt » par la constante du SDK + progression 100 %
#        3. sauvegarde écrite aussi par bridge.storage (au plus toutes les 15 s, et à la mise en arrière-plan), relue au démarrage si le stockage local est vide
#        4. tools/mkportail.py copie les 2 fichiers dans le zip Playgama · sw.js nouvelle version
# Ne touche à rien hors de la porte pg (constancy.fr, itch, ng, gj, y8, cg, pk identiques).
import os, re, subprocess, shutil, tempfile, json, sys
R = os.getcwd(); assert os.path.exists(os.path.join(R, "index.html")), "lancer depuis la racine du dépôt"
t = tempfile.mkdtemp()
subprocess.check_call(["npm", "pack", "@playgama/bridge@2.4.4"], cwd=t, stdout=subprocess.DEVNULL)
subprocess.check_call(["tar", "xzf", "playgama-bridge-2.4.4.tgz"], cwd=t)
pk = json.load(open(os.path.join(t, "package/package.json"))); assert pk["version"] == "2.4.4"
shutil.copy(os.path.join(t, "package/dist/playgama-bridge.js"), os.path.join(R, "playgama-bridge.js"))
json.dump({"loadingScreenType": "none", "game": {"adaptToSafeArea": False}}, open(os.path.join(R, "playgama-bridge-config.json"), "w"), indent=4)
p = os.path.join(R, "index.html"); s = open(p, encoding="utf-8").read(); n = 0
def rep(a, b):
    global s, n
    assert s.count(a) == 1, ("introuvable ou en double", a[:90]); s = s.replace(a, b); n += 1
# 1. chargement du Bridge v2.4.4 (local d'abord, CDN v2 en secours)
rep('sc.src = PORTAL === "cg" ? "https://sdk.crazygames.com/crazygames-sdk-v3.js" : "https://bridge.playgama.com/v1/stable/playgama-bridge.js";',
    'sc.src = PORTAL === "cg" ? "https://sdk.crazygames.com/crazygames-sdk-v3.js" : "playgama-bridge.js"; /* V310.94 : Bridge v2.4.4 embarqué à côté d\'index.html (+ playgama-bridge-config.json), CDN v2 en secours */')
rep("sc.onerror = () => {}; document.head.appendChild(sc);",
    'sc.onerror = () => { try { if (PORTAL === "pg" && !sc.__v2) { sc.__v2 = 1; const s2 = document.createElement("script"); s2.async = true; s2.src = "https://bridge.playgama.com/v2/stable/playgama-bridge.js"; s2.onload = sc.onload; s2.onerror = () => {}; document.head.appendChild(s2); } } catch (e) {} }; document.head.appendChild(sc);')
# 2. après l'initialisation : partie relue par bridge.storage si le stockage local est vide
rep("window.bridge.initialize().then(() => { PSDK.pg = window.bridge; }).catch(() => {});",
    'window.bridge.initialize().then(() => { PSDK.pg = window.bridge; window.__pgBridge = (window.bridge.version || "?"); try { if (!localStorage.getItem(SAVE_KEY) && !sessionStorage.getItem("cst-pgr")) PSDK.pg.storage.get("cst-partie", false).then(v => { try { if (v && typeof v === "object") v = JSON.stringify(v); if (typeof v !== "string" || v.length < 20 || localStorage.getItem(SAVE_KEY)) return; const d = JSON.parse(v); if (!d || !d.day) return; localStorage.setItem(SAVE_KEY, v); sessionStorage.setItem("cst-pgr", "1"); window.__pgRestore = 1; location.reload(); } catch (e) {} }).catch(() => {}); } catch (e) {} }).catch(() => {});')
# 3. « jeu prêt » par la constante du SDK v2, progression du chargement à 100 %, envoi de la sauvegarde au plus toutes les 15 s
rep('try { PSDK.pg && PSDK.pg.platform.sendMessage("game_ready"); } catch (e) {} }',
    'try { if (PSDK.pg) { try { PSDK.pg.setGameLoadingProgress && PSDK.pg.setGameLoadingProgress(100); } catch (e) {} PSDK.pg.platform.sendMessage((PSDK.pg.PLATFORM_MESSAGE && PSDK.pg.PLATFORM_MESSAGE.GAME_READY) || "game_ready"); window.__pgReady = Date.now(); } } catch (e) {} }\n  if (PSDK.pg && PSDK.pgLast && PSDK.pgLast !== PSDK.pgSent && Date.now() - (PSDK.pgT || 0) > 15000) pgFlush();')
rep("const ADS_ON = false, PSDK = { cg: null, pg: null, play: false, ready: false };",
    'const ADS_ON = false, PSDK = { cg: null, pg: null, play: false, ready: false };\n/* V310.94 · Playgama : la partie est aussi gardée par bridge.storage (exigé par leur outil de test), jamais plus d\'une écriture toutes les 15 s, et tout de suite quand la page passe en arrière-plan */\nfunction pgFlush() { try { if (!PSDK.pg || !PSDK.pgLast || PSDK.pgLast === PSDK.pgSent) return; PSDK.pgT = Date.now(); const v = PSDK.pgLast; PSDK.pg.storage.set("cst-partie", v).then(() => { PSDK.pgSent = v; window.__pgSaved = (window.__pgSaved || 0) + 1; }).catch(() => {}); } catch (e) {} }\nif (PORTAL === "pg") document.addEventListener("visibilitychange", () => { if (document.hidden) pgFlush(); });')
rep("try { localStorage.setItem(SAVE_KEY, JSON.stringify(d)); } catch (e) {} }, // pas d'adresse, pas de sauvegarde",
    "try { const js = JSON.stringify(d); localStorage.setItem(SAVE_KEY, js); if (PORTAL === \"pg\") PSDK.pgLast = js; } catch (e) {} }, // pas d'adresse, pas de sauvegarde · V310.94 : copie pour bridge.storage sur Playgama")
open(p, "w", encoding="utf-8").write(s)
# 4. zip Playgama : les 2 fichiers à côté d'index.html
m = os.path.join(R, "tools/mkportail.py"); ms = open(m, encoding="utf-8").read()
a = 'for sub_ in ["assets", "icons"]: shutil.copytree(os.path.join(REPO, sub_), os.path.join(d, sub_))'
assert ms.count(a) == 1
ms = ms.replace(a, a + '\nif por == "pg":  # V310.94 : Playgama Bridge v2.4.4 et son fichier de réglages, à côté d\'index.html\n    for f_ in ["playgama-bridge.js", "playgama-bridge-config.json"]: shutil.copy(os.path.join(REPO, f_), os.path.join(d, f_))')
open(m, "w", encoding="utf-8").write(ms)
w = os.path.join(R, "sw.js"); ws = open(w, encoding="utf-8").read(); ws2 = re.sub(r"const V = 'constancy-\d+';", "const V = 'constancy-202611270930';", ws, count=1); assert ws2 != ws; open(w, "w", encoding="utf-8").write(ws2)
print("OK", n, "remplacements · playgama-bridge.js", os.path.getsize(os.path.join(R, "playgama-bridge.js")), "octets · config, mkportail.py, sw.js")
