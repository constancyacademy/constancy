import sys,math,json; sys.path.insert(0,'/root/cap'); from h import *
CLOUD="{const W6=window.__W();if(!window.__NCL){window.__NCL=1;W6.scene.traverse(o=>{if(o.isInstancedMesh&&o.material&&o.material.uniforms&&o.material.uniforms.sheet){Object.defineProperty(o,'visible',{configurable:true,get:()=>false,set:()=>{}});}});}}"
NO=CLOUD+open("/root/w/noufo.js").read()
PRE="const W6=window.__W();const g=W6.REX.d.g;const P=(g.position.lengthSq()>1)?g.position:new THREE.Vector3(W6.REX.d.cx,W6.GH(W6.REX.d.cx,W6.REX.d.cz),W6.REX.d.cz);const hh=g.rotation.y;const fx=Math.sin(hh),fz=Math.cos(hh),sx=Math.cos(hh),sz=-Math.sin(hh);"
def rel(f,s,u,tf,ts,tu,fov=55):
  return "return {p:[P.x+fx*(%s)+sx*(%s),P.y+(%s),P.z+fz*(%s)+sz*(%s)],t:[P.x+fx*(%s)+sx*(%s),P.y+(%s),P.z+fz*(%s)+sz*(%s)],fov:%s};"%(f,s,u,f,s,tf,ts,tu,tf,ts,fov)
def mk(name,body,n=1,o=0,dt=840,js="",wait=2500):
  s=shot(name,body,dayT=dt,n=n,toff=o,wait=wait,js=NO+js,pre=PRE); s["far"]=20000; return s
EV="(()=>{const W=window.__W();const R=W.REX;const d=R.d;if(!d)return {nod:1,c:R.c};const g=d.g;const b=new THREE.Box3().setFromObject(g);let sk=0,bones=0;g.traverse(o=>{if(o.isSkinnedMesh)sk++;if(o.isBone)bones++;});return {key:d.key,p:g.position.toArray(),ry:g.rotation.y,sc:g.scale.toArray(),min:b.min.toArray(),max:b.max.toArray(),sk,bones,c:R.c,R:R.R,gate:R.gate,cx:d.cx,cz:d.cz,r:d.r,GH:W.GH(g.position.x,g.position.z)}})()"
def pol(dphi,rad,h,ty,fov=55,tside=0):
  # caméra sur un cercle autour du centre de l'enclos, à l'angle a + dphi (a = angle du Rex), visée sur le Rex
  return "const d6=W6.REX.d;const A=d6.a+(%s);const cxx=d6.cx+Math.cos(A)*(%s),czz=d6.cz+Math.sin(A)*(%s);return {p:[cxx,P.y+(%s),czz],t:[P.x+sx*(%s),P.y+(%s),P.z+sz*(%s)],fov:%s};"%(dphi,rad,rad,h,tside,ty,tside,fov)
def polf(dphi,rad,h,ty,fov=55):
  # angle de caméra FIXE (compense la marche du Rex d.s rad/s)
  return "const d6=W6.REX.d;const A=d6.a-d6.s*T+(%s);const cxx=d6.cx+Math.cos(A)*(%s),czz=d6.cz+Math.sin(A)*(%s);return {p:[cxx,P.y+(%s),czz],t:[P.x,P.y+(%s),P.z],fov:%s};"%(dphi,rad,rad,h,ty,fov)
def PIN(a0): return "W6.REX.d.a=(%s)+W6.REX.d.s*T;"%a0
def polp(a0,dphi,rad,h,ty,fov=55):
  # Rex épinglé à l'angle a0 au début du plan (il marche ensuite normalement), caméra fixe à a0+dphi
  return PIN(a0)+"const d6=W6.REX.d;const A=(%s)+(%s);const cxx=d6.cx+Math.cos(A)*(%s),czz=d6.cz+Math.sin(A)*(%s);return {p:[cxx,P.y+(%s),czz],t:[P.x,P.y+(%s),P.z],fov:%s};"%(a0,dphi,rad,rad,h,ty,fov)
