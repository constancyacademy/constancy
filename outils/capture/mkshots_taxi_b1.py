# taxi_b1 (sam. 28/11 7h, M1 MISSION POV « POV : Ton téléphone est resté dans le taxi. ») · mission « Rattrape le taxi » (V310.55)
# Rue z = 0 (centre-ville, voie +x à z ≈ +2), au lever du jour (G.dawn, h0 6,75). Le taxi du jeu (car_taxi, blanc et rose), la voiture du joueur derrière qui fonce, le colle, se met à sa hauteur, le taxi s'arrête.
import os
exec(open('/root/cap/lib212.py').read())
H0=float(os.environ.get("H0","6.75"))
TAXIM=os.environ.get("TAXIM","car_taxi"); PCAR=os.environ.get("PCAR","minuit")
X0=float(os.environ.get("X0","-262"))
ZT,ZP=2.2,-1.4
DAWN="{const W6=window.__W();W6.G.dawn=Math.max(0,8-%f);if(W6.P)W6.P.dayT=0.5;}"%H0
UNFPV="{const W6=window.__W();W6.G.fpv=false;W6.G.mode='play';}"
HB="{const W6=window.__W();if(!window.__HB){window.__HB=1;const H=o=>{if(o&&o.isObject3D)Object.defineProperty(o,'visible',{configurable:true,get:()=>false,set:()=>{}});};const B=W6.BANNER;if(B){H(B.g);H(B.plane);H(B.cloth);}}}"
CARS2=("{const W9=window.__W();if(!window.__TX){const g=W9.makeCar({id:'trafic',color:0xffffff},{model:'%s',keepPaint:true});W9.scene.add(g);window.__TX=g;}"
 "if(!window.__PC){const g=W9.makeCar(W9.CARS.find(c=>c.id=='%s'));W9.scene.add(g);window.__PC=g;}"
 "W9.scene.traverse(o=>{if(o.userData&&o.userData.isCar&&o!==window.__TX&&o!==window.__PC&&!o.__hid&&!(W9.SHOWROOM&&0)){o.__hid=1;Object.defineProperty(o,'visible',{configurable:true,get:()=>false,set:()=>{}});}});"
 "delete window.__TX.visible;delete window.__PC.visible;window.__TX.visible=true;window.__PC.visible=true;window.__lt=null;}")%(TAXIM,PCAR)
# simulation : R = temps de l'histoire
SIM=("const W7=window.__W();const R=T+(%%s);const V0=15,TB=3.7,DEC=7.5,X0=%f,ZT=%f,ZP=%f;"
 "const sm=u=>{u=Math.max(0,Math.min(1,u));return u*u*(3-2*u);};const dsm=u=>(u<=0||u>=1)?0:6*u*(1-u);"
 "const s=Math.max(0,Math.min(R-TB,V0/DEC));const xt=X0+V0*Math.min(R,TB)+V0*s-0.5*DEC*s*s;const vt=R<TB?V0:Math.max(0,V0-DEC*(R-TB));"
 "const u=Math.max(0,Math.min(1,R/2.4));const gp=-16+15*(1-(1-u)*(1-u));const dg=u<1?15*2*(1-u)/2.4:0;"
 "const w=(R-0.8)/1.2;const zp=ZT+(ZP-ZT)*sm(w);const dz=(ZP-ZT)*dsm(w)/1.2;"
 "const xp=xt+gp,vp=vt+dg;const A=window.__TX,B=window.__PC;"
 "A.position.set(xt,W7.GH(xt,ZT),ZT);A.rotation.order='YXZ';A.rotation.y=Math.PI/2;"
 "B.position.set(xp,W7.GH(xp,zp),zp);B.rotation.order='YXZ';B.rotation.y=Math.atan2(Math.max(vp,0.001),dz);"
 "if(window.__lt!=null&&T>window.__lt){W7.spinWheels(A,vt,0,T-window.__lt);W7.spinWheels(B,vp,0,T-window.__lt);}window.__lt=T;"
 "const tx=xt,ty=A.position.y,px=xp,py=B.position.y,pz=zp;")%(X0,ZT,ZP)
def L(p,t,fov=60): return "return {p:[%s,%s,%s],t:[%s,%s,%s],fov:%s};"%(tuple(p)+tuple(t)+(fov,))
def MKT(name,body,n=1,o=0,js="",wait=2500):
  s=shot(name,body,dayT=0.5,n=n,toff=o,wait=wait,js=DAWN+NO+NOPLANE+HB+UNFPV+CARS2+notraf+HIDELIGHTS+js,pre=DAWN); s["far"]=6000; return s
S={}
# A : derrière la voiture du joueur, bas, qui fonce vers le taxi
S["A1"]=SIM%"0"+L(("px-7.5","py+1.35","pz+0.5"),("px+22","py+0.9","(pz+%f)/2"%ZT),58)
S["A2"]=SIM%"0"+L(("px-6","py+0.9","pz-1.2"),("px+22","py+0.8","%f"%ZT),56)
# B : devant les deux voitures, caméra qui recule à leur vitesse, côte à côte
S["B1"]=SIM%"2.4"+L(("tx+12","ty+1.2","0.4"),("tx","ty+0.7","0.4"),52)
S["B2"]=SIM%"2.4"+L(("tx+9","ty+0.7","%f"%(ZP-3.2)),("tx-1","ty+0.8","0.8"),54)
# C : sur le trottoir, le taxi freine et s'arrête
XS=X0+15*3.7+15
S["C1"]=SIM%"4.6"+L(("%f"%(XS+7),"1.3","7.2"),("tx-1","ty+0.8","%f"%ZT),56)
S["C2"]=SIM%"4.6"+L(("%f"%(XS+3),"1.2","-6.5"),("tx","ty+0.8","0.4"),56)
def MK(name,body,n=1,o=0,js="",wait=2500): return MKT(name,body,n,o,js,wait)
NEAR=""
# FINAL (60 i/s, pre 11 : image 0 à T = 0,2 s, donc décalage R0 - 0,2)
S["Af"]=SIM%"-0.2"+L(("px-7.5","py+1.35","pz+0.5"),("px+22","py+0.9","(pz+%f)/2"%ZT),58)
S["Bf"]=SIM%"2.1"+L(("tx+9","ty+0.7","%f"%(ZP-3.2)),("tx-1","ty+0.8","0.8"),54)
S["Cf"]=SIM%"3.6"+L(("%f-0.5*(R-3.8)"%(XS+6),"1.3","-8.5+0.2*(R-3.8)"),("tx-0.5","ty+0.8","0.4"),60)
# v2 : cadrages plus serrés (moins d'asphalte), C en arc autour des 2 voitures arrêtées
S["Bg"]=SIM%"2.1"+L(("tx+7.2","ty+0.85","%f"%(ZP-2.4)),("tx-1.2","ty+0.55","0.6"),62)
S["Cg"]=SIM%"3.6"+("const a=-0.62-0.16*Math.max(0,R-4.6);const MX=%f,MZ=0.4;"%(XS-0.6))+L(("MX+8.2*Math.cos(a)","1.05","MZ+8.2*Math.sin(a)"),("Math.max(tx-0.6,MX-40)","ty+0.5","MZ"),62)
S["Cg2"]=SIM%"3.6"+("const a=-0.62+0.14*Math.max(0,R-4.6);const MX=%f,MZ=0.6;"%(XS-0.6))+L(("MX+8.2*Math.cos(a)","1.05","MZ+8.2*Math.sin(a)"),("Math.max(tx-0.8,MX-40)","ty+0.5","MZ"),62)
