import sys,os,json,time
sys.path.insert(0,'/root/cap'); exec(open('/root/cap/lib212.py').read())
DT=int(os.environ.get("DT","840"))
VX,VY,VZ=-1710.2023,2.4,537.6719
HC=("{const W9=window.__W();W9.scene.traverse(o=>{if(o.userData&&o.userData.isCar&&!o.__hid){o.__hid=1;Object.defineProperty(o,'visible',{configurable:true,get:()=>false,set:()=>{}});}});"
    "W9.scene.traverse(o=>{if(o.isPoints&&o.material&&Math.abs(o.material.size-0.32)<1e-6&&!o.__h){o.__h=1;Object.defineProperty(o,'visible',{configurable:true,get:()=>false,set:()=>{}});}});}")
def L(p,t,fov=60): return "return {p:[%s,%s,%s],t:[%s,%s,%s],fov:%s};"%(tuple(p)+tuple(t)+(fov,))
def V(dx,y,dz): return ("%f+(%s)"%(VX,dx),"%f+(%s)"%(VY,y),"%f+(%s)"%(VZ,dz))
def MK(name,body,n=1,o=0,js="",wait=3000):
  s=shot(name,"const W7=window.__W();"+body,dayT=DT,n=n,toff=o,wait=wait,js=NO+NOPLANE+notraf+HC+js); s["far"]=20000; return s
S={}
