exec(open('/root/w/vi/fin2.py').read().split('\nnames=')[0])
def ORB(a0,da,r,h,ty,fov,cz=6):
  return ("const a=(%f+(%f)*T)*Math.PI/180;"%(a0,da))+L(V("%f*Math.cos(a)"%r,h,"%f*Math.sin(a)+%f"%(r,cz)),V(0,ty,cz),fov)
S["Q1"]=ORB(200,12,45,22,0,55)
S["Q2"]=ORB(100,-12,40,16,0,55)
S["Q3"]=ORB(160,12,38,10,1,55)
S["Q4"]=ORB(60,-12,40,14,0,55)
names=sys.argv[2].split(',')
shots=[]
for k in names:
  sh=MKI(k,S[k],hl=0.3); sh["fps"]=60; sh["n"]=1; shots.append(sh)
print(run(shots,sys.argv[1],w=540,h=960))
