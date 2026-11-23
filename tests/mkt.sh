# page de test + accès aux fonctions internes (tests/lieux), jamais publié
sh "$(dirname "$0")/mk.sh" "$1" "$2"
python3 - "$2" <<'PY'
import sys
p=sys.argv[1]; s=open(p).read(); a='window.__W = () => ({'
assert s.count(a)==1
s=s.replace(a,'window.__T = () => ({ get traffic() { return traffic; }, openMap3D: typeof openMap3D === "function" ? openMap3D : null, get M3() { return M3; }, titleScreen, hideScreen, nullP() { P = null; }, get P() { return P; }, coupePhone, rdvCard, gpsRoute, updateMe, toggleCar, onPonton, prologueRadio, coupeBuy, coupeGoalOn, addCash, PRADIO, TALKIE, updateCar, collideCar, collideBlocks, collideProps, finishEnter, AP_OLD, leaveApt: typeof leaveApt === "function" ? leaveApt : null, get carMesh() { return carMesh; }, get renderer() { return renderer; }, cullChunks, FREED, freeStatic, get loopCf() { return loop.cf; }, get CSM() { return typeof CSM !== "undefined" ? CSM : null; } });\n'+a)
open(p,'w').write(s)
PY
