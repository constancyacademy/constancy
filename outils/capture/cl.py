import json
hide=open('/home/claude/constancy/rushes/outils/capture/hide.js').read().strip()
fw="const W5=window.__W();W5.scene.traverse(o=>{if(o.isPoints&&o.material&&o.material.blending===2&&o.geometry){o.geometry.computeBoundingBox();if(o.geometry.boundingBox.max.y>100){o.visible=false;o.onBeforeRender=()=>{o.visible=false};}}});W5.scene.traverse(o=>{if((o.isPoints||o.isSprite)&&o.material&&o.material.blending===2){const v=new THREE.Vector3();o.getWorldPosition(v);if(v.y>90&&v.y<900)o.visible=false;}});W5.scene.traverse(o=>{const m=o.material;if(m&&m.uniforms&&m.uniforms.uK)m.visible=false;});try{Object.values(W5.beacons||{}).forEach(b=>{if(b)b.visible=false;});if(W5.destBeacon)W5.destBeacon.visible=false;if(W5.ownMark)W5.ownMark.visible=false;}catch(e){}"
notraf="{const W8=window.__W();W8.traffic.forEach(a=>{if(a.mesh)a.mesh.visible=false;});}"
def place(cars):
  s="{const W9=window.__W();window.__PC=window.__PC||[];window.__PC.forEach(g=>W9.scene.remove(g));window.__PC=[];"
  for cid,x,z,h in cars:
    s+="{const d=W9.CARS.find(c=>c.id=='%s');const g=W9.makeCar(d);g.position.set(%f,0,%f);g.rotation.y=%f;W9.scene.add(g);window.__PC.push(g);}"%(cid,x,z,h)
  return s+"}"
def cam(body,toff=0):
  return "(G)=>{const T=(performance.now()-(window.__T0||performance.now()))/1000+(%s);%s}"%(toff,body)
def shot(name,body,dayT=840,n=1,toff=0,wait=2500,js="",rain=0):
  return {"name":name,"n":n,"wait":wait,"dayT":dayT,"rain":rain,"js":hide+";"+fw+js,"camjs":cam(body,toff)}
def look(p,t,fov=60):
  return "return {p:[%f,%f,%f],t:[%f,%f,%f],fov:%f};"%(tuple(p)+tuple(t)+(fov,))
def job(path,out,shots,w=540,h=960,ev=None):
  d={"out":out,"w":w,"h":h,"shots":shots}
  if ev: d["eval"]=ev
  json.dump(d,open(path,'w'))
