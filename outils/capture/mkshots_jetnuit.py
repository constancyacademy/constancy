import sys,json; sys.path.insert(0,'/root/cap'); from h import *
JET=open('/root/w/jet_js.txt').read()
CLOUD="{const W6=window.__W();if(!window.__NCL){window.__NCL=1;W6.scene.traverse(o=>{if(o.isInstancedMesh&&o.material&&o.material.uniforms&&o.material.uniforms.sheet){Object.defineProperty(o,'visible',{configurable:true,get:()=>false,set:()=>{}});}});}}"
# jet along -x on z=112 at y=34, chase cam behind-right-above
S={
"city":"const J=window.__JET;J.visible=true;const x=330-85*T;J.position.set(x,34,112);J.rotation.set(0,-Math.PI/2,0);J.rotation.z=0.10*Math.sin(T*2.2);return {p:[x+32,41,112+9],t:[x-20,37,112-1],fov:60};",
"lake":"const J=window.__JET;J.visible=true;const z=-1780-80*T;const wy=105;J.position.set(-1080,wy+7,z);J.rotation.set(0,Math.PI,0);J.rotation.z=-0.35;return {p:[-1080-16,wy+4,z-10+4*T],t:[-1080,wy+7,z],fov:60};",
"pins":"const J=window.__JET;J.visible=true;const z=-1780-80*T;J.position.set(-1080,140,z);J.rotation.set(0,Math.PI,0);J.rotation.z=-0.3;return {p:[-1080-30,144,z+20],t:[-1080,139,z-4],fov:60};",
"peak":"const J=window.__JET;J.visible=true;const x=-260+95*T;J.position.set(x,300,-1720);J.rotation.set(0,Math.PI/2,0);J.rotation.z=0.3;return {p:[x-34+20*T,308,-1660],t:[x+10,299,-1760],fov:60};",
"mont":"const J=window.__JET;J.visible=true;const x=-320+90*T;J.position.set(x,120,-1600);J.rotation.set(0,Math.PI/2,0);J.rotation.z=0.25;return {p:[x-10+30*T,112,-1540],t:[x,118,-1640],fov:60};",
"city2":"const J=window.__JET;J.visible=true;const x=150-85*T;J.position.set(x,30,112);J.rotation.set(0,-Math.PI/2,0);J.rotation.z=0.15*Math.sin(T*2);return {p:[40,6,121],t:[x-8,26,112],fov:62};",
"tour2":"const J=window.__JET;J.visible=true;const a=-0.6+0.55*T,R=95;const x=28+R*Math.cos(a),z=-28+R*Math.sin(a);J.position.set(x,120,z);J.rotation.set(0,-a,0);J.rotation.z=0.5;const b=a-0.25;return {p:[28+62*Math.cos(b),112,-28+62*Math.sin(b)],t:[x,126,z],fov:62};",
"city3":"const J=window.__JET;J.visible=true;const x=-330+85*T;J.position.set(x,34,-168);J.rotation.set(0,Math.PI/2,0);J.rotation.z=-0.10*Math.sin(T*2.2);return {p:[x-32,41,-168-9],t:[x+20,37,-168+1],fov:60};",
"tour":"const J=window.__JET;J.visible=true;const a=-0.6+0.55*T,R=95;const x=28+R*Math.cos(a),z=-28+R*Math.sin(a);J.position.set(x,120,z);J.rotation.set(0,-a,0);J.rotation.z=0.5;return {p:[x+32*Math.cos(a),116,z+32*Math.sin(a)],t:[28,134,-28],fov:62};",
}
def mk(k,n=1,o=0,name=None,dt=840):
  s=shot(name or "%s_%02d"%(k,int(o*10)),S[k],dayT=dt,n=n,toff=o,wait=1500,js=JET+CLOUD+open('/root/w/noufo.js').read()); s["far"]=20000; return s
if __name__=="__main__" and len(sys.argv)>3:
  sel=sys.argv[1].split(','); offs=[float(v) for v in sys.argv[2].split(',')]; out=sys.argv[3]
  run([mk(k,o=o) for k in sel for o in offs],out)
  from PIL import Image
  import glob
  rows=[]
  for k in sel:
    fs=sorted(glob.glob(out+'/'+k+'_*.png')); rows.append([Image.open(f).resize((270,480)) for f in fs])
  Wd=max(len(r) for r in rows); I=Image.new('RGB',(270*Wd,480*len(rows)))
  for j,r in enumerate(rows):
    for i,im in enumerate(r): I.paste(im,(i*270,j*480))
  I.save(out+'.png')
