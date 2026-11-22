import sys,json; sys.path.insert(0,'/root/cap'); from h import *
CLOUD="{const W6=window.__W();if(!window.__NCL){window.__NCL=1;W6.scene.traverse(o=>{if(o.isInstancedMesh&&o.material&&o.material.uniforms&&o.material.uniforms.sheet){Object.defineProperty(o,'visible',{configurable:true,get:()=>false,set:()=>{}});}});}}"
DT=1140
S={
"wideF":"return {p:[300-75*T,38-3*T,760-25*T],t:[60-40*T,40,40],fov:60};",
"roofC":"return {p:[-188+16-6*T,31,-76+18+3*T],t:[-188,24,-76],fov:62};",
"roofC4":"return {p:[204-18+6*T,31,-36+16+3*T],t:[204,23.5,-36],fov:62};",
"mall2":"return {p:[330-150+22*T,66-4*T,1082-160+12*T],t:[330,26,1082],fov:60};",
"roof3":"return {p:[-188+32-10*T,36-2*T,-76+30+8*T],t:[-188,25,-76],fov:62};",
"roof4":"return {p:[204-32+10*T,36-2*T,-36+30+8*T],t:[204,24,-36],fov:62};",
"wide2":"return {p:[-90+14*T,4,600-4*T],t:[0,45,-30],fov:62};",
"mall":"return {p:[330-150+22*T,70-4*T,1082+150-14*T],t:[330,30,1082],fov:60};",
"roof":"return {p:[132+34-12*T,34-2*T,187+30+6*T],t:[132,19,187],fov:62};",
"roof2":"return {p:[-35+34-12*T,40-2*T,-203+30+6*T],t:[-35,26,-203],fov:62};",
"letters":"return {p:[22+10*T,3.2,628],t:[90+4*T,6,600],fov:60};",
"skate":"return {p:[-175-10*T,6+1*T,450-6*T],t:[-170,1,486],fov:62};",
"venice":"return {p:[-445,1.3,230+9*T],t:[-430,2,300+9*T],fov:62};",
"wide":"return {p:[260-22*T,70,780-6*T],t:[0,35,60],fov:60};",
}
if __name__=="__main__" and len(sys.argv)>3:
  sel=sys.argv[1].split(','); offs=[float(v) for v in sys.argv[2].split(',')]; out=sys.argv[3]
  shots=[]
  for k in sel:
    for o in offs:
      s=shot("%s_%02d"%(k,int(o*10)),S[k],dayT=DT,n=1,toff=o,wait=1200,js=CLOUD); s["far"]=20000; shots.append(s)
  run(shots,out)
  from PIL import Image
  import glob
  rows=[]
  for k in sel:
    fs=sorted(glob.glob(out+'/'+k+'_*.png')); rows.append([Image.open(f).resize((270,480)) for f in fs])
  Wd=max(len(r) for r in rows); I=Image.new('RGB',(270*Wd,480*len(rows)))
  for j,r in enumerate(rows):
    for i,im in enumerate(r): I.paste(im,(i*270,j*480))
  I.save(out+'.png')
