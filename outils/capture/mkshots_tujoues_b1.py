DT=int(os.environ.get("DT","480"))
def L(p,t,fov=60): return "return {p:[%s,%s,%s],t:[%s,%s,%s],fov:%s};"%(tuple(p)+tuple(t)+(fov,))
HB="{const W6=window.__W();if(!window.__HB){window.__HB=1;const H=o=>{if(o&&o.isObject3D)Object.defineProperty(o,'visible',{configurable:true,get:()=>false,set:()=>{}});};const B=W6.BANNER;if(B){H(B.g);H(B.plane);H(B.cloth);}W6.scene.traverse(o=>{if(o.isMesh&&o.material&&o.material.blending===2&&o.geometry){o.geometry.computeBoundingBox();const bb=o.geometry.boundingBox;if(o.scale.y*(bb.max.y-bb.min.y)>100)H(o);}});(W6.JW&&W6.JW.beams||[]).forEach(b=>H(b.isObject3D?b:(b.m||b.mesh)));}}"
def MK(name,body,n=1,o=0,js="",wait=2500):
  s=shot(name,body,dayT=DT,n=n,toff=o,wait=wait,js=NO+NOPLANE+HB+js); s["far"]=20000; return s
S={}
S["OV"]=L(("-180","140","1640"),("-180","0","1480"),70)
S["OV2"]=L(("-180","25","1560"),("-180","5","1440"),65)
S["OV3"]=L(("100","25","1560"),("100","5","1440"),65)
CX,CZ,CH=-130.0,1490.0,-math.pi/2
PX,PZ=float(os.environ.get("PX","-124")),float(os.environ.get("PZ","1497"))
TE=float(os.environ.get("TE","1.2")); TD=float(os.environ.get("TD","2.6"))
INIT=("{const W6=window.__W(),G=W6.G;G.mode='play';G.fpv=false;W6.P.car='suv';if(!W6.P.cars.includes('suv'))W6.P.cars.push('suv');"
 "if(!G.onFoot){G.car.v=0;G.entering=null;W6.toggleCar();}"
 "if(!G.parked){G.parked={x:0,z:0,h:0,mesh:null};}"
 "if(!window.__SUVOK){W6.setCar('suv');window.__SUVOK=1;}"
 "G.parked.x=%f;G.parked.z=%f;G.parked.h=%f;const m=G.parked.mesh;m.position.set(%f,Math.max(0,W6.GH(%f,%f)),%f);m.rotation.set(0,%f,0);m.visible=true;"
 "G.entering=null;G.wantExit=false;G.me.x=%f;G.me.z=%f;G.me.h=Math.atan2((%f)-(%f),(%f)-(%f));G.car.v=0;window.__ENT=0;"
 "window.__auto=(g)=>{if(window.__T0==null)return {fwd:0,side:0};const T=(performance.now()-window.__T0)/1000;"
 "if(T<%f)return {fwd:1,side:0};if(!window.__ENT){window.__ENT=1;try{W6.toggleCar();}catch(e){}}if(T<%f)return {fwd:0,side:0};return {fwd:1,side:0};};}"
 )%(CX,CZ,CH,CX,CX,CZ,CZ,CH,PX,PZ,CX,PX,CZ+1.6,PZ,TE,TD)
ST="const W7=window.__W(),G7=W7.G;window.__LM=G7.mode;G7.mode='play';const ox=G7.onFoot?G7.me.x:G7.car.x,oz=G7.onFoot?G7.me.z:G7.car.z;window.__LOGS=window.__LOGS||[];window.__LOGS.push([+T.toFixed(2),G7.onFoot,+G7.me.x.toFixed(2),+G7.me.z.toFixed(2),+G7.car.x.toFixed(2),+G7.car.z.toFixed(2),+(G7.car.v||0).toFixed(1),!!G7.entering,window.__LM]);"
S["T1"]=ST+L(("-127","9","1515"),("-128","0.8","1490"),55)
# ---- simulation complète (une seule prise) ----
CX,CZ,CH=-130.0,1490.0,-math.pi/2
PX,PZ=-124.4,1494.8
INIT2=("{const W6=window.__W(),G=W6.G;G.mode='play';window.__LOGS=[];G.fpv=false;W6.P.car='suv';if(!W6.P.cars.includes('suv'))W6.P.cars.push('suv');window.__auto=null;"
 "if(!G.onFoot){G.car.v=0;G.entering=null;G.wantExit=false;W6.toggleCar();}G.doorClose=null;"
 "W6.setCar('suv');"
 "G.parked.x=%f;G.parked.z=%f;G.parked.h=%f;const m=G.parked.mesh;m.position.set(%f,Math.max(0,W6.GH(%f,%f)),%f);m.rotation.set(0,%f,0);m.visible=true;"
 "G.entering=null;G.me.x=%f;G.me.z=%f;G.me.v=0;G.me.h=Math.atan2((%f)-(%f),(%f)-(%f));G.car.v=0;W6.meMesh.visible=true;"
 "{const om=W6.ownMark;if(om&&!om.__h){om.__h=1;Object.defineProperty(om,'visible',{configurable:true,get:()=>false,set:()=>{}});}}window.__PH=0;window.__lt2=null;window.__SL=null;"
 "window.__auto=(g)=>{if(window.__T0==null)return {fwd:0,side:0};const ph=window.__PH;if(ph===0)return {fwd:0.1,side:0};if(ph===2)return {fwd:1,side:0};return {fwd:0,side:0};};}"
 )%(CX,CZ,CH,CX,CX,CZ,CZ,CH,PX,PZ,CX,PX,CZ+1.6,PZ)
SIM=("const W7=window.__W(),G7=W7.G;window.__LM2=G7.mode;G7.mode='play';if(window.__lt2==null)window.__lt2=T;const dt=T-window.__lt2;window.__lt2=T;"
 "if(dt>0){const n=Math.max(1,Math.round(dt*30));for(let i=0;i<n;i++){const st=dt/n;"
 " if(window.__PH===0){const dx=G7.parked.x+Math.cos(G7.parked.h)*1.6-G7.me.x,dz=G7.parked.z-Math.sin(G7.parked.h)*1.6-G7.me.z;const d=Math.hypot(dx,dz);G7.me.h=Math.atan2(dx,dz);if(d<0.35){window.__PH=1;window.__SL={t:0,x:G7.me.x,z:G7.me.z};}}"
 " if(window.__PH===1){const S=window.__SL;S.t+=st;const k=Math.min(1,S.t/0.45);G7.me.h=G7.parked.h+Math.PI;G7.me.x=S.x+(G7.parked.x-S.x)*k*0.55;G7.me.z=S.z+(G7.parked.z-S.z)*k*0.55;G7.me.v=0;"
 "  if(k>=1){const p=G7.parked;W7.meMesh.visible=false;W7.scene.remove(p.mesh);G7.car.x=p.x;G7.car.z=p.z;G7.car.h=p.h;G7.car.v=0;G7.parked=null;G7.onFoot=false;G7.ride={kind:'none'};W7.setCar('suv');G7.ride={kind:'own'};window.__PH=2;}}"
 " if(window.__PH===1){W7.meMesh.position.set(G7.me.x,0.25-Math.min(1,window.__SL.t/0.55)*0.35,G7.me.z);W7.meMesh.rotation.y=G7.me.h;}"
 " if(window.__PH>=2)W7.meMesh.visible=false;}}"
 "const P0=G7.parked||{x:G7.car.x,z:G7.car.z,h:G7.car.h};const car=G7.onFoot?P0:G7.car;const ch=car.h,fx=Math.sin(ch),fz=Math.cos(ch),sx=Math.cos(ch),sz=-Math.sin(ch);const cx=car.x,cz=car.z,cy=W7.GH(cx,cz);"
 "window.__LOGS=window.__LOGS||[];window.__LOGS.push([+T.toFixed(2),window.__LM2,+(G7.me.v||0).toFixed(2),window.__PH,+G7.me.x.toFixed(1),+G7.me.z.toFixed(1),+cx.toFixed(1),+cz.toFixed(1),+(G7.car.v||0).toFixed(1)]);"
 )
CAMS=("if(T<2.3333){const mx=(cx+G7.me.x)/2,mz=(cz+G7.me.z)/2;const a=-0.45-0.25*T;return {p:[mx+13*Math.sin(a),2.4,mz+13*Math.cos(a)],t:[mx,1.0,mz],fov:50};}"
 "if(T<4.0){return {p:[%f,0.6,%f],t:[cx,cy+0.8,cz],fov:56};}"
 "if(T<5.7){return {p:[cx-fx*6,cy+2.1,cz-fz*6],t:[cx+fx*8,cy+0.8,cz+fz*8],fov:60};}"
 "if(T<7.4){return {p:[cx+sx*8+fx*1.5,cy+1.3,cz+sz*8+fz*1.5],t:[cx,cy+0.8,cz],fov:56};}"
 "return {p:[cx+fx*10+sx*4,cy+1.5,cz+fz*10+sz*4],t:[cx+fx*2,cy+2.4,cz+fz*2],fov:56};")%(CX-14,CZ+4.2)
S["SIM"]=SIM+CAMS
def dcam(f,s,y,ty,fov): 
  return ("const W7=window.__W(),G7=W7.G;const car=G7.parked||G7.car;const ch=car.h,fx=Math.sin(ch),fz=Math.cos(ch),sx=Math.cos(ch),sz=-Math.sin(ch);const cx=car.x,cz=car.z,cy=W7.GH(cx,cz);"
   "return {p:[cx+fx*%f+sx*%f,cy+%f,cz+fz*%f+sz*%f],t:[cx+fx*2,cy+%f,cz+fz*2],fov:%f};")%(f,s,y,f,s,ty,fov)
S["D1"]=dcam(10,4,1.5,2.4,56)
S["D2"]=dcam(9,4,1.8,2.6,52)
