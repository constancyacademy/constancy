# monde_b1 / monde_b1B (sam. 28/11 12h et dim. 29/11 12h, M2 VRAI 3D, test A/B d'accroche) · safari (girafes, zèbres) au pied du Canyon Rouge, Venice Beach, le Mall (portes automatiques), puis vue haute
import os
exec(open('/root/cap/lib212.py').read())
DT=int(os.environ.get("DT","480"))
UNFPV="{const W6=window.__W();W6.G.fpv=false;W6.G.mode='play';}"
HB="{const W6=window.__W();if(!window.__HB){window.__HB=1;const H=o=>{if(o&&o.isObject3D)Object.defineProperty(o,'visible',{configurable:true,get:()=>false,set:()=>{}});};const B=W6.BANNER;if(B){H(B.g);H(B.plane);H(B.cloth);}}}"
NOME="{const W6=window.__W();const G=W6.G;if(!G.onFoot){G.car.v=0;W6.toggleCar();}G.onFoot=true;const mm=W6.meMesh;if(mm&&!mm.__h){mm.__h=1;Object.defineProperty(mm,'visible',{configurable:true,get:()=>false,set:()=>{}});}G.me.x=%s;G.me.z=%s;G.me.v=0;window.__auto=()=>({fwd:0,side:0});}"
def L(p,t,fov=60): return "return {p:[%s,%s,%s],t:[%s,%s,%s],fov:%s};"%(tuple(p)+tuple(t)+(fov,))
def MKM(name,body,n=1,o=0,js="",wait=6000,me=("330","860")):
  s=shot(name,body,dayT=DT,n=n,toff=o,wait=wait,js=NO+NOPLANE+HB+UNFPV+(NOME%me)+HIDELIGHTS+js); s["far"]=8000; return s
GH="const W7=window.__W();const gh=(x,z)=>W7.GH(x,z);"
S={}; ME={}
# SAFARI : caméra basse qui file entre les zèbres et les girafes, vers le Canyon Rouge (direction u = (-0,8 ; 0,6))
def saf(s0,v,h,ah,fov=66,dx=0,dz=0):
  return GH+("const ux=-0.8,uz=0.6,s=%s+%s*T;const x=1485+%s+ux*s,z=-1395+%s+uz*s;const y=gh(x,z)+%s;"%(s0,v,dx,dz,h))+L(("x","y","z"),("x+ux*30","y+%s"%ah,"z+uz*30"),fov)
S["S1"]=saf(-16,10,1.7,1.2)
S["S2"]=saf(-16,10,1.1,2.5,70,0,1.5)
S["S3"]=GH+"const a=0.9+0.25*T;const x=1485+Math.cos(a)*14,z=-1395+Math.sin(a)*14;const y=gh(x,z)+1.4;"+L(("x","y","z"),("1485","gh(1485,-1395)+3","-1395"),64)
# VENICE : au ras du sable, la foule de Muscle Beach
S["V1"]=GH+"const x=-444,z=188+8*T;"+L(("x","gh(x,z)+0.9","z"),("-462","gh(-462,z+30)+1.6","z+30"),62)
S["V2"]=GH+"const x=-430-1.5*T,z=236+7*T;"+L(("x","gh(x,z)+0.8","z"),("-470","1.5","215+7*T"),62)
S["V3"]=GH+"const x=-500+6*T,z=200;"+L(("x","gh(x,z)+1.0","z"),("x+25","2","232"),62)
# MALL : la caméra fonce vers les portes, qui s'ouvrent (le perso invisible arrive à la porte à T > 0,25)
MALLJS="if(T>0.25){W7.G.me.x=330;W7.G.me.z=1006;}else{W7.G.me.x=330;W7.G.me.z=860;}"
S["M1"]=GH+MALLJS+"const z=978+7*T;"+L(("330","3.26+2.2","z"),("330","3.26+3.2","z+30"),60)
S["M2"]=GH+MALLJS+"const z=970+6*T;"+L(("318+2*T","3.26+1.4","z"),("332","3.26+4.5","1011"),62)
# VUE HAUTE : la caméra s'élève devant le Mall et révèle la ville (vers le nord-est, sans la grande tour)
S["R1"]=GH+"const u=Math.min(1,T/2.5),e=u*u*(3-2*u);const y=4+150*e,z=985-40*e;"+L(("330","y","z"),("420","y*0.35","620"),62)
S["R2"]=GH+"const u=Math.min(1,T/2.5),e=u*u*(3-2*u);const y=6+170*e,z=980+50*e;"+L(("330+10*e","y","z"),("470","0","560"),60)
def MK(name,body,n=1,o=0,js="",wait=6000): return MKM(name,body,n,o,js,wait)
NEAR=""
# v2 : girafe + zèbres de près, Muscle Beach lisible (caméra au nord du panneau, vers le sud)
S["S4"]=GH+"const x=1506-9*T,z=-1392+3*T;const y=gh(x,z)+1.5;"+L(("x","y","z"),("1483","gh(1483,-1380)+3.2","-1380"),66)
S["S5"]=GH+"const x=1468+8*T,z=-1372-3*T;const y=gh(x,z)+1.3;"+L(("x","y","z"),("1488","gh(1488,-1395)+2.5","-1395"),66)
S["V4"]=GH+"const x=-440-2*T,z=262-7*T;"+L(("x","gh(x,z)+1.3","z"),("-454","gh(-454,214)+2.4","214"),62)
S["V5"]=GH+"const x=-425-1*T,z=250-7*T;"+L(("x","gh(x,z)+1.1","z"),("-458","gh(-458,214)+2.0","205"),64)
# v3 : vue haute au-dessus du viaduc, Venice vers la mer (ouest)
S["R3"]=GH+"const u=Math.min(1,T/4.2),e=1-(1-u)*(1-u);const y=45+150*e,z=990-50*e;"+L(("330","y","z"),("420","y*0.35","620"),62)
S["V6"]=GH+"const x=-424,z=212+6*T;"+L(("x","gh(x,z)+1.2","z"),("-480","1.4","z+4"),64)
S["V7"]=GH+"const x=-436,z=196+6*T;"+L(("x","gh(x,z)+0.9","z"),("-470","1.6","z+22"),64)
S["V8"]=GH+"const x=-400,z=150;"+L(("x","40","z"),("-460","0","230"),70)
# FINAL (60 i/s, pre 11 : image 0 à T = 0,2 s)
S["Sf"]=GH+"const x=1463+6*T,z=-1370.8-2.4*T;const y=gh(x,z)+1.3;"+L(("x","y","z"),("1488","gh(1488,-1395)+2.5","-1395"),66)
S["Vf"]=GH+"const U=Math.max(0,T-0.2);const x=-395-21*U,z=150+32*U,y=34-15*U;"+L(("x","y","z"),("-462","0","230"),70)
S["Mf"]=GH+MALLJS+"const z=978+7*T;"+L(("330","3.26+2.2","z"),("330","3.26+3.2","z+30"),60)
S["Rf"]=S["R3"]
# v4 safari : travelling latéral bas tout près des zèbres, girafe derrière (z = -1393, vers +z)
S["Sg"]=GH+"const x=1461+9*T,z=-1393.5;const y=gh(x,z)+1.0;"+L(("x","y","z"),("x+4","gh(x+4,-1378)+2.6","-1378"),64)
S["Sh"]=GH+"const x=1461+9*T,z=-1394.5;const y=gh(x,z)+1.4;"+L(("x","y","z"),("x+2","gh(x+2,-1380)+2.0","-1380"),70)
S["Sf2"]=GH+"const x=1465.2+9*T,z=-1393.5;const y=gh(x,z)+1.0;"+L(("x","y","z"),("x+4","gh(x+4,-1378)+2.6","-1378"),64)
S["Rf2"]=GH+"const u=Math.min(1,T/6.5),e=1-(1-u)*(1-u);const y=45+170*e,z=990-60*e;"+L(("330","y","z"),("420","y*0.35","620"),62)
