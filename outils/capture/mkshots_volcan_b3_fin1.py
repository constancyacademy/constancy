exec(open('/root/w/sc4.py').read().split('\nshots=')[0])
S["P2a"]=TP(45,135,38,30,115,58,dh=7,dd=12)
S["P2b"]=TP(30,150,18,25,100,55,dh=8,dd=14)
a,d=58,188
c,s=math.cos(math.radians(a)),math.sin(math.radians(a)); rx,rz=s,-c
x,z=VX+c*d,VZ+s*d
S["P5a"]="const W7b=window.__W();const gy=W7b.GH(%f,%f);"%(x,z)+L(("%f"%x,"gy+1.7","%f"%z),V(rx*14,"128+2*T",rz*14),"(27-3*T)")
px,pz=PA(58,184)
S["P4a"]=CAMP+"const b=7-1.2*T;return {p:[me.x-fx*b+rx*2.0,my+1.8,me.z-fz*b+rz*2.0],t:[me.x+fx*60-rx*9,my+14,me.z+fz*60-rz*9],fov:62};"; PL["P4a"]=NORING+ME(px,pz)
names=sys.argv[2].split(',')
shots=[MK("x",S["x"])]+[MK(k,S[k]) for k in names]
shots[0]["n"]=1
for s in shots[1:]: s["fps"]=60; s["n"]=int(sys.argv[3])
shots[0]["fps"]=60
print(run(shots,sys.argv[1],w=1080,h=1920))
