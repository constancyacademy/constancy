exec(open('/root/w/vi/sc2.py').read().split('\nnames=')[0])
for a in (60,90,120):
  c,s=math.cos(math.radians(a)),math.sin(math.radians(a))
  S["G%d"%a]=L(V("%f"%(c*32),2.5,"%f"%(s*32)),V(0,2.5,0),50); HL["G%d"%a]=0.3
S["H1"]=L(V(-5.0,1.6,-5.4),V(-3,1.3,7),70); HL["H1"]=0.22
S["H2"]=L(V(-9,1.6,6.2),V(8,1.4,-2),70); HL["H2"]=0.22
S["H3"]=L(V(9.5,1.7,-5.5),V(-4,1.0,4),72); HL["H3"]=0.22
S["H4"]=L(V(0,1.5,5.0),V(0,0.0,30),66); HL["H4"]=0.22
S["C3"]=L(V(4,1.7,8),V("%f"%(ux*400),"25","%f"%(uz*400)),55); HL["C3"]=0.22
names=sys.argv[2].split(',')
shots=[MKI(k,S[k],hl=HL.get(k,0.45),ext=EXT.get(k,0)) for k in names]
for s in shots: s["fps"]=60; s["n"]=1
print(run(shots,sys.argv[1],w=540,h=960))
