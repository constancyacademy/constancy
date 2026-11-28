import math
def ME(dx,dz):
  x="%f+(%s)"%(VX,dx); z="%f+(%s)"%(VZ,dz)
  return ("{const W6=window.__W(),G=W6.G;G.mode='play';G.fpv=false;if(!G.onFoot){G.car.v=0;G.entering=null;G.wantExit=false;W6.toggleCar();}G.doorClose=null;G.entering=null;"
          "G.me.x=%s;G.me.z=%s;G.me.v=0;G.me.h=Math.atan2(-(%f-G.me.z),(%f-G.me.x))+Math.PI;W6.meMesh.visible=true;window.__auto=(g)=>({fwd:0,side:0});}")%(x,z,VZ,VX)
def MEW(dx,dz):
  return ME(dx,dz).replace("window.__auto=(g)=>({fwd:0,side:0});","window.__auto=(g)=>{if(window.__T0==null)return {fwd:0,side:0};return {fwd:0.1,side:0};};")
PL={}
_MK=MK
def MK(name,body,n=1,o=0,js="",wait=3000):
  k=[x for x in PL if S[x]==body]
  return _MK(name,body,n=n,o=o,js=js+(PL[k[0]] if k else ""),wait=wait)
CAMP="const G7=W7.G,me=G7.me,my=W7.GH(me.x,me.z);const ux=%f-me.x,uz=%f-me.z,ul=Math.hypot(ux,uz),fx=ux/ul,fz=uz/ul,rx=-fz,rz=fx;"%(VX,VZ)
