exec(open('/root/w/vi/sc4.py').read().split('\nnames=')[0])
a=math.atan2(-VZ,-VX)
c,s=math.cos(a),math.sin(a)
for h in (15,35,60):
  S["U%d"%h]=L(V(-c*20,h,-s*20+9),V("%f"%(c*1700),"40","%f"%(s*1700)),50); HL["U%d"%h]=0.3
S["U35w"]=L(V(-c*20,35,-s*20+9),V("%f"%(c*1700),"40","%f"%(s*1700)),62); HL["U35w"]=0.3
names=sys.argv[2].split(',')
shots=[MKI(k,S[k],hl=HL.get(k,0.45),ext=EXT.get(k,0)) for k in names]
for s in shots: s["fps"]=60; s["n"]=1
print(run(shots,sys.argv[1],w=540,h=960))
