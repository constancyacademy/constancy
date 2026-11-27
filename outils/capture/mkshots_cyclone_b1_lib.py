import sys,os,json,time
sys.path.insert(0,'/root/cap'); exec(open('/root/cap/lib212.py').read())
DT=int(os.environ.get("DT","600"))
CYJ=("{const W9=window.__W();if(W9.CY.on&&(W9.CY.st==='fin'||(W9.CY.ppl||[]).some(q=>!q.b))){(W9.CY.ppl||[]).forEach(q=>{if(q.m)W9.scene.remove(q.m);if(q.b)W9.scene.remove(q.b);});W9.cyClean();W9.G.wxForce=null;}if(!W9.CY.on){W9.CY.forced=1;W9.cyStart(true);}W9.CY.st='go';W9.CY.t=10;W9.G.wxForce=0.95;W9.WX.rain=0.8;"
     "W9.scene.traverse(o=>{if(o.userData&&o.userData.isCar&&!o.__hid&&!(W9.CY.cars||[]).some(q=>q.m===o)){o.__hid=1;Object.defineProperty(o,'visible',{configurable:true,get:()=>false,set:()=>{}});}});"
     "W9.scene.traverse(o=>{if(o.isPoints&&o.material&&Math.abs(o.material.size-0.32)<1e-6&&!o.__h){o.__h=1;Object.defineProperty(o,'visible',{configurable:true,get:()=>false,set:()=>{}});}});}")
def TOR(x,z): return "const TG=W7.CY.grp;const tx=%s,tz=%s;if(TG){TG.position.set(tx,W7.GH(tx,tz),tz);}"%(x,z)
def L(p,t,fov=60): return "return {p:[%s,%s,%s],t:[%s,%s,%s],fov:%s};"%(tuple(p)+tuple(t)+(fov,))
def MK(name,body,n=1,o=0,js="",wait=3000):
  s=shot(name,body,dayT=DT,n=n,toff=o,wait=wait,rain=0.8,js=NO+NOPLANE+notraf+CYJ+js); s["far"]=20000; return s
S={}
