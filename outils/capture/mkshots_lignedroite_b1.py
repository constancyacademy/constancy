import math
exec(open('/root/cap/lib212.py').read())
DT=690
HB="{const W6=window.__W();if(!window.__HB){window.__HB=1;const H=o=>{if(o&&o.isObject3D)Object.defineProperty(o,'visible',{configurable:true,get:()=>false,set:()=>{}});};const B=W6.BANNER;if(B){H(B.g);H(B.plane);H(B.cloth);}}}"
UNFPV="{const W6=window.__W();W6.G.fpv=false;W6.G.mode='play';}"
CARS2="{const W9=window.__W();if(!window.__CA){const g=W9.makeCar(W9.CARS.find(c=>c.id=='coupe'));W9.scene.add(g);window.__CA=g;}if(!window.__CB){const g=W9.makeCar(W9.CARS.find(c=>c.id=='%s'));W9.scene.add(g);window.__CB=g;}window.__CA.visible=true;window.__CB.visible=true;window.__ltA=null;window.__ltB=null;}"
RIVAL="gt"
ZA,ZB=-52.4,-55.6
X0=-80.0
# position le long de x : arrêt jusqu'à R0, puis accélération a jusqu'à vmax
def P(a,vm): return "((R)=>{const t=Math.max(0,R-%f);const tv=%f/%f;return t<tv?0.5*%f*t*t:0.5*%f*tv*tv+%f*(t-tv);})"%(3.2,vm,a,a,a,vm)
def V(a,vm): return "((R)=>{const t=Math.max(0,R-%f);return Math.min(%f,%f*t);})"%(3.2,vm,a)
def RACE(off):
  return ("const W7=window.__W();const R=T+(%f);const pA=%s,pB=%s,vA=%s,vB=%s;"
   "const ax=%f+pA(R),bx=%f+pB(R),za=%f,zb=%f;const A=window.__CA,B=window.__CB;"
   "A.position.set(ax,W7.GH(ax,za),za);A.rotation.order='YXZ';A.rotation.y=Math.PI/2;B.position.set(bx,W7.GH(bx,zb),zb);B.rotation.order='YXZ';B.rotation.y=Math.PI/2;"
   "if(window.__ltA!=null&&T>window.__ltA){W7.spinWheels(A,vA(R),0,T-window.__ltA);W7.spinWheels(B,vB(R),0,T-window.__ltA);}window.__ltA=T;"
   "const cx=ax,cy=A.position.y,cz=za;")%(off,P(9,30),P(8,28),V(9,30),V(8,28),X0,X0+0.6,ZA,ZB)
def L(p,t,fov=60): return "return {p:[%s,%s,%s],t:[%s,%s,%s],fov:%s};"%(tuple(p)+tuple(t)+(fov,))
def MKL(name,body,n=1,o=0,js="",wait=2500):
  s=shot(name,body,dayT=DT,n=n,toff=o,wait=wait,js=NO+NOPLANE+HB+UNFPV+(CARS2%RIVAL)+notraf+js+BEACON); s["far"]=20000; return s
S={}
S["OV"]=RACE(0)+L(("cx+10","cy+40","cz-30"),("cx+10","cy","cz-2"),60)
S["OV2"]=RACE(0)+L(("cx-25","cy+12","cz-12"),("cx+30","cy","cz-3"),60)
BX=X0+120
BEACON="{const W5b=window.__W();const b=W5b.destBeacon;if(b){b.position.set(%f,0,-54);delete b.visible;b.visible=true;}}"%BX
S["V1"]=RACE(0)+L(("cx+0.15","cy+1.12","cz-0.35"),("cx-0.1","cy+0.95","%f"%ZB),62)
S["F1"]=RACE(0)+L(("cx+5.5","cy+0.6","-49.5-5*T"),("cx+1","cy+0.7","-54"),54)
S["W2"]=RACE(1.6)+L(("cx+2.5+0.4*T","cy+0.4","cz+3.2"),("cx+0.5","cy+0.4","-54"),56)
S["D3"]=RACE(3.2)+L(("cx-1.5","cy+0.9","cz+4.5"),("cx+3","cy+0.5","-54"),58)
S["D4"]=RACE(3.2)+L(("cx+6","cy+0.5","-48.5"),("cx-2","cy+0.6","-54"),56)
S["B4"]=RACE(8.07)+L(("%f"%(BX+6),"1.3","-48.5"),("%f"%(BX-20),"0.9","-54"),56)
S["Wf"]=RACE(1.8)+L(("cx+2.5+0.4*T","cy+0.4","cz+3.2"),("cx+0.5","cy+0.4","-54"),56)
S["Df"]=RACE(3.3)+L(("cx+6","cy+0.5","-48.5"),("cx-2","cy+0.6","-54"),56)
S["Vf"]=RACE(1.2)+L(("cx+0.15+0.5*T","cy+1.12","cz-0.35"),("cx-0.1+0.5*T","cy+0.95","%f"%ZB),62)
S["Bf"]=RACE(8.47)+L(("%f"%(BX+3),"1.0","-50.2"),("%f"%(BX-15),"0.7","-53.6"),50)
S["Bp"]=RACE(8.47)+L(("%f"%(BX+3),"1.0","-49.6"),("cx","cy+0.6","cz"),52)
S["Ef"]=RACE(10.2)+L(("cx+4.5","cy+0.8","cz+3.6"),("cx-3","cy+0.5","-54"),58)
S["G1"]=RACE(1.2)+L(("cx-1.2+1.4*T","cy+0.8","-59.8"),("cx+0.4+1.4*T","cy+0.6","-55.6"),55)
S["Wg"]=RACE(1.8)+L(("cx-2.8+2.3*T","cy+0.45","cz+2.6"),("cx-1.6+2.3*T","cy+0.4","cz"),56)
S["Pf"]=RACE(3.3)+L(("%f"%(X0-3),"W7.GH(%f,-49.8)+0.8"%(X0-3),"-49.8"),("%f"%(X0+25),"W7.GH(%f,-54.2)+1.0"%(X0+25),"-54.2"),55)
S["Eg"]=RACE(5.0)+L(("cx+4.5","cy+0.8","cz+3.6"),("cx-3","cy+0.5","-54"),58)
S["Eh"]=RACE(5.0)+L(("cx+4.5","cy+0.9","-59.6"),("cx-4","cy+0.5","-54"),58)
def MK(name,body,n=1,o=0,js="",wait=2500): return MKL(name,body,n,o,js,wait)
NEAR=""
