# Construit le zip complet d'une plateforme (CrazyGames, Poki, Playgama, Y8…) : python3 tools/mkportail.py index.html <portail> <version>
# Prérequis une fois : cd /tmp && npm pack three@0.128.0 && mkdir -p three128 && tar xzf three-0.128.0.tgz -C three128
# Sortie : /home/claude/work/portails/Constancy · <plateforme> · <version>.zip (index.html à la racine, three.js embarqué, assets/ et icons/ du dépôt)
import sys, os, re, shutil, zipfile
src, por, ver = sys.argv[1], sys.argv[2], sys.argv[3]
NAMES = {"itch": "itch.io", "ng": "Newgrounds", "gj": "Game Jolt", "y8": "Y8", "cg": "CrazyGames", "pk": "Poki", "pg": "Playgama"}
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); T3 = "/tmp/three128/package"; OUT = os.environ.get("OUT", "/home/claude/work/portails"); os.makedirs(OUT, exist_ok=True)
d = os.path.join(OUT, "build_" + por)
shutil.rmtree(d, ignore_errors=True); os.makedirs(d + "/lib")
s = open(src, encoding="utf-8").read()
libs = []
def sub(m):
    url = m.group(1); name = url.rsplit("/", 1)[1]
    if "cdnjs" in url: path = T3 + "/build/three.min.js"
    else: path = T3 + "/" + url.split("three@0.128.0/")[1]
    shutil.copy(path, d + "/lib/" + name); libs.append(name); return 'src="lib/' + name + '"'
s = re.sub(r'src="(https://(?:cdnjs\.cloudflare\.com/ajax/libs/three\.js/r128|cdn\.jsdelivr\.net/npm/three@0\.128\.0)/[^"]+)"', sub, s)
assert len(libs) == 12, libs
s = re.sub(r'<link rel="manifest"[^>]*>\s*', '', s)
s = s.replace("<head>", '<head>\n<script>window.CONSTANCY_PORTAIL = "%s";</script>' % por, 1)
assert 'window.CONSTANCY_PORTAIL = "%s"' % por in s
# V310.88 : le jeu est en anglais sur toutes les plateformes, l'en-tête aussi (description, og, lang)
s = s.replace('<html lang="fr">', '<html lang="en">', 1)
s = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="Constancy: the city where your consistency is the score. Free to play in your browser.">', s, count=1)
s = re.sub(r'<meta property="og:description" content="[^"]*">', '<meta property="og:description" content="The city where your consistency is the score.">', s, count=1)
assert '<html lang="en">' in s and "Free to play" in s
open(d + "/index.html", "w", encoding="utf-8").write(s)
for sub_ in ["assets", "icons"]: shutil.copytree(os.path.join(REPO, sub_), os.path.join(d, sub_))
if por == "cg":  # V310.133 : textures des modèles et photos allégées (leur outil compte les Mo jusqu'au début du jeu)
    import subprocess; print(subprocess.run([sys.executable, os.path.join(REPO, "tools", "cg_assets.py"), os.path.join(d, "assets")], capture_output=True, text=True, check=True).stdout.strip())
if por == "pg":  # V310.94 : Playgama Bridge v2.4.4 et son fichier de réglages, à côté d'index.html
    for f_ in ["playgama-bridge.js", "playgama-bridge-config.json"]: shutil.copy(os.path.join(REPO, f_), os.path.join(d, f_))
z = os.path.join(OUT, "Constancy · %s · %s.zip" % (NAMES[por], ver))
if os.path.exists(z): os.remove(z)
n = 0
with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as zf:
    for root, _, files in os.walk(d):
        for f in files:
            p = os.path.join(root, f); zf.write(p, os.path.relpath(p, d)); n += 1
print(z, n, "fichiers", round(os.path.getsize(z) / 1e6, 1), "Mo")
