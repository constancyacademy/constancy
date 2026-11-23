# M4 « 23 h. Ma ville ne dort jamais. » (mer. 25/11 21h, NUIT) · roue depuis l'eau, file du Constancy Club, plage et lampadaires, voiture sur le pont de l'Esplanade
DT=int(os.environ.get("DT","900"))
def L(p,t,fov=60): return "return {p:[%s,%s,%s],t:[%s,%s,%s],fov:%s};"%(tuple(p)+tuple(t)+(fov,))
UNFPV="{const W6=window.__W();W6.G.fpv=false;W6.G.mode='play';}"
def MK(name,body,n=1,o=0,js="",wait=2500):
  s=shot(name,body,dayT=DT,n=n,toff=o,wait=wait,js=NO+NOPLANE+UNFPV+js); s["far"]=20000; return s
S={}
S["R1"]=L(("-575+60","1.2","-56+70"),("-575","38","-56"),55)
S["R2"]=L(("-575-50","1.2","-56+60"),("-575","36","-56"),55)
S["R3"]=L(("-575+20","1.2","-56-90"),("-575","38","-56"),55)
S["C1"]=L(("-74","2.2","-104"),("-88","1.6","-122"),55)
S["C2"]=L(("-100","2.0","-106"),("-86","1.6","-122"),55)
S["P1"]=L(("-60","2.0","560"),("40","1.5","470"),60)
S["P2"]=L(("120","2.5","470"),("0","1.2","520"),60)
S["E1"]=L(("30","6","640"),("10","3","690"),60)
S["E2"]=L(("-10","2","700"),("10","4","650"),60)
S["R4"]=L(("-628+3*T","1.1","6"),("-575","36","-56"),55)
S["C3"]=L(("-101+2*T","1.9","-108"),("-87","2.8","-122"),52)
S["P3"]=L(("0","3","420"),("40","2","520"),60)
S["P4"]=L(("-200","1.7","600"),("-100","2.5","560"),60)
S["P5"]=L(("150","2.2","430"),("60","1.6","470"),58)
CARN="{const W9=window.__W();if(!window.__VNC){const g=W9.makeCar(W9.CARS.find(c=>c.id=='minuit'));W9.scene.add(g);window.__VNC=g;}delete window.__VNC.visible;window.__VNC.visible=true;window.__lt=null;}"
def bridge(x,z0,vz):
  ry=0 if vz>0 else math.pi
  return ("const W7=window.__W();const g=window.__VNC;const D=W7.DK.decks.find(d=>d.name===\"Pont de l'Esplanade\").S;const cx=%f,cz=%f+(%f)*T;let cy=D[0][2];for(let i=1;i<D.length;i++){if(D[i][1]>=cz){const a=D[i-1],b=D[i],k=(cz-a[1])/(b[1]-a[1]);cy=a[2]+(b[2]-a[2])*k;break;}cy=D[i][2];}cy+=0.12;"
          "g.position.set(cx,cy,cz);g.rotation.order='YXZ';g.rotation.y=%f;if(window.__lt!=null&&T>window.__lt){W7.spinWheels(g,%f,0,T-window.__lt);}window.__lt=T;")%(x,z0,vz,ry,abs(vz))
S["E3"]=bridge(13.5,615,18)+L(("30","3","650"),("cx","cy+0.6","cz"),58)
S["E4"]=bridge(13.5,615,18)+L(("cx+6","cy+3","cz-9"),("cx-1","cy+0.5","cz+6"),60)
_MKV=MK
def MK(name,body,n=1,o=0,js="",wait=2500):
  if "__VNC" in body: js=CARN+js
  return _MKV(name,body,n=n,o=o,js=js,wait=wait)
# rendu final (24/11 0h10)
S["R5"]=L(("-630+6*T","1.1+0.3*T","6"),("-575","36","-56"),55)
S["R6"]=L(("-552-4*T","1.2","-146"),("-575","36","-56"),55)
S["E5"]=bridge(6.5,612,18)+L(("cx+6","cy+3","cz-9"),("cx-1","cy+0.5","cz+6"),60)
# pont : circulation cachée (une citadine de la circulation passait à travers la Minuit), phares fantômes coupés
S["E6"]="{const W8=window.__W();W8.traffic.forEach(a=>{if(a.mesh&&!a.mesh.__h){a.mesh.__h=1;Object.defineProperty(a.mesh,'visible',{configurable:true,get:()=>false,set:()=>{}});}});}"+HIDELIGHTS+S["E5"]
# les 2 voitures du pont (DK, pas dans traffic) aussi cachées : seule la Minuit roule
S["E7"]="{const W8=window.__W();W8.scene.traverse(o=>{if(o.userData&&o.userData.isCar&&o!==window.__VNC&&!o.__hid){o.__hid=1;Object.defineProperty(o,'visible',{configurable:true,get:()=>false,set:()=>{}});}});}"+S["E6"]
