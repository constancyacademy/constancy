#!/bin/bash
# Installe la chaîne de montage Constancy. Usage : bash outils/installer.sh (depuis la racine de la branche rushes)
set -e
R=$(cd "$(dirname "$0")/.." && pwd)
M=$HOME/monteur; mkdir -p $M/src $M/out /tmp/fnt
cp $R/outils/fnt/*.ttf /tmp/fnt/
cp -r $R/outils/mus $M/mus; cp -r $R/outils/cov $M/cov; mkdir -p $M/cov/out
sed -e "s#/home/claude/src/#$M/src/#" -e "s#/home/claude/r7/#$M/#g" -e "s#/home/claude/mus/#$M/mus/#g" $R/outils/render2.py > $M/render2.py
for f in $R/specs/*.json; do sed -e "s#/home/claude/mus/#$M/mus/#g" "$f" > $M/$(basename "$f"); done
# Rushes : chaque fichier rushes/JJ-MM/<nom>.mp4 devient $M/src/t_<nom>.mp4
for f in $R/rushes/*/*.mp4; do [ -e "$f" ] && ln -sf "$f" "$M/src/t_$(basename "$f")"; done
pip install --break-system-packages -q pillow numpy 2>/dev/null || true
which ffmpeg >/dev/null || (apt-get install -y -q ffmpeg >/dev/null 2>&1 || true)
fc-list | grep -qi NotoColorEmoji || (apt-get install -y -q fonts-noto-color-emoji >/dev/null 2>&1 || true)
echo "Monteur prêt dans $M : python3 $M/render2.py $M/spec_X.json  ·  sorties dans $M/out  ·  miniature : cd $M/cov && python3 make.py jobs.json (sortie dans $M/cov/out)"
