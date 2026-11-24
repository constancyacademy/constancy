# appart25m_b1 (jeu. 26/11 21h, M4 NUIT, COMMANDE de l'expert du 24/11 19h45) · « La vue d'un appart à 25 millions. »
# Le Penthouse de la Tour (Agence, 25 000 000 $, 88e étage, y 296) : W.startVisit construit l'intérieur, puis VISIT.on = false pour reprendre la caméra (sinon visitCam)
import os,math
DT=int(os.environ.get("DT","840"))
def L(p,t,fov=60): return "return {p:[%s,%s,%s],t:[%s,%s,%s],fov:%s};"%(tuple(p)+tuple(t)+(fov,))
PLAYW="{const W6=window.__W();if(!window.__stepP){const s0=window.__step;window.__step=ms=>{W6.G.mode='play';return s0(ms);};window.__stepP=1;}const F=window.__FW;window.__fwBig=1;F.party=30;F.pts.visible=true;}"
VIS="{const W6=window.__W();if(!window.__APG){const a=(W6.AGENCE||[]).find(x=>x.id=='penthouse');W6.startVisit(a);}}"
TAKE="{const W6=window.__W();if(W6.VISIT.on){window.__APG=W6.VISIT.g;W6.VISIT.on=false;}W6.G.mode='play';W6.G.fpv=false;document.body.classList.remove('lifting');}"
FWK="{const F=window.__FW;if(F){if(!(F.party>5))F.party=30;if(F.next>0.45)F.next=0.45;}window.__fwBig=1;}"
# coordonnées locales de l'appartement (W 24 en x, D 16 en z, H 5,8) → monde
def LL(p,t,fov=60):
  return ("const g=window.__APG;if(!g)return {p:[0,400,0],t:[0,0,0],fov:60};const A=g.localToWorld(new THREE.Vector3(%s,%s,%s)),B=g.localToWorld(new THREE.Vector3(%s,%s,%s));"
          "return {p:[A.x,A.y,A.z],t:[B.x,B.y,B.z],fov:%s};")%(tuple(p)+tuple(t)+(fov,))
def MK(name,body,n=1,o=0,js="",wait=2500):
  s=shot(name,FWK+body,dayT=DT,n=n,toff=o,wait=wait,js=NO+NOPLANE+PLAYW+TAKE+globals().get("ME","")+js); s["far"]=20000; return s
S={}
for nm,(p,t) in {"V0":((0,1.6,-6.5),(0,1.4,30)),"V1":((0,1.6,6.5),(0,1.4,-30)),"V2":((-10,1.6,0),(30,1.4,0)),"V3":((10,1.6,0),(-30,1.4,0)),
                 "V4":((-8,1.7,-5),(20,1.0,20)),"V5":((8,1.7,5),(-20,1.0,-20)),"V6":((0,4.5,-6),(0,0,8)),"V7":((0,1.6,0),(0,-10,40))}.items():
  S[nm]=LL(p,t,62)
# joueur posé devant la baie (est, +x monde) : les tirs de la fête partent autour de lui, sous la baie
ME="{const W6=window.__W();const T6=W6.TOWER;W6.G.me.x=T6.x+200;W6.G.me.z=T6.z+20;W6.G.onFoot=true;}"
S["D1"]=LL((0,1.7,5.0),(0,-60,60),62)
S["D2"]=LL((5,1.7,5.5),(30,-80,80),62)
S["D3"]=LL((-10,1.7,3),(-40,-60,10),62)
S["D4"]=LL((0,2.5,2),(0,-30,60),70)
S["D5"]=LL((9,1.7,0),(40,-60,0),62)
