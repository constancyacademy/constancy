import json,sys
hide=open('/home/claude/rushes/outils/capture/hide.js').read().strip()
fix="try{const W2=window.__W();Object.values(W2.beacons||{}).forEach(b=>{if(b)b.visible=false;});if(W2.destBeacon)W2.destBeacon.visible=false;if(W2.ownMark)W2.ownMark.visible=false;}catch(e){}"
H="const L=(a,b,k)=>a.map((v,i)=>v+(b[i]-v)*k);const E=k=>k<0?0:k>1?1:(1-Math.pow(1-k,2));"
def camjs(body,toff=0): return "(G)=>{const T=(performance.now()-(window.__T0||performance.now()))/1000+%s;%s%s}"%(toff,H,body)
def job(path,out,shots,w,h): json.dump({"out":out,"w":w,"h":h,"shots":shots},open(path,'w'))
def shot(name,body,dayT,n=1,wait=3000,toff=0,far=0,rain=0): return {"name":name,"n":n,"wait":wait,"dayT":dayT,"js":hide+";"+fix,"camjs":camjs(body,toff),"far":far,"rain":rain}
