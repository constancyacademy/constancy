# V310.127 · PONT DE LA VOIE RAPIDE DU MONT (R1, R2 · Thomas 27/11 17h10, capture : la GT orange plantée à la verticale contre le parapet d'un pont, route vers le Mont)
# Trouvé dans le code du pont de la voie rapide (de l'avenue centrale jusqu'à la campagne, au-dessus du chenal, parapets à 7,8 m de l'axe) :
#  1. la voiture était retenue à 7,2 m de l'axe (son centre) alors que le parapet commence à 7,6 m : carrosserie dans le parapet, et les roues du côté parapet lisaient le sol HORS du pont (l'eau, 9 m plus bas) → voiture couchée à la verticale
#  2. cette retenue n'existait qu'à partir de 30 m après le début du pont (et 10 m avant la fin) : en entrant en biais depuis la ville, on passait à travers le parapet et on tombait dans l'eau
#  3. chaque image contre le parapet comptait comme un choc (vitesse × 0,02 par seconde) : la voiture s'arrêtait net
# Corrigé : centre de la voiture retenu à 6,4 m (carrosserie contre le parapet, roues toujours sur le tablier), sur tout le pont (4 m après le début jusqu'à 4 m avant la fin),
# et comme sur les tabliers (V310.121) : glisse le long, perte selon l'angle une fois par contact, cap recalé, choc, vibration, secousse · à pied inchangé (7,2 m)
import re, sys
p = "index.html"; s = open(p, encoding="utf-8").read(); n = 0
def rep(a, b):
    global s, n
    if s.count(a) != 1: sys.exit("REFUS %d : %s" % (s.count(a), a[:90]))
    s = s.replace(a, b); n += 1
rep("if (onHighway(o.x, o.z)) { if (o.z < HW.z0 - 30 && o.z > HW.z1 + 10) { const lx = HW.x - 7.2, rx = HW.x + 7.2; if (o.x < lx) { o.x = lx; hit = true; } if (o.x > rx) { o.x = rx; hit = true; } } return hit; }",
    "if (onHighway(o.x, o.z)) { if (o.z < HW.z0 - 4 && o.z > HW.z1 + 4) { const car = o === G.car, lim = car ? 6.4 : 7.2, lx = HW.x - lim, rx = HW.x + lim; if (o.x < lx || o.x > rx) { o.x = o.x < lx ? lx : rx; if (car) railSlide(o, 0, -1); else hit = true; } } return hit; } /* V310.127 : parapets du pont de la voie rapide du Mont, voir railSlide */")
rep("function collide0Terrain(o, swim) {",
    "/* V310.127 · glissière : la voiture glisse le long (tangente tx, tz), perte selon l'angle une seule fois par contact, cap recalé, choc, vibration, secousse · jamais d'arrêt net */\n"
    "function railSlide(c, tx, tz) { const fx = Math.sin(c.h), fz = Math.cos(c.h), dp = fx * tx + fz * tz, sa = Math.sqrt(Math.max(0, 1 - dp * dp)), av = Math.abs(c.v), now = performance.now();\n"
    "  if (!railSlide.t || now - railSlide.t > 700) { if (av > 4) { c.v *= 1 - Math.min(0.5, Math.max(0.02, sa * sa * 0.7)); const k = Math.min(1, av * (0.25 + sa) / 30); try { if (typeof clang === \"function\") clang(Math.max(0.15, k)); } catch (e) {} try { navigator.vibrate && navigator.vibrate(k > 0.5 ? [30, 30, 40] : 25); } catch (e) {} try { shakeAdd(Math.min(0.7, 0.12 + k * 0.6)); } catch (e) {} if (!railSlide.s) { railSlide.s = 1; try { stat(\"parapet-choc\"); } catch (e) {} } } }\n"
    "  railSlide.t = now; if (av > 1 && sa > 0.02) { const sg = (dp * (c.v >= 0 ? 1 : -1)) >= 0 ? 1 : -1, ht = Math.atan2(tx * sg, tz * sg) + (c.v < 0 ? Math.PI : 0); let d = ht - c.h; while (d > Math.PI) d -= 2 * Math.PI; while (d < -Math.PI) d += 2 * Math.PI; c.h += d * Math.min(1, (railSlide.dt || 0.016) * 7); } c.roll = 0; }\n"
    "function collide0Terrain(o, swim) {")
# R3 · parapets : plus de bloc clair uni (rose sous les néons la nuit) · béton gris texturé (grain, joints tous les 4 m) et glissière métallique brillante sur le dessus, sur le pont de la voie rapide du Mont et les ponts de la rivière en ville
rep("function collide0Terrain(o, swim) {",
    "/* V310.127 · parapets en béton (texture dessinée une fois, joints tous les 4 m) et glissière métallique */\n"
    "var PARAP_M = null; function parapetMats() { if (PARAP_M) return PARAP_M; const c = document.createElement(\"canvas\"); c.width = c.height = 128; const g = c.getContext(\"2d\"); g.fillStyle = \"#a9a7a3\"; g.fillRect(0, 0, 128, 128); for (let i = 0; i < 1400; i++) { const v = 140 + Math.random() * 60 | 0; g.fillStyle = `rgba(${v},${v - 2},${v - 6},${0.12 + Math.random() * 0.2})`; g.fillRect(Math.random() * 128, Math.random() * 128, 1 + Math.random() * 2, 1 + Math.random() * 2); }\n"
    "  g.fillStyle = \"rgba(60,58,55,.55)\"; g.fillRect(0, 0, 2, 128); g.fillStyle = \"rgba(255,255,255,.18)\"; g.fillRect(0, 0, 128, 6); g.fillStyle = \"rgba(40,38,36,.25)\"; g.fillRect(0, 118, 128, 10); const t = new THREE.CanvasTexture(c); t.wrapS = t.wrapT = THREE.RepeatWrapping;\n"
    "  PARAP_M = { beton: new THREE.MeshLambertMaterial({ color: 0xffffff, map: t }), metal: new THREE.MeshPhongMaterial({ color: 0xc3c9d0, specular: 0x9aa4ae, shininess: 90 }) }; return PARAP_M; }\n"
    "function collide0Terrain(o, swim) {")
rep("[-1, 1].forEach(sd => addGeo(railM, new THREE.BoxGeometry(0.4, 0.9, 6.4), HW.x + sd * 7.8, mid + 0.45, z - 3, 0, 1, 1, 1, -pitch));",
    "[-1, 1].forEach(sd => { const PM = parapetMats(); addGeo(PM.beton, boxUV(0.4, 0.9, 6.4, 4), HW.x + sd * 7.8, mid + 0.45, z - 3, 0, 1, 1, 1, -pitch); addGeo(PM.metal, new THREE.BoxGeometry(0.5, 0.14, 6.4), HW.x + sd * 7.8, mid + 0.97, z - 3, 0, 1, 1, 1, -pitch); }); /* V310.127 : béton et glissière */")
rep("[-1, 1].forEach(sd => { addGeo(railM, new THREE.BoxGeometry(0.35, 1.1, RZ1 - RZ0), x + sd * (ROAD / 2 - 0.2), 0.55, (RZ0 + RZ1) / 2); for (let z = RZ0 + 2; z < RZ1; z += 4) addGeo(railM, new THREE.BoxGeometry(0.5, 1.2, 0.5), x + sd * (ROAD / 2 - 0.2), 0.5, z); });",
    "[-1, 1].forEach(sd => { const PM = parapetMats(); addGeo(PM.beton, boxUV(0.35, 1.1, RZ1 - RZ0, 4), x + sd * (ROAD / 2 - 0.2), 0.55, (RZ0 + RZ1) / 2); addGeo(PM.metal, new THREE.BoxGeometry(0.45, 0.14, RZ1 - RZ0), x + sd * (ROAD / 2 - 0.2), 1.17, (RZ0 + RZ1) / 2); for (let z = RZ0 + 2; z < RZ1; z += 4) addGeo(PM.beton, boxUV(0.5, 1.2, 0.5, 4), x + sd * (ROAD / 2 - 0.2), 0.5, z); }); /* V310.127 : béton et glissière */")
open(p, "w", encoding="utf-8").write(s)
w = "sw.js"; ws = open(w, encoding="utf-8").read(); ws2 = re.sub(r"const V = 'constancy-\d+';", "const V = 'constancy-202611272330';", ws, count=1); assert ws2 != ws; open(w, "w", encoding="utf-8").write(ws2)
print("OK", n, "remplacements")
