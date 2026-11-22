import sys,json; sys.path.insert(0,'/root/cap'); from h import *
X,Z=330,-975
SETUP="""{const W6=window.__W();const G6=W6.G,U6=W6.UFO;const x=%f,z=%f;G6.onFoot=true;G6.me.x=x;G6.me.z=z;G6.me.h=%f;const mm=W6.meMesh;if(mm){if(mm.parent!==W6.scene)W6.scene.add(mm);mm.position.set(x,W6.GH(x,z)+0.25,z);mm.rotation.set(0,0,0);mm.visible=true;}U6.st=null;U6.leave=null;if(U6.crew)U6.crew.forEach(a=>a.visible=false);if(U6.dome){U6.dome.material.opacity=0.85;U6.dome.material.depthWrite=true;}U6.beam.visible=false;U6.mesh.rotation.set(0,0,0);G6.ufoRide={t:0,x:x,z:z,gy:W6.GH(x,z)%s};G6.farT=0;window.__RT0=%f;}"""
PRE="""const W6=window.__W(),R6=W6.G.ufoRide,U6=W6.UFO;if(R6)R6.t=window.__RT0+T;if(U6.crew&&!U6.__bp){U6.__bp=1;U6.crew.forEach(a=>{const b=a.userData&&a.userData.bub;if(b)Object.defineProperty(b,'visible',{configurable:true,get:()=>false,set:()=>{}});});}const M6=U6.mesh.position;"""
def setup(t0,h=0.0,dest=None):
  d="" if dest is None else ",dest:{x:%f,z:%f}"%dest
  return SETUP%(X,Z,h,d,t0)
if __name__=="__main__":
  shots=[]
  for nm,t0,body in [
    ("a48",4.8,"return {p:[%f,8,%f],t:[M6.x,M6.y,M6.z],fov:62};"%(X-60,Z+70)),
    ("a30",3.0,"return {p:[%f,8,%f],t:[M6.x,M6.y,M6.z],fov:62};"%(X-60,Z+70)),
    ("b62",6.2,"return {p:[%f,12,%f],t:[M6.x,M6.y-10,M6.z],fov:62};"%(X-45,Z+55)),
    ("c20",7.2+20,"return {p:[M6.x+14,M6.y+6,M6.z+14],t:[M6.x,M6.y,M6.z],fov:60};"),
    ("d15",7.2+15,"return {p:[M6.x+40,M6.y+25,M6.z+40],t:[M6.x,M6.y-30,M6.z],fov:62};"),
  ]:
    shots.append(shot(nm,body,dayT=840,n=1,wait=1500,js=setup(t0),pre=PRE))
  r=run(shots,'/root/w/u1',ev="(()=>{const R=window.__W().G.ufoRide;return R?{dest:R.dest,plan:R.plan,T:R.T}:null})()")
  print(r)
