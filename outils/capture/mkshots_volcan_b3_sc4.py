exec(open('/root/w/sc3.py').read().split('\nshots=')[0])
def TPG(a,d,hag,sh,ty,fov):
  c,s=math.cos(math.radians(a)),math.sin(math.radians(a)); rx,rz=s,-c
  x,z=VX+c*d,VZ+s*d
  return "const W7b=window.__W();const gy=W7b.GH(%f,%f);"%(x,z)+L(("%f"%x,"gy+%f"%hag,"%f"%z),V(rx*sh,ty,rz*sh),fov)
for i,a in enumerate([50,58,65]):
  d={50:194,58:188,65:182}[a]
  S["f%d"%i]=TPG(a,d,1.7,14,134,26)
  px,pz=PA(a,d-4)
  S["g%d"%i]=CAMP+"return {p:[me.x-fx*6+rx*1.2,my+1.9,me.z-fz*6+rz*1.2],t:[me.x+fx*60+rx*6,my+40,me.z+fz*60+rz*6],fov:58};"; PL["g%d"%i]=NORING+ME(px,pz)
shots=[MK(k,S[k]) for k in sys.argv[2].split(',')]
for s in shots: s["fps"]=60; s["n"]=int(sys.argv[3]) if len(sys.argv)>3 else 1
print(run(shots,sys.argv[1],w=540,h=960))
