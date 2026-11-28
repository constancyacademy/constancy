exec(open('/root/w/vi/sc1.py').read().split('\nnames=')[0])
for i in range(8):
  a=i*45; c,s=math.cos(math.radians(a)),math.sin(math.radians(a))
  S["R%d"%a]=L(V("%f"%(c*45),2.0,"%f"%(s*45)),V(0,3,0),45); EXT["R%d"%a]=1
S["T1"]=L(V(0,60,0.1),V(0,0,0),70); EXT["T1"]=1
names=sys.argv[2].split(',')
shots=[MKI(k,S[k],hl=HL.get(k,0.45),ext=EXT.get(k,0)) for k in names]
for s in shots: s["fps"]=60; s["n"]=1
print(run(shots,sys.argv[1],w=540,h=960))
