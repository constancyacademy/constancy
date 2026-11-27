# V310.106 · CARTE 3D DE NUIT SUR ORDINATEUR (Thomas 27/11 17h00, capture : « de nuit, sur ordinateur… la carte réapparaît en jour ») + plus de « Tu es à… » par-dessus la carte
import re, sys
p = "index.html"; s = open(p, encoding="utf-8").read(); n = 0
def rep(a, b):
    global s, n
    if s.count(a) != 1: sys.exit("REFUS %d : %s" % (s.count(a), a[:90]))
    s = s.replace(a, b); n += 1
A = "hemi.color.setRGB(1, 0.97 - nightK * 0.36, 0.95 - nightK * 0.03); hemi.groundColor.setRGB(0.23 + nightK * 0.27, 0.16 + nightK * 0.09, 0.23 + nightK * 0.32);"
rep(A, A + ' if (G.map3d && nightK > 0.2) { /* V310.106 (Thomas, 27/11 17h00 : « de nuit, sur ordinateur, la carte réapparaît en jour ») : dans le jeu, la nuit vient surtout du brouillard violet, que la carte repousse au loin · sur la carte, la lumière elle-même passe en nuit bleue, la ville et ses lumières restent allumées */ const q = clamp((nightK - 0.2) / 0.5, 0, 1); hemi.intensity *= 1 - 0.5 * q; sun.intensity *= 1 - 0.55 * q; hemi.color.lerp(M3NC || (M3NC = new THREE.Color(0.5, 0.56, 1)), 0.55 * q); }')
rep("function satNight(g, x0, z0, w, px) {", "let M3NC = null;\nfunction satNight(g, x0, z0, w, px) {")
rep('function updateZoneTitle(dt) { if (G.mode !== "play" || DREAM.on) return;', 'function updateZoneTitle(dt) { if (G.map3d && ZT.el && ZT.el.style.opacity !== "0") { ZT.el.style.opacity = 0; document.body.classList.remove("zton"); } if (G.mode !== "play" || DREAM.on || G.map3d) return; /* V310.106 (capture de Thomas 17h00 : « Tu es à La Plage » par-dessus la carte 3D) */')
rep('g.fillStyle = TOUCH_DEV() ? "rgb(118,96,168)" : "rgb(150,160,215)";', 'g.fillStyle = TOUCH_DEV() ? "rgb(118,96,168)" : "rgb(80,86,155)"; /* V310.106 (Thomas, 27/11 17h00 : sur ordinateur, la carte dézoomée de nuit paraissait en plein jour) : teinte de nuit plus profonde, les lumières dessinées par-dessus ressortent */')
open(p, "w", encoding="utf-8").write(s)
w = "sw.js"; ws = open(w, encoding="utf-8").read(); ws2 = re.sub(r"const V = 'constancy-\d+';", "const V = 'constancy-202611271710';", ws, count=1); assert ws2 != ws; open(w, "w", encoding="utf-8").write(ws2)
print("OK", n, "remplacements")
