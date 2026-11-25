import math
exec(open('/root/cap/lib212.py').read())
DT=840
CX,CZ=-1500.0,330.0
NOPAN="{const e=document.getElementById('screen');if(e){e.classList.add('hidden');e.innerHTML='';}}"
CAR="{const W9=window.__W();if(!window.__LX){const g=W9.makeCar(W9.CARS.find(c=>c.id=='%s'));if(g.userData.nacre)g.userData.nacre.em=[];W9.scene.add(g);window.__LX=g;}window.__LX.visible=true;window.__lt=null;}"
CARID="or"
def ring(R,a0,w):
  return ("const W7=window.__W();const g=window.__LX;const a=%f+(%f)*T;const x=%f+Math.cos(a)*%f,z=%f+Math.sin(a)*%f;const y=W7.GH(x,z);g.position.set(x,y,z);g.rotation.order='YXZ';"
          "const dx=-Math.sin(a)*Math.sign(%f),dz=Math.cos(a)*Math.sign(%f);g.rotation.y=Math.atan2(dx,dz);"
          "if(window.__lt!=null&&T>window.__lt){W7.spinWheels(g,%f,0,T-window.__lt);}window.__lt=T;const cx=x,cy=y,cz=z;")%(a0,w,CX,R,CZ,R,w,w,abs(w*R))
def L(p,t,fov=60): return "return {p:[%s,%s,%s],t:[%s,%s,%s],fov:%s};"%(tuple(p)+tuple(t)+(fov,))
S={}
for i,a in enumerate([0.0,0.8,1.6,2.4,3.2,4.0,4.8,5.6]):
  S["O%d"%i]=ring(90,0.3,0.2)+L(("%f"%(CX+math.cos(a)*140),"40","%f"%(CZ+math.sin(a)*140)),("%f"%CX,"5","%f"%CZ),60)
S["G1"]=ring(90,-0.25,0.18)+L(("%f+Math.cos(0.35-0.12*T)*112"%CX,"7","%f+Math.sin(0.35-0.12*T)*112"%CZ),("%f"%CX,"12","%f"%CZ),62)
S["G2"]=ring(90,-0.2,0.2)+L(("cx+Math.cos(0.1)*14","3","cz+Math.sin(0.1)*14"),("cx","1","cz"),58)
import math as _m
S["M1"]=ring(90,0.35,-0.22)+L(("%f+Math.cos(-0.22+0.21*T)*104"%CX,"cy+9","%f+Math.sin(-0.22+0.21*T)*104"%CZ),("%f"%CX,"cy+7","%f"%CZ),58)
S["M1b"]=ring(90,0.30,-0.22)+L(("%f+Math.cos(-0.25+0.21*T)*100"%CX,"cy+4.5","%f+Math.sin(-0.25+0.21*T)*100"%CZ),("%f+Math.cos(0.05)*60"%CX,"cy+6","%f+Math.sin(0.05)*60"%CZ),60)
S["P1"]=ring(90,0,0)+L(("-1050-15*T","220-8*T","330"),("-1350","0","330"),60)
S["P2"]=ring(90,0,0)+L(("-1150-15*T","140-6*T","520"),("-1400","0","380"),62)
S["P3"]=ring(90,0,0)+L(("-1250-12*T","90-4*T","600"),("-1450","0","420"),62)
S["Y1"]=ring(90,0,0)+L(("-1170-4*T","6","700+2*T"),("-1235","2","770"),58)
S["Y2"]=ring(90,0,0)+L(("-1150","14","650+4*T"),("-1260","0","790"),62)
S["N1"]=ring(90,0,0)+L(("26+6*T","1.5","636+Math.max(0,26+6*T-66)*1.25"),("26+6*T","8","604"),60)
S["N2"]=ring(90,0,0)+L(("40+6*T","2.5","650"),("40+6*T","9","604"),62)
S["M1c"]=ring(88,0.55,-0.42)+L(("%f+Math.cos(0.30-0.25*T)*96"%CX,"cy*0+W7.GH(%f+Math.cos(0.30-0.25*T)*96,%f+Math.sin(0.30-0.25*T)*96)+2.2"%(CX,CZ),"%f+Math.sin(0.30-0.25*T)*96"%CZ),("%f+Math.cos(-0.2-0.25*T)*35"%CX,"W7.GH(%f,%f)+7"%(CX,CZ),"%f+Math.sin(-0.2-0.25*T)*35"%CZ),60)
S["Y3"]=ring(90,0,0)+L(("-1345+4*T","6","885"),("-1372","3","828"),56)
S["Y4"]=ring(90,0,0)+L(("-1320+5*T","26","900"),("-1380","0","800"),60)
S["P4"]=ring(90,0,0)+L(("%f+Math.cos(2.3)*(430-12*T)"%CX,"45-2*T","%f+Math.sin(2.3)*(430-12*T)"%CZ),("%f+Math.cos(2.3)*280"%CX,"0","%f+Math.sin(2.3)*280"%CZ),60)
S["M1d"]=ring(88,0.80,-0.36)+L(("%f+Math.cos(0.45-0.16*T)*100"%CX,"W7.GH(%f+Math.cos(0.45-0.16*T)*100,%f+Math.sin(0.45-0.16*T)*100)+5"%(CX,CZ),"%f+Math.sin(0.45-0.16*T)*100"%CZ),("%f"%CX,"W7.GH(%f,%f)+9"%(CX,CZ),"%f"%CZ),58)
RINGA=("const W7=window.__W();const g=window.__LX;const a=%f+(%f)*T;const x=%f+Math.cos(a)*%f,z=%f+Math.sin(a)*%f;const y=W7.GH(x,z);g.position.set(x,y,z);g.rotation.order='YXZ';"
 "const dx=-Math.sin(a)*Math.sign(%f),dz=Math.cos(a)*Math.sign(%f);g.rotation.y=Math.atan2(dx,dz);"
 "if(window.__lt!=null&&T>window.__lt){W7.spinWheels(g,%f,0,T-window.__lt);}window.__lt=T;const cx=x,cy=y,cz=z;")
def ringa(R,a0,w): return RINGA%(a0,w,CX,R,CZ,R,w,w,abs(w*R))
S["S1"]=ringa(88,0.95,-0.2)+L(("%f+Math.cos(a+0.045)*94"%CX,"cy+0.8","%f+Math.sin(a+0.045)*94"%CZ),("cx+(%f-cx)*0.12"%CX,"cy+1.3","cz+(%f-cz)*0.12"%CZ),56)
S["S2"]=ringa(88,0.95,-0.2)+L(("%f+Math.cos(a+0.06)*93"%CX,"cy+1.1","%f+Math.sin(a+0.06)*93"%CZ),("%f"%CX,"cy+6","%f"%CZ),58)
S["Y5"]=ring(90,0,0)+L(("-1320+14*T","20-3*T","900-6*T"),("-1375+4*T","2","815"),60)
S["P5"]=ring(90,0,0)+L(("%f+Math.cos(2.3)*(330-16*T)+Math.cos(2.3+1.57)*6"%CX,"24-3*T","%f+Math.sin(2.3)*(330-16*T)+Math.sin(2.3+1.57)*6"%CZ),("%f+Math.cos(2.3)*(285-16*T)"%CX,"0","%f+Math.sin(2.3)*(285-16*T)"%CZ),60)
S["P6"]=ring(90,0,0)+L(("%f+Math.cos(2.0)*(360-16*T)"%CX,"30-3*T","%f+Math.sin(2.0)*(360-16*T)"%CZ),("%f+Math.cos(2.0)*(310-16*T)"%CX,"0","%f+Math.sin(2.0)*(310-16*T)"%CZ),60)
S["N3"]=ring(90,0,0)+L(("40+6*T","2.5","650-1.6*T"),("40+6*T","9","604"),62)
NOPED="{const W6=window.__W();const H=m=>{if(m&&m.isObject3D&&!m.__h){m.__h=1;Object.defineProperty(m,'visible',{configurable:true,get:()=>false,set:()=>{}});}};[].concat(W6.peds||[]).forEach(p=>{H(p&&(p.mesh||p.g||p.m||p));});}"
S["S3"]=ringa(90,0.95,-0.2)+L(("%f+Math.cos(a+0.055)*94.5"%CX,"cy+0.75","%f+Math.sin(a+0.055)*94.5"%CZ),("%f"%CX,"cy+4.5","%f"%CZ),56)
NOFIRE="{const W6=window.__W();if(W6.FIRE&&W6.FIRE.grp)W6.FIRE.grp.visible=false;if(W6.FIRE&&W6.FIRE.truck)W6.FIRE.truck.visible=false;}"
NOME="{const W8=window.__W();if(!W8.meMesh.__h){W8.meMesh.__h=1;Object.defineProperty(W8.meMesh,'visible',{configurable:true,get:()=>false,set:()=>{}});}}"
def MK(name,body,n=1,o=0,js="",wait=2500):
  s=shot(name,body,dayT=DT,n=n,toff=o,wait=wait,js=NO+NOPLANE+notraf+NOPAN+(CAR%CARID)+NOME+NOPED+NOFIRE+js); s["far"]=20000; return s
NEAR=""
