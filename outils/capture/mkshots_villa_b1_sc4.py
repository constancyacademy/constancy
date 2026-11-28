exec(open('/root/w/vi/sc3.py').read().split('\nnames=')[0])
for a in (-30,0,30,60,90,120,150):
  c,s=math.cos(math.radians(a)),math.sin(math.radians(a))
  S["D%d"%a]=L(V(0,4.5,9),V("%f"%(c*600),"30","%f"%(9+s*600)),58); HL["D%d"%a]=0.3
names=sys.argv[2].split(',')
shots=[MKI(k,S[k],hl=HL.get(k,0.45),ext=EXT.get(k,0)) for k in names]
for s in shots: s["fps"]=60; s["n"]=1
print(run(shots,sys.argv[1],w=540,h=960))
