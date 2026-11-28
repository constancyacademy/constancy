exec(open('/root/w/fin1.py').read().split('\nnames=')[0])
S["P2c"]=TP(45,140,30,30,118,58,dh=16,dd=22)
S["P2d"]=TP(42,150,60,30,118,58,dh=-18,dd=20)
S["P5b"]="const W7b=window.__W();const gy=W7b.GH(%f,%f);"%(x,z)+L(("%f"%x,"gy+1.7","%f"%z),V(rx*12,"121+2*T",rz*12),"(28-3*T)")
S["P2e"]=TP(42,155,70,30,118,58,dh=-30,dd=28)
names=sys.argv[2].split(',')
shots=[MK("x",S["x"])]+[MK(k,S[k]) for k in names]
for s in shots[1:]: s["fps"]=60; s["n"]=int(sys.argv[3])
shots[0]["fps"]=60
print(run(shots,sys.argv[1],w=1080,h=1920))
