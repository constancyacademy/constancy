import sys,math; sys.path.insert(0,'/root/cap')
from h import *
NOPAN="{const e=document.getElementById('screen');if(e){e.classList.add('hidden');e.innerHTML='';}}"
NOCL="{const W7=window.__W();W7.scene.traverse(o=>{if(o.isInstancedMesh&&o.renderOrder===-1&&o.material&&o.material.uniforms&&o.material.uniforms.sheet){Object.defineProperty(o,'visible',{get:()=>false,set:()=>{},configurable:true});}});}"
def body(pitch,D0,D1,dur,tx=-1610,fov=62):
    a=math.radians(pitch)
    return ("const k=Math.min(1,T/%f),D=%f+(%f)*k;return {p:[%f+D*%f,D*%f,330],t:[%f,0,330],fov:%f};"
            %(dur,D0,D1-D0,tx,math.cos(a),math.sin(a),tx,fov))
if __name__=="__main__":
    mode=sys.argv[1]
    if mode=='prev':
        shots=[]
        for nm,pt in [("p50",50),("p45",45),("p56",56)]:
            b=body(pt,1850,1450,2.0667)
            for t in (0.5,2.0):
                shots.append(dict(shot("%s_t%02d"%(nm,int(t*10)),b,dayT=630,n=1,toff=t,wait=3000,js=notraf+NOPAN+NOCL),far=6000))
        print(run(shots,'/root/wk/prev2',wait=False))
    else:
        pt=float(sys.argv[2]); n=62
        b=body(pt,1900,1300,2.0667)
        shots=[dict(shot("pa2_A",b,dayT=630,n=n,wait=3000,js=notraf+NOPAN+NOCL),far=6000)]
        print(run(shots,'/root/wk/full',w=1080,h=1920,wait=False))
