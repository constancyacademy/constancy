import sys,json; sys.path.insert(0,sys.argv[1]); from mk import *
CL="W.enterClub();const PP=W.CLUBI.ppl;for(let it=0;it<3;it++)for(let i=1;i<23&&i<PP.length;i++)for(let j=i+1;j<23&&j<PP.length;j++){const a=PP[i].position,b=PP[j].position;const dx=b.x-a.x,dz=b.z-a.z,d=Math.hypot(dx,dz);if(d<1.25){const m=(1.3-d)/2;a.x-=dx/d*m;a.z-=dz/d*m;b.x+=dx/d*m;b.z+=dz/d*m;}}W.G.inside='club';if(W.CLUBI.g){W.CLUBI.g.visible=true;W.CLUBI.ppl.forEach(h=>h.visible=true);}"
# camera helper: club-local coords
def cam(body): return "const C=[3000,0,420];const A=(v)=>[v[0]+C[0],v[1],v[2]+C[2]];const W3=window.__W();W3.G.inside='club';"+body
S={
"A":(-0.9375,"const k=(T+0.9375)/2.8125;return {p:A(L([0,6.5,9.2],[0,5.0,5.0],k)),t:A(L([0,0.4,-3],[0,1.2,-8],k)),fov:70};",85),
"B":(0,"const k=T/1.40625;return {p:A(L([-3,2.3,-3.2],[-1.6,4.0,-4.4],k)),t:A(L([0,2.2,-9.8],[0,2.9,-9.8],k)),fov:66};",43),
"Cl":(0,"const k=T/0.9375;return {p:A(L([1.4,0.95,1.6],[1.0,1.05,0.6],k)),t:A(L([0,4.6,-9],[0,4.9,-9],k)),fov:72};",29),
"E":(0,"const k=T/0.9375;return {p:A(L([10.2,4.4,4.6],[10.2,4.5,1.6],k)),t:A(L([0,0.6,-3.5],[0,0.6,-5],k)),fov:66};",29),
"D":(0,"const k=T/1.875;return {p:A(L([-0.6,3.0,-7.85],[0.7,3.35,-7.3],k)),t:A(L([-0.3,0.7,4],[0.6,0.8,4],k)),fov:70};",57),
}
NOB=";W.CLUBI.beams.forEach(b=>b.visible=false);"
mode=sys.argv[2]; names=sys.argv[3].split(','); out=sys.argv[4]; jf=sys.argv[5]
sh=[]
for nm in names:
  st,b,n=S[nm]
  if mode=='scout':
    for to in (st, st+ (n/30)/2, st+n/30-0.05):
      s=shot("%s_%d"%(nm,int(to*100)),cam(b),840,wait=2500,toff=to); s["js"]+=";"+CL; sh.append(s)
  else:
    s=shot(nm,cam(b),840,n=n,wait=4000,toff=st-4/30); s["js"]+=";"+CL+(NOB if nm!="A" else ""); sh.append(s)
job(jf,out,sh,540 if mode=='scout' else 1080,960 if mode=='scout' else 1920)
