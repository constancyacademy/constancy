#!/bin/bash
# Installe la chaîne de montage Constancy. Usage : bash outils/installer.sh (depuis la racine de la branche rushes)
R=$(cd "$(dirname "$0")/.." && pwd)
# 1. VERROU : Une seule session du monteur à la fois (Thomas, 20/11). Sans verrou, rien n'est installé.
bash "$R/outils/verrou.sh" prendre; V=$?
[ $V -eq 0 ] || exit $V
set -e
M=$HOME/monteur; mkdir -p $M/src $M/out /tmp/fnt
cp $R/outils/fnt/*.ttf /tmp/fnt/
cp -r $R/outils/mus $M/mus; cp -r $R/outils/cov $M/cov; mkdir -p $M/cov/out
{ echo "import subprocess as _sp; _sp.run(['bash','$R/outils/verrou.sh','rafraichir'])"; sed -e "s#/home/claude/src/#$M/src/#" -e "s#/home/claude/r7/#$M/#g" -e "s#/home/claude/mus/#$M/mus/#g" $R/outils/render2.py; } > $M/render2.py
printf '#!/bin/bash\nbash %s/outils/verrou.sh rendre\n' "$R" > $M/rendre.sh; chmod +x $M/rendre.sh
for f in $R/specs/*.json; do sed -e "s#/home/claude/mus/#$M/mus/#g" "$f" > $M/$(basename "$f"); done
# Rushes : chaque fichier rushes/JJ-MM/<nom>.mp4 devient $M/src/t_<nom>.mp4
for f in $R/rushes/*/*.mp4; do [ -e "$f" ] && ln -sf "$f" "$M/src/t_$(basename "$f")"; done
pip install --break-system-packages -q pillow numpy 2>/dev/null || true
which ffmpeg >/dev/null || (apt-get install -y -q ffmpeg >/dev/null 2>&1 || true)
fc-list | grep -qi NotoColorEmoji || (apt-get install -y -q fonts-noto-color-emoji >/dev/null 2>&1 || true)
echo "RUSHES : Tu les filmes TOI-MÊME dans le jeu (outils/capture/LISEZMOI.txt : cap.js, capd.js). Ne demande pas de rushes à la conversation jeu, sauf si un décor n'existe pas encore dans le jeu."
echo "FIN DE SESSION OBLIGATOIRE : bash $M/rendre.sh (libère le verrou). S'il refuse, traite d'abord les messages en file qu'il affiche."
echo "Monteur prêt dans $M : python3 $M/render2.py $M/spec_X.json  ·  sorties dans $M/out  ·  miniature : cd $M/cov && python3 make.py jobs.json (sortie dans $M/cov/out)"
