# V310.133 · CrazyGames : allège les fichiers du zip (leur outil compte les Mo téléchargés jusqu'au début du jeu)
# - textures intégrées aux modèles (.json = GLB) de plus de 512 px ramenées à 512 px (sauf voitures, vues de près)
# - photos .jpg réenregistrées en qualité 80 (même taille en pixels), gardées seulement si plus légères
# Usage : python3 tools/cg_assets.py <dossier_build>/assets
import sys, os, io, json, struct, glob
from PIL import Image
A = sys.argv[1]; g0 = g1 = j0 = j1 = 0
def pad4(b, c=b"\0"): return b + c * ((4 - len(b) % 4) % 4)
for f in sorted(glob.glob(os.path.join(A, "m_*.json"))):
    k = os.path.basename(f)[2:-5]; b = open(f, "rb").read()
    if b[:4] != b"glTF" or k.startswith("car_"): continue
    jl = struct.unpack("<I", b[12:16])[0]; J = json.loads(b[20:20 + jl]); o = 20 + jl; bl = struct.unpack("<I", b[o:o + 4])[0]; BIN = b[o + 8:o + 8 + bl]
    imgs = {im["bufferView"]: im for im in J.get("images", []) if "bufferView" in im}; ch = False; new = {}
    for vi, im in imgs.items():
        v = J["bufferViews"][vi]; d = BIN[v.get("byteOffset", 0):v.get("byteOffset", 0) + v["byteLength"]]
        try: I = Image.open(io.BytesIO(d)); I.load()
        except Exception: continue
        if max(I.size) <= 512: continue
        sc = 512 / max(I.size); I2 = I.resize((max(1, round(I.size[0] * sc)), max(1, round(I.size[1] * sc))), Image.LANCZOS); out = io.BytesIO()
        if im.get("mimeType") == "image/png": I2.save(out, "PNG", optimize=True)
        else: I2.convert("RGB").save(out, "JPEG", quality=82, optimize=True)
        if len(out.getvalue()) < len(d): new[vi] = out.getvalue(); ch = True
    if not ch or any(v.get("buffer", 0) != 0 for v in J["bufferViews"]): continue
    nb = b""
    for vi, v in enumerate(J["bufferViews"]):
        d = new.get(vi) or BIN[v.get("byteOffset", 0):v.get("byteOffset", 0) + v["byteLength"]]
        nb = pad4(nb); v["byteOffset"] = len(nb); v["byteLength"] = len(d); nb += d
    nb = pad4(nb); J["buffers"][0]["byteLength"] = len(nb); js = pad4(json.dumps(J, separators=(",", ":")).encode(), b" ")
    out = b"glTF" + struct.pack("<II", 2, 12 + 8 + len(js) + 8 + len(nb)) + struct.pack("<I", len(js)) + b"JSON" + js + struct.pack("<I", len(nb)) + b"BIN\0" + nb
    g0 += len(b); g1 += len(out); open(f, "wb").write(out)
for f in sorted(glob.glob(os.path.join(A, "*.jpg"))):
    b = open(f, "rb").read()
    try: I = Image.open(io.BytesIO(b)); I.load()
    except Exception: continue
    out = io.BytesIO(); I.convert("RGB").save(out, "JPEG", quality=80, optimize=True, progressive=True)
    if len(out.getvalue()) < len(b) * 0.95: j0 += len(b); j1 += len(out.getvalue()); open(f, "wb").write(out.getvalue())
print("modèles %.2f → %.2f Mo · photos %.2f → %.2f Mo" % (g0 / 1e6, g1 / 1e6, j0 / 1e6, j1 / 1e6))
