import math,sys; sys.path.insert(0,'/root/cap/lib'); from cl import *
CARS=[(133,-90),(148,-90),(133,-77),(148,-77),(128,-83),(152,-83),(140,-86)]
def orb(cx,cz,R=5.5,h=1.5,th0=0.8,w=1.6,ty=0.7,fov=55):
  return "const th=%f+%f*T;return {p:[%f+%f*Math.cos(th),%f,%f+%f*Math.sin(th)],t:[%f,%f,%f],fov:%f};"%(th0,w,cx,R,h,cz,R,cx,ty,cz,fov)
S3=orb(140,-86,R=9,h=5.2,ty=3.4,fov=52,th0=0.6,w=1.1)
S4="return {p:[122+4*T,6.5+1.5*T,-102],t:[142+2*T,1,-81],fov:62};"
S5="return {p:[136-2*T,3.6,-55+6*T],t:[134,3.0,-76],fov:55};"
HIDEP="{const W4=window.__W();const v=new THREE.Vector3();W4.scene.traverse(o=>{if(o.isSkinnedMesh){o.getWorldPosition(v);if(Math.hypot(v.x-140,v.z-83+0)<0&&false){} if(Math.hypot(v.x-140,v.z+83)<22){let p=o;while(p.parent&&p.parent!==W4.scene)p=p.parent;p.visible=false;p.onBeforeRender=()=>{};}}});}"
S4="return {p:[131+3*T,8.5,-97+2*T],t:[147,0.5,-78],fov:64};"
S5="return {p:[139-2*T,3.6,-55+6*T],t:[143,3.0,-76],fov:55};"
S3=orb(140,-86,R=9,h=5.2,ty=3.4,fov=52,th0=2.0,w=1.1)
HIDEP="{const W4=window.__W();const v=new THREE.Vector3();W4.scene.children.forEach(o=>{if(o.userData&&o.userData.rig){o.getWorldPosition(v);if(Math.hypot(v.x-140,v.z+83)<16){o.scale.set(0.0001,0.0001,0.0001);}}});}"
S3=orb(140,-86,R=9,h=5.2,ty=3.4,fov=52,th0=0.6,w=1.1)
R1=orb(128,-83,R=6.8,h=2.7,ty=1.3,fov=52,th0=0.8,w=1.6)
R2=orb(152,-83,R=6.8,h=2.7,ty=1.3,fov=52,th0=0.8,w=1.6)
HIDEGT="{const W3=window.__W();const v=new THREE.Vector3();W3.scene.children.forEach(o=>{if(o.userData&&o.userData.carId=='gt'){o.getWorldPosition(v);if(Math.hypot(v.x-140,v.z+83)<20)o.scale.set(0.0001,0.0001,0.0001);}});}"
R1b=orb(128,-83,R=5.6,h=2.6,ty=1.3,fov=56,th0=0.8,w=1.6)
R1c=orb(128,-83,R=5.6,h=2.6,ty=1.3,fov=56,th0=-0.3,w=1.3)
