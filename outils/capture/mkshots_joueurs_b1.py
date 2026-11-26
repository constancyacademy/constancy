# joueurs_b1 (sam. 28/11 17h, M3 DEUX ÉCRANS · COMPTEUR « +50 joueurs. Et toi, t'attends quoi ? ») · bas 1080 × 960 au coucher du soleil : coupé néon au ras du sol sur la route de la plage, grande roue depuis le canal, guinguette de la plage
import os
exec(open('/root/cap/lib212.py').read())
DT=int(os.environ.get("DT","690"))
UNFPV="{const W6=window.__W();W6.G.fpv=false;W6.G.mode='play';}"
HB="{const W6=window.__W();if(!window.__HB){window.__HB=1;const H=o=>{if(o&&o.isObject3D)Object.defineProperty(o,'visible',{configurable:true,get:()=>false,set:()=>{}});};const B=W6.BANNER;if(B){H(B.g);H(B.plane);H(B.cloth);}}}"
CP=("{const W9=window.__W();if(!window.__CP){const g=W9.makeCar(W9.CARS.find(c=>c.id=='coupe'));W9.scene.add(g);window.__CP=g;}"
 "W9.scene.traverse(o=>{if(o.userData&&o.userData.isCar&&o!==window.__CP&&!o.__hid&&!(W9.SHOWROOM&&W9.SHOWROOM.includes&&W9.SHOWROOM.includes(o))){o.__hid=1;Object.defineProperty(o,'visible',{configurable:true,get:()=>false,set:()=>{}});}});"
 "delete window.__CP.visible;window.__CP.visible=%s;window.__lt=null;}")
GV="{const W8=window.__W();W8.GUING.people.forEach(h=>{if(!h.__gv&&Math.abs(h.position.x+422)<40){h.__gv=1;Object.defineProperty(h,'visible',{configurable:true,get:()=>true,set:()=>{}});if(h.userData.cup){const c=h.userData.cup;Object.defineProperty(c,'visible',{configurable:true,get:()=>true,set:()=>{}});}}});}"
ME="{const W6=window.__W();const G=W6.G;if(!G.onFoot){G.car.v=0;W6.toggleCar();}G.onFoot=true;const mm=W6.meMesh;if(mm&&!mm.__h){mm.__h=1;Object.defineProperty(mm,'visible',{configurable:true,get:()=>false,set:()=>{}});}G.me.x=%s;G.me.z=%s;G.me.v=0;window.__auto=()=>({fwd:0,side:0});}"
def CARZ(x,z0,v):  # coupé le long de z, sens -z
  return ("const W7=window.__W();const g=window.__CP;const cx=%f,cz=%f-%f*T;const cy=W7.GH(cx,cz);g.position.set(cx,cy,cz);g.rotation.order='YXZ';g.rotation.y=Math.PI;"
          "if(window.__lt!=null&&T>window.__lt){W7.spinWheels(g,%f,0,T-window.__lt);}window.__lt=T;")%(x,z0,v,v)
def L(p,t,fov=60): return "return {p:[%s,%s,%s],t:[%s,%s,%s],fov:%s};"%(tuple(p)+tuple(t)+(fov,))
def MKJ(name,body,n=1,o=0,js="",wait=3000,car="true",me=("395","200")):
  s=shot(name,body,dayT=DT,n=n,toff=o,wait=wait,js=NO+NOPLANE+HB+UNFPV+(CP%car)+notraf+HIDELIGHTS+(ME%me)+js); s["far"]=8000; return s
S={}; K={}
# J1 : coupé néon au ras du sol sur la route de la plage (voie -z x = 395,6), caméra basse
S["J1"]=CARZ(395.6,320,22)+L(("cx-1.6","cy+0.35","cz+5.5"),("cx+0.2","cy+0.6","cz-30"),58)
S["J1b"]=CARZ(395.6,320,22)+L(("cx+3.4","cy+0.3","cz-4.5"),("cx-0.6","cy+0.55","cz+2"),56)
# J2 : la grande roue depuis le canal
S["J2"]="const W7=window.__W();"+L(("-560+6*T","2.0","120"),("-575","36","-56"),56)
S["J2b"]="const W7=window.__W();"+L(("-600+6*T","1.6","110"),("-575","34","-56"),52)
# J3 : guinguette de la plage avec du monde
S["J3"]="const W7=window.__W();"+L(("-432+1.2*T","1.9","88"),("-414","2.2","78"),58)
S["J3b"]="const W7=window.__W();"+L(("-436+1.5*T","1.7","92"),("-418","1.6","79"),54)
for k in ("J2","J2b","J3","J3b"): K[k]=dict(car="false",me=("-470","80"),js=GV)
def MK(name,body,n=1,o=0,js="",wait=3000):
  k=K.get(name.split('_')[0],{})
  return MKJ(name,body,n,o,js+k.get("js",""),wait,k.get("car","true"),k.get("me",("395","200")))
NEAR=""
S["J1c"]=CARZ(395.6,320,22)+L(("cx+4.2","cy+0.35","cz-2.2+0.0*T"),("cx-0.6","cy+0.55","cz+0.4"),56)
S["J1d"]=CARZ(395.6,320,22)+L(("cx-3.8","cy+0.4","cz-3.5"),("cx+0.4","cy+0.6","cz+1"),56)
S["J2c"]="const W7=window.__W();"+L(("-640+7*T","1.4","12"),("-575","34","-56"),60)
for k in ("J2c",): K[k]=dict(car="false",me=("-470","80"),js=GV)
