exec(open('/root/w/v2/base.py').read())
import math
def CR(a,r0,dr,h0,dh,sh,ty,fov):
  c,s=math.cos(math.radians(a)),math.sin(math.radians(a)); rx,rz=s,-c
  return L(V("(%f)*((%f)-(%f)*T)"%(c,r0,dr),"(%f)-(%f)*T"%(h0,dh),"(%f)*((%f)-(%f)*T)"%(s,r0,dr)),V(rx*sh,ty,rz*sh),fov)
NORING="{const W6=window.__W();W6.scene.traverse(o=>{if(o.isMesh&&o.geometry&&o.geometry.type==='RingGeometry'&&o.geometry.parameters&&Math.abs(o.geometry.parameters.innerRadius-0.8)<1e-6&&!o.__h){o.__h=1;Object.defineProperty(o,'visible',{configurable:true,get:()=>false,set:()=>{}});}});}"
def PA(a,d): c,s=math.cos(math.radians(a)),math.sin(math.radians(a)); return (c*d,s*d)
S["x"]=L(V(0,300,300),V(0,0,0),60)
S["c1"]=CR(70,170,0,85,0,25,135,55)
S["c2"]=CR(100,170,0,85,0,-25,135,55)
S["c3"]=CR(60,120,0,110,0,20,140,50)
S["c4"]=CR(80,150,0,60,0,0,120,60)
S["c5"]=CR(30,140,0,95,0,25,130,52)
px,pz=PA(80,166)
S["b1"]=CAMP+"return {p:[me.x-fx*6+rx*1.5,my+1.2,me.z-fz*6+rz*1.5],t:[me.x+fx*60,my+25,me.z+fz*60],fov:60};"; PL["b1"]=NORING+ME(px,pz)
S["b2"]=CAMP+"return {p:[me.x-fx*4+rx*4,my+0.9,me.z-fz*4+rz*4],t:[me.x+fx*60-rx*4,my+40,me.z+fz*60-rz*4],fov:62};"; PL["b2"]=NORING+ME(px,pz)
qx,qz=PA(80,160)
S["b3"]=L(V(qx,"0.6",qz),V(0,"60",0),60)
S["b4"]=CAMP+"return {p:[me.x+fx*8+rx*3,my+1.5,me.z+fz*8+rz*3],t:[me.x,my+1.4,me.z],fov:60};"; PL["b4"]=NORING+ME(px,pz)
shots=[MK(k,S[k]) for k in sys.argv[2].split(',')]
for s in shots: s["fps"]=60; s["n"]=int(sys.argv[3]) if len(sys.argv)>3 else 1
print(run(shots,sys.argv[1],w=540,h=960))
