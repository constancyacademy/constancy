import json,sys,math
hide=open('/home/claude/constancy/rushes/outils/capture/hide.js').read().strip()
fix="try{const W2=window.__W();Object.values(W2.beacons||{}).forEach(b=>{if(b)b.visible=false;});if(W2.destBeacon)W2.destBeacon.visible=false;if(W2.ownMark)W2.ownMark.visible=false;window.__FW&&window.__FW.pts&&(window.__FW.pts.visible=false);}catch(e){}"
grab="{const W4=window.__W();W4.scene.traverse(o=>{const m=o.material;if(m&&m.uniforms&&m.uniforms.uK)m.visible=false;});W4.scene.traverse(o=>{const m=o.material;if(o.isMesh&&m&&m.blending===THREE.AdditiveBlending&&o.geometry){if(!o.geometry.boundingBox)o.geometry.computeBoundingBox();const bb=o.geometry.boundingBox;if(bb.max.y-bb.min.y>120||bb.max.x-bb.min.x>120&&false)m.visible=false;}});(W4.JW&&W4.JW.beams||[]).forEach(o=>o.b.traverse(x=>{if(x.material)x.material.visible=false;}));const W3=window.__W();if(!window.__HM){window.__HM=W3.life.heli.mesh;W3.life.heli.mesh=new THREE.Group();}}"
# helper inside camjs: HP(T) -> heli pos/yaw ; set mesh
def camjs(heli, cam, toff=0):
  return "(G)=>{const W=window.__W();const T=(performance.now()-(window.__T0||performance.now()))/1000+%s;const E=k=>k<0?0:k>1?1:k*k*(3-2*k);const LH=(x,z)=>W.landH(x,z);%s;const M=window.__HM;M.position.set(hx,hy,hz);M.rotation.set(hp||0,hyaw,hr||0,'YXZ');%s}"%(toff,heli,cam)
def job(out,w,h,shots): return {"out":out,"w":w,"h":h,"shots":shots}
def shot(name,n,dayT,heli,cam,toff=0,wait=2500):
  return {"name":name,"n":n,"wait":wait,"dayT":dayT,"js":hide+fix+grab,"camjs":camjs(heli,cam,toff),"far":6000}
