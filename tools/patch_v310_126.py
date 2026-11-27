# V310.126 · NOËL, DÉCOR PROGRESSIF (commande 27/11 13h55 : « décor progressif dès le 1/12 ») : dès le 4 décembre, chaque réverbère de la ville porte ses lumières de Noël
# (une couronne de 3 points rouge, vert et or qui scintillent doucement) · un seul objet pour toute la ville (un nuage de points), aucune lumière ajoutée · s'ajoute au sapin (1/12), aux cadeaux (8/12) et à la neige (20/12)
import re, sys
p = "index.html"; s = open(p, encoding="utf-8").read(); n = 0
def rep(a, b):
    global s, n
    if s.count(a) != 1: sys.exit("REFUS %d : %s" % (s.count(a), a[:90]))
    s = s.replace(a, b); n += 1
rep("function xmasSnowInit() {",
    "function xmasLamps() { XM.lampsDone = true; const L = lampPos.filter(q => Math.abs(q[0]) < HALF + 40 && Math.abs(q[2]) < HALF + 40); if (!L.length) return; const N = L.length * 3, pos = new Float32Array(N * 3), col = new Float32Array(N * 3), C = [[1, 0.18, 0.3], [0.25, 1, 0.45], [1, 0.82, 0.35]];\n"
    "  L.forEach((q, i) => { for (let k = 0; k < 3; k++) { const a = k * 2.094 + i, j = (i * 3 + k) * 3; pos[j] = q[0] - 0.6 + Math.cos(a) * 0.32; pos[j + 1] = q[1] - 2.6 + k * 0.55; pos[j + 2] = q[2] + Math.sin(a) * 0.32; col[j] = C[k][0]; col[j + 1] = C[k][1]; col[j + 2] = C[k][2]; } });\n"
    "  const g = new THREE.BufferGeometry(); g.setAttribute(\"position\", new THREE.BufferAttribute(pos, 3)); g.setAttribute(\"color\", new THREE.BufferAttribute(col, 3)); g.computeBoundingSphere();\n"
    "  XM.lamps = new THREE.Points(g, new THREE.PointsMaterial({ size: 1.3, map: (() => { const c = document.createElement(\"canvas\"); c.width = c.height = 32; const x = c.getContext(\"2d\"), gr = x.createRadialGradient(16, 16, 1, 16, 16, 15); gr.addColorStop(0, \"rgba(255,255,255,1)\"); gr.addColorStop(0.35, \"rgba(255,255,255,0.9)\"); gr.addColorStop(1, \"rgba(255,255,255,0)\"); x.fillStyle = gr; x.fillRect(0, 0, 32, 32); return new THREE.CanvasTexture(c); })(), vertexColors: true, transparent: true, opacity: 1, depthWrite: false })); XM.lamps.frustumCulled = false; scene.add(XM.lamps); stat(\"noel-reverberes\"); }\n"
    "function xmasSnowInit() {")
rep("if (XM.star) XM.star.material.opacity = 0.75 + 0.25 * Math.sin(T * 3);",
    "if (XM.star) XM.star.material.opacity = 0.75 + 0.25 * Math.sin(T * 3); if (XM.day >= 4 && !XM.lampsDone) { try { xmasLamps(); } catch (e) { XM.lampsDone = true; } } if (XM.lamps) { XM.lamps.visible = !G.inside; XM.lamps.material.opacity = 0.75 + 0.25 * Math.sin(T * 1.7); }")
open(p, "w", encoding="utf-8").write(s)
w = "sw.js"; ws = open(w, encoding="utf-8").read(); ws2 = re.sub(r"const V = 'constancy-\d+';", "const V = 'constancy-202611272300';", ws, count=1); assert ws2 != ws; open(w, "w", encoding="utf-8").write(ws2)
print("OK", n, "remplacements")
