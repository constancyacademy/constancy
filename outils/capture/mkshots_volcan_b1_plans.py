def ME(dx,dz):
  x="%f+(%s)"%(VX,dx); z="%f+(%s)"%(VZ,dz)
  return ("{const W6=window.__W(),G=W6.G;G.mode='play';G.fpv=false;if(!G.onFoot){G.car.v=0;G.entering=null;G.wantExit=false;W6.toggleCar();}G.doorClose=null;G.entering=null;"
          "G.me.x=%s;G.me.z=%s;G.me.v=0;G.me.h=Math.atan2(-(%f-G.me.z),(%f-G.me.x))+Math.PI;W6.meMesh.visible=true;window.__auto=(g)=>({fwd:0,side:0});}")%(x,z,VZ,VX)
PL={}
S["P1"]=L(V(18,2.2,176),V(0,100,0),55); PL["P1"]=ME(10,168)
S["P2"]=L(V(4,1.8,160),V(10,1.4,168),50); PL["P2"]=ME(10,168)
S["P3"]=L(V(-15,2.0,190),V(0,110,0),52); PL["P3"]=ME(10,168)
_MK=MK
def MK(name,body,n=1,o=0,js="",wait=3000):
  k=[x for x in PL if S[x]==body]
  return _MK(name,body,n=n,o=o,js=js+(PL[k[0]] if k else ""),wait=wait)
S["A7"]=L(V("140-22*T","200-10*T","0"),V(0,"135+4*T",0),55)
S["B4"]=L(V(330,3,60),V(0,62,0),36)
S["P4"]=L(V(15,1.7,164),V(5,2.6,168),58); PL["P4"]=ME(10,168)
S["P5"]=L(V(13,1.7,162),V(0,95,0),50); PL["P5"]=ME(10,168)
S["B5"]=L(V(240,2.5,40),V(0,70,0),46)
S["P6"]=L(V(18,1.6,166),V(2,8,140),60); PL["P6"]=ME(10,168)
S["P7"]=L(V("21-1.2*T",1.5,"160+0.6*T"),V(0,40,60),62); PL["P7"]=ME(10,168)
def MEW(dx,dz):
  return ME(dx,dz).replace("window.__auto=(g)=>({fwd:0,side:0});","window.__auto=(g)=>{if(window.__T0==null)return {fwd:0,side:0};return {fwd:0.1,side:0};};")
CAMP="const G7=W7.G,me=G7.me,my=W7.GH(me.x,me.z);const ux=%f-me.x,uz=%f-me.z,ul=Math.hypot(ux,uz),fx=ux/ul,fz=uz/ul,rx=-fz,rz=fx;"%(VX,VZ)
S["P8"]=CAMP+"return {p:[me.x+rx*3.2-fx*3.2,my+1.9,me.z+rz*3.2-fz*3.2],t:[%f,85,%f],fov:58};"%(VX,VZ); PL["P8"]=MEW(10,184)
S["P9"]=CAMP+"return {p:[me.x-rx*3.4-fx*2.6,my+1.7,me.z-rz*3.4-fz*2.6],t:[%f,85,%f],fov:58};"%(VX,VZ); PL["P9"]=MEW(10,184)
S["Q1"]=("const u=Math.min(T,1.4),d=3*u-0.6*u*u+0.15*Math.max(0,T-1.4);const sx=13-0.12*d,sz=166-0.99*d;"
         +L(V("sx","1.7","sz"),V(0,"92+4*T",0),52))
S["Q2"]=("const u=Math.min(T,1.4),d=3*u-0.6*u*u+0.15*Math.max(0,T-1.4);const sx=17-0.12*d,sz=166-0.99*d;"
         +L(V("sx","1.7","sz"),V(-6,"148+3*T",0),58))
