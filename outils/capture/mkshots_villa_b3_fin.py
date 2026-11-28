exec(open('/root/w/vi/b3s.py').read().split('\nnames=')[0])
P=151/60.
def ORB3(a0,da,r,h,ty,fov,cz=6):
  return ("const U=Math.max(0,T-%f);const a=(%f+(%f)*U)*Math.PI/180;"%(P,a0,da))+L(V("%f*Math.cos(a)"%r,h,"%f*Math.sin(a)+%f"%(r,cz)),V(0,ty,cz),fov)
S["Q9"]=ORB3(94,12,38,13,3.5,68); F["Q9"]=130; PRE={"Q9":150}
F["R3"]=80
names=sys.argv[2].split(',')
shots=[MKI("x",S["W1"],hl=0.3)]; shots[0]["fps"]=60; shots[0]["n"]=1
for k in names:
  sh=MKI(k,S[k],hl=HL.get(k,0.3),ext=EXT.get(k,0)); sh["fps"]=60; sh["n"]=F[k]
  if k in PRE: sh["pre"]=PRE[k]
  shots.append(sh)
print(run(shots,sys.argv[1],w=1080,h=1920))
