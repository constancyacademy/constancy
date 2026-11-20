import json
hide=open('/home/claude/constancy/rushes/outils/capture/hide.js').read().strip()
fw="const W5=window.__W();W5.scene.traverse(o=>{if(o.isPoints&&o.material&&o.material.blending===2&&o.geometry){o.geometry.computeBoundingBox();if(o.geometry.boundingBox.max.y>100){o.visible=false;o.onBeforeRender=()=>{o.visible=false};}}});W5.scene.traverse(o=>{if((o.isPoints||o.isSprite)&&o.material&&o.material.blending===2){const v=new THREE.Vector3();o.getWorldPosition(v);if(v.y>90&&v.y<900)o.visible=false;}});W5.scene.traverse(o=>{const m=o.material;if(m&&m.uniforms&&m.uniforms.uK)m.visible=false;});try{Object.values(W5.beacons||{}).forEach(b=>{if(b)b.visible=false;});if(W5.destBeacon)W5.destBeacon.visible=false;if(W5.ownMark)W5.ownMark.visible=false;}catch(e){}"
def cam(body,toff=0,sw=None):
  s="" if sw is None else "const W6=window.__W();if(W6.P){W6.P.dayT=(T<%f?360:840);}"%sw
  return "(G)=>{const T=(performance.now()-(window.__T0||performance.now()))/1000+(%s);%s%s}"%(toff,s,body)
def shot(name,body,dayT,n=1,toff=0,sw=None,wait=2500):
  return {"name":name,"n":n,"wait":wait,"dayT":dayT,"js":hide+";"+fw,"camjs":cam(body,toff,sw)}
def job(path,out,shots,w,h): json.dump({"out":out,"w":w,"h":h,"shots":shots},open(path,'w'))
