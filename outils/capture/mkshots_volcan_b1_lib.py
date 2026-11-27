import sys,os,json,time
sys.path.insert(0,'/root/cap'); exec(open('/root/cap/lib212.py').read())
DT=int(os.environ.get("DT","840"))
VX,VZ=-39.6485,-3332.4706
ERU=("{const W9=window.__W();if(!W9.VOL.on){W9.volStart(true);window.__ERU=0;}if(!window.__ERU){window.__ERU=1;for(let i=0;i<%d;i++)W9.updateVolcano(0.05);}W9.VOL.t=12;W9.VOL.fin=null;W9.scene.traverse(o=>{if(o.isPoints&&o.material&&Math.abs(o.material.size-0.32)<1e-6&&!o.__h){o.__h=1;Object.defineProperty(o,'visible',{configurable:true,get:()=>false,set:()=>{}});}});"
     "W9.scene.traverse(o=>{if(o.userData&&o.userData.isCar&&!o.__hid){o.__hid=1;Object.defineProperty(o,'visible',{configurable:true,get:()=>false,set:()=>{}});}});}")%int(os.environ.get("PREV","300"))
def L(p,t,fov=60): return "return {p:[%s,%s,%s],t:[%s,%s,%s],fov:%s};"%(tuple(p)+tuple(t)+(fov,))
def MK(name,body,n=1,o=0,js="",wait=3000):
  s=shot(name,"const W7=window.__W();"+body,dayT=DT,n=n,toff=o,wait=wait,js=NO+NOPLANE+notraf+ERU+js); s["far"]=20000; return s
def V(dx,y,dz): return ("%f+(%s)"%(VX,dx),str(y),"%f+(%s)"%(VZ,dz))
S={}
