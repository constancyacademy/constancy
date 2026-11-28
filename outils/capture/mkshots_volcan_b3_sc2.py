exec(open('/root/w/sc1.py').read().split('\nshots=')[0])
def TP(a,d,h,sh,ty,fov,dh=0,dd=0):
  c,s=math.cos(math.radians(a)),math.sin(math.radians(a)); rx,rz=s,-c
  return L(V("(%f)*((%f)-(%f)*T)"%(c,d,dd),"(%f)+(%f)*T"%(h,dh),"(%f)*((%f)-(%f)*T)"%(s,d,dd)),V(rx*sh,ty,rz*sh),fov)
S["c6"]=TP(80,176,2.2,22,140,16)
S["c6b"]=TP(80,176,2.2,30,150,22)
S["c7"]=TP(45,120,90,22,150,52)
S["c8"]=TP(45,150,120,20,140,55)
S["c9"]=TP(20,120,90,20,150,52)
S["c10"]=TP(60,100,105,24,150,55)
pa,pz=PA(80,166)
S["b5"]=CAMP+"return {p:[me.x+rx*7+fx*0.5,my+1.4,me.z+rz*7+fz*0.5],t:[me.x-rx*2+fx*40,my+12,me.z-rz*2+fz*40],fov:62};"; PL["b5"]=NORING+ME(pa,pz)
S["b6"]=CAMP+"return {p:[me.x-fx*9+rx*2,my+7,me.z-fz*9+rz*2],t:[me.x+fx*60-rx*3,my+20,me.z+fz*60-rz*3],fov:60};"; PL["b6"]=NORING+ME(pa,pz)
S["b7"]=CAMP+"return {p:[me.x-rx*7+fx*0.5,my+1.4,me.z-rz*7+fz*0.5],t:[me.x+rx*2+fx*40,my+12,me.z+rz*2+fz*40],fov:62};"; PL["b7"]=NORING+ME(pa,pz)
S["w1"]=TP(80,150,0.8,0,20,60)
shots=[MK(k,S[k]) for k in sys.argv[2].split(',')]
for s in shots: s["fps"]=60; s["n"]=int(sys.argv[3]) if len(sys.argv)>3 else 1
print(run(shots,sys.argv[1],w=540,h=960))
