import sys; sys.path.insert(0,'/root/cap')
DT=690
SETUP="""{const W6=window.__W(),G=W6.G,F=W6.FIRE;window.__auto=(g)=>({fwd:0,side:0});
if(!F.sp){W6.P.fire=null;F.on=false;W6.fireStart(true);}
F.on=true;F.t=0;F.fade=null;F.st='out';const sp=F.sp;window.__SP=sp;const ho=sp.side>0?0:Math.PI;
try{const hb=document.getElementById('fireHold');if(hb)hb.remove();W6.fireSmokeVeil(0);}catch(e){}
if(!G.onFoot){G.car.v=0;W6.toggleCar();}
G.me.x=sp.dx+(%s);G.me.z=sp.dz+sp.side*(%s);G.me.v=0;G.me.h=%s;W6.meMesh.visible=true;
if(!window.__MAM){const m=W6.makeHuman({shirt:0x9fd8b0,pants:0x6a6a7a,skin:0xf0c8a8,hair:0xdedede});W6.scene.add(m);if(m.userData.q)W6.setClip(m,'Idle_Talking_Loop');window.__MAM=m;}
const m=window.__MAM;m.visible=%s;{const ax=sp.dx+(%s),az=sp.dz+sp.side*(%s);m.position.set(ax,W6.GH(ax,az)+0.02,az);}m.rotation.y=%s;
if(!F.truck)W6.fireTruck(sp);if(F.truck)F.truck.visible=%s;
{const keep=new Set([].concat(F.smoke.map(q=>q.s),F.flames.map(q=>q.s)));F.grp.children.slice().forEach(c=>{if(!keep.has(c))F.grp.remove(c);});F.parts=null;}W6.traffic.forEach(a=>{if(a.mesh)a.mesh.visible=false;});window.__bd=0;}"""
def setup(mx="40",mz="60",mh="0",mam="false",ax="-0.5",az="7.4",ar="0",truck="true"):
  return SETUP%(mx,mz,mh,mam,ax,az,ar,truck)
BURST="if(T>%s&&!window.__bd){window.__bd=1;W6.fireBurst();}"
def cam(p,t,fov,burst=None):
  b=(BURST%burst) if burst is not None else ""
  x,y,z=p; tx,ty,tz=t
  return ("const W6=window.__W(),sp=window.__SP;"+b+"return {p:[sp.dx+(%s),%s,sp.dz+sp.side*(%s)],t:[sp.dx+(%s),%s,sp.dz+sp.side*(%s)],fov:%s};")%(x,y,z,tx,ty,tz,fov)
S={}; J={}
# A : drone qui fonce vers la fumée au-dessus des toits (cible : le haut de l'immeuble en feu)
S["A1"]=cam(("0","52-4*T","230-26*T"),("0","sp.top+12","-21"),60); J["A1"]=setup()
S["A2"]=cam(("-45+8*T","42-3*T","200-24*T"),("0","sp.top+10","-21"),62); J["A2"]=setup()
S["A3"]=cam(("10","34-2*T","160-22*T"),("0","sp.top+6","-15"),64); J["A3"]=setup()
# B : la porte, perso qui entre (3/4)
S["B1"]=cam(("3.2-0.3*T","1.7","3.0-0.5*T"),("-0.5","1.6","-2"),58); J["B1"]=setup("0.3","1.6","ho+Math.PI+0.5")
# C : fenêtre qui saute, Mamie et perso dehors face caméra 3/4, camion
S["C1"]=cam(("-3.5+0.4*T","1.8","13-0.5*T"),("2","5.5","0"),62,0.35); J["C1"]=setup("0.8","9","ho+0.45","true","-0.5","7.4","ho+0.2")
S["C2"]=cam(("4+0.3*T","1.6","13.5-0.4*T"),("1","6","0"),64,0.35); J["C2"]=setup("0.8","9","ho-0.35","true","-0.5","7.4","ho-0.25")
# D : plan large, camion rouge, façade en feu, fumée
S["D1"]=cam(("20-1.5*T","4.5","24-0.5*T"),("5","7","0"),62); J["D1"]=setup("0.8","9","ho+0.45","true","-0.5","7.4","ho+0.2")
S["D2"]=cam(("-12+1.5*T","3.5","22"),("6","8","0"),64); J["D2"]=setup("0.8","9","ho+0.45","true","-0.5","7.4","ho+0.2")
S["A4"]=cam(("6","38-3*T","140-25*T"),("0","sp.top+8","-21"),62); J["A4"]=setup()
S["A5"]=cam(("-8+4*T","28-2*T","110-22*T"),("0","sp.top+6","-21"),62); J["A5"]=setup()
S["B2"]=cam(("-3+0.2*T","1.6","6-0.4*T"),("0.3","1.2","1.2"),56); J["B2"]=setup("0.3","1.8","ho+Math.PI+0.9")
S["C3"]=cam(("1","1.7","17-0.6*T"),("1.5","6.5","0"),62,0.35); J["C3"]=setup("0.8","9","ho+0.45","true","-0.5","7.4","ho+0.2")
S["C4"]=cam(("-2+0.3*T","1.6","15-0.5*T"),("1.5","6.8","0"),64,0.35); J["C4"]=setup("0.8","9","ho+0.6","true","-0.6","7.6","ho+0.1")
S["D3"]=cam(("24-1.2*T","5","20"),("8","8","0"),62); J["D3"]=setup("0.8","9","ho+0.45","true","-0.5","7.4","ho+0.2")
S["D4"]=cam(("26-1.2*T","3","22"),("10","6","0"),58); J["D4"]=setup("0.8","9","ho+0.45","true","-0.5","7.4","ho+0.2")
S["A6"]=cam(("2","30-1.5*T","100-20*T"),("1","sp.top+2","-10"),62); J["A6"]=setup()
S["A7"]=cam(("-6+3*T","34-2*T","120-24*T"),("1","sp.top+4","-12"),60); J["A7"]=setup()
RUN="window.__auto=(g)=>(window.__T0==null?{fwd:0,side:0}:{fwd:1,side:0});"
S["B3"]=cam(("1.6","1.7","0.9"),("0","1.3","6"),60); J["B3"]=setup("0.2","7.5","ho+Math.PI")+RUN
S["C5"]=cam(("1","1.7","17-0.6*T"),("1.5","6.5","0"),62,0.35); J["C5"]=setup("0.8","9","ho+0.9","true","-0.5","7.4","ho+0.3")
S["D5"]=cam(("14-1.0*T","4","26"),("8","7","0"),62); J["D5"]=setup("0.8","9","ho+0.45","true","-0.5","7.4","ho+0.2")
S["D6"]=cam(("30","4","15-0.8*T"),("10","7","2"),62); J["D6"]=setup("0.8","9","ho+0.45","true","-0.5","7.4","ho+0.2")
S["A8"]=cam(("120-30*T","6.5-0.6*T","10"),("0","sp.top","-6"),60); J["A8"]=setup(truck="false")
S["A9"]=cam(("110-26*T","9-1.0*T","14"),("0","sp.top+2","-8"),62); J["A9"]=setup(truck="false")
S["Bf"]=cam(("1.6","1.7","0.9+2.5*T"),("0.1","1.4","7.5"),60); J["Bf"]=setup("0.2","7.5","ho+Math.PI")
S["D7"]=cam(("19.5","4.5","23.5+0.6*T"),("5","7","0"),62); J["D7"]=setup("0.8","9","ho+0.45","true","-0.5","7.4","ho+0.2")
S["D8"]=cam(("19.5","5","23.5+0.6*T"),("9","3.5","5"),66); J["D8"]=setup("0.8","9","ho+0.45","true","-0.5","7.4","ho+0.2")
S["D9"]=cam(("17","6.5","25+0.6*T"),("8","4","4"),64); J["D9"]=setup("0.8","9","ho+0.45","true","-0.5","7.4","ho+0.2")
S["D10"]=cam(("19.5","5.5","23.5+0.6*T"),("9","0.3","5"),70); J["D10"]=setup("0.8","9","ho+0.45","true","-0.5","7.4","ho+0.2")
S["D11"]=cam(("19.5","5","23.5+0.6*T"),("8","1.5","4"),76); J["D11"]=setup("0.8","9","ho+0.45","true","-0.5","7.4","ho+0.2")
S["D12"]=cam(("19.5","2.0","23.5+0.6*T"),("9","2.0","5"),68); J["D12"]=setup("0.8","9","ho+0.45","true","-0.5","7.4","ho+0.2")
S["D13"]=cam(("20.5","2.5","25+0.6*T"),("9","2.6","5"),70); J["D13"]=setup("0.8","9","ho+0.45","true","-0.5","7.4","ho+0.2")
S["D14"]=cam(("19.5","2.0","23.5-0.5*T"),("9","2.0","5"),68); J["D14"]=setup("0.8","9","ho+0.45","true","-0.5","7.4","ho+0.2")
from h import shot
def MK(name,body,n=1,o=0,js="",wait=2500):
  k=[x for x in J if S[x]==body]
  return shot(name,body,dayT=DT,n=n,toff=o,wait=wait,js=js+(J[k[0]] if k else ""))
NEAR=""
