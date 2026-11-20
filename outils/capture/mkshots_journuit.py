import json,sys
S="/tmp/claude-0/-home-claude-constancy/388fec11-a943-5647-9012-5c3a9b1c2ae2/scratchpad"
hide=open('/home/claude/rushes/outils/capture/hide.js').read().strip()
fw="W.scene.traverse(o=>{if(o.isPoints&&o.material&&o.material.blending===2&&o.geometry){o.geometry.computeBoundingBox();if(o.geometry.boundingBox.max.y>100){o.visible=false;o.onBeforeRender=()=>{o.visible=false};}}});W.scene.traverse(o=>{if((o.isPoints||o.isSprite)&&o.material&&o.material.blending===2){const v=new THREE.Vector3();o.getWorldPosition(v);if(v.y>90&&v.y<900)o.visible=false;}});"
P={
"P1":"return {p:[-452-4*T,10,70-55*T],t:[-575,52,-56-20*T],fov:64};",
"P2":"return {p:[-330+60*T,40+5*T,140-28*T],t:[28+20*T,58,-28],fov:58};",
"P3":"return {p:[228-12*T,31+2*T,-16-10*T],t:[204-12*T,22,-36-10*T],fov:62};",
"P4":"return {p:[-520,55-3*T,230-45*T],t:[-40,35,-80-45*T],fov:60};",
}
def cam(body,toff):
  return "(G)=>{const T=(performance.now()-(window.__T0||performance.now()))/1000+(%s);%s}"%(toff,body)
mode=sys.argv[1]; shots=[]
if mode=="scout":
  for n,b in P.items():
    if len(sys.argv)>2 and n not in sys.argv[2:]: continue
    for tag,dt in (("j",360),("n",840)):
      for toff in ((-0.7,1.4) if n=="P1" else (0.0,1.4)):
        shots.append({"name":f"se_{n}{tag}_{toff}","n":1,"one":True,"pre":0,"wait":2500,"dayT":dt,"js":hide+fw,"camjs":cam(b,toff)})
  json.dump({"out":S+"/scout","w":540,"h":960,"shots":shots},open(S+"/cap/q/e1.json","w"))
else:
  for n,b in P.items():
    if len(sys.argv)>2 and n not in sys.argv[2:]: continue
    d0=-0.7 if n=="P1" else 0.0
    shots.append({"name":f"{n}j","n":int(round((0.9-d0)*30)),"pre":0,"wait":3000,"dayT":360,"js":hide+fw,"camjs":cam(b,d0)})
    shots.append({"name":f"{n}n","n":27,"pre":0,"wait":3000,"dayT":840,"js":hide+fw,"camjs":cam(b,0.5)})
  json.dump({"out":S+"/full","w":1080,"h":1920,"shots":shots},open(S+"/cap/q/f_%s.json"%"_".join(sys.argv[2:] or ["all"]),"w"))
