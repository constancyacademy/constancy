# tujoues_b4 (mer. 25/11 12h, VRAI 3D, COMMANDE de l'expert du 23/11 23h15) · perso qui court vers l'avion de ligne au sol, ras du tarmac le long de l'avion, tour de contrôle
# Avions de ligne au sol (V310.41) : groupes de 67,6 × 22,9 × 63,8 à (-40 ; 1525) rot π, (-354 ; 1506), (-474 ; 1506), (-594 ; 1506) · tour (-150 ; 1422), 81 m
DT=int(os.environ.get("DT","480"))
def L(p,t,fov=60): return "return {p:[%s,%s,%s],t:[%s,%s,%s],fov:%s};"%(tuple(p)+tuple(t)+(fov,))
HB="{const W6=window.__W();if(!window.__HB){window.__HB=1;const H=o=>{if(o&&o.isObject3D)Object.defineProperty(o,'visible',{configurable:true,get:()=>false,set:()=>{}});};const B=W6.BANNER;if(B){H(B.g);H(B.plane);H(B.cloth);}W6.scene.traverse(o=>{if(o.isMesh&&o.material&&o.material.blending===2&&o.geometry){o.geometry.computeBoundingBox();const bb=o.geometry.boundingBox;if(o.scale.y*(bb.max.y-bb.min.y)>100)H(o);}});(W6.JW&&W6.JW.beams||[]).forEach(b=>H(b.isObject3D?b:(b.m||b.mesh)));}}"
NOCAR="{const W8=window.__W();W8.traffic.forEach(a=>{if(a.mesh&&!a.mesh.__h){a.mesh.__h=1;Object.defineProperty(a.mesh,'visible',{configurable:true,get:()=>false,set:()=>{}});}});const G8=W8.G;if(G8.parked&&G8.parked.mesh)G8.parked.mesh.visible=false;{const om=W8.ownMark;if(om&&!om.__h){om.__h=1;Object.defineProperty(om,'visible',{configurable:true,get:()=>false,set:()=>{}});}}}"
def MK(name,body,n=1,o=0,js="",wait=2500):
  s=shot(name,body,dayT=DT,n=n,toff=o,wait=wait,js=NO+NOPLANE+HB+NOCAR+js); s["far"]=20000; return s
S={}
# repérage
S["V1"]=L(("-112","3","1497"),("-40","8","1525"),60)
S["V2"]=L(("-40","160","1525.1"),("-40","0","1525"),60)
S["V3"]=L(("-100","3","1470"),("-150","40","1422"),60)
S["V4"]=L(("-90","2","1540"),("-150","30","1422"),60)
S["V5"]=L(("-80","1.2","1505"),("-40","5","1525"),60)
S["V6"]=L(("-10","1.4","1492"),("-40","6","1525"),60)
# perso qui court (le jeu le fait courir lui-même) · caméra du jeu derrière lui
PX,PZ=float(os.environ.get("PX","-112")),float(os.environ.get("PZ","1497"))
TX,TZ=float(os.environ.get("TGX","-58")),float(os.environ.get("TGZ","1514"))
RUN=("{const W6=window.__W(),G=W6.G;G.mode='play';G.fpv=false;if(!G.onFoot){G.car.v=0;G.entering=null;G.wantExit=false;W6.toggleCar();}G.doorClose=null;G.entering=null;"
 "G.me.x=%f;G.me.z=%f;G.me.v=0;G.me.h=Math.atan2((%f)-(%f),(%f)-(%f));W6.meMesh.visible=true;window.__LOGS=[];"
 "window.__auto=(g)=>{if(window.__T0==null)return {fwd:0,side:0};return {fwd:1,side:0};};}")%(PX,PZ,TX,PX,TZ,PZ)
ME="const W7=window.__W(),G7=W7.G;G7.mode='play';const mx=G7.me.x,mz=G7.me.z,mh=G7.me.h,fx=Math.sin(mh),fz=Math.cos(mh);window.__LOGS.push([+T.toFixed(2),+mx.toFixed(2),+mz.toFixed(2),+(G7.me.v||0).toFixed(2)]);"
D=float(os.environ.get("D","4.6")); Y=float(os.environ.get("Y","2.0"))
S["RUN1"]=ME+"return {p:[mx-fx*%f,%f,mz-fz*%f],t:[mx+fx*20,%f,mz+fz*20],fov:58};"%(D,Y,D,Y+1.2)
S["RUN2"]=ME+"return {p:[mx-fx*%f+fz*0.9,%f,mz-fz*%f-fx*0.9],t:[mx+fx*18,%f,mz+fz*18],fov:56};"%(D,Y,D,Y+2.0)
_MK0=MK
def MK(name,body,n=1,o=0,js="",wait=2500):
  if "G7.me" in body: js=RUN+js
  return _MK0(name,body,n=n,o=o,js=js,wait=wait)
S["T1"]=L(("0","3","1480"),("-200","25","1450"),60)
S["T2"]=L(("-40","2.5","1470"),("-250","22","1455"),60)
S["T3"]=L(("-20","2","1500"),("-200","25","1445"),62)
S["U1"]=L(("-95","1.3","1512"),("-40","4","1520"),60)
S["U2"]=L(("-90","1.1","1488"),("-40","3","1500"),60)
S["RUN3"]=ME+"return {p:[mx-fx*7.5,3.3,mz-fz*7.5],t:[mx+fx*22,1.6,mz+fz*22],fov:58};"
S["RUN4"]=ME+"return {p:[mx-fx*8.5+fz*1.2,3.8,mz-fz*8.5-fx*1.2],t:[mx+fx*22,1.4,mz+fz*22],fov:56};"
S["U3"]=L(("-68","1.2","1486+9*T"),("-40","3.5","1500+9*T"),60)
S["U4"]=L(("-75+7*T","1.0","1470"),("-40","3","1492"),60)
S["T4"]=L(("0-7*T","3","1480-1*T"),("-200","25","1450"),60)
S["V3m"]=L(("-100-1.2*T","3+0.5*T","1470"),("-150","40","1422"),60)
S["RUN5"]=ME+"return {p:[mx-fx*7.5,3.3,mz-fz*7.5],t:[mx+fx*22,0,mz+fz*22],fov:58};"
