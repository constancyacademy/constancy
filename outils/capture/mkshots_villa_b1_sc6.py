exec(open('/root/w/vi/sc5.py').read().split('\nnames=')[0])
S["P1"]=L(V(-6,0.9,8.0),V(10,0.0,30),62); HL["P1"]=0.25
S["P2"]=L(V(8,1.2,8.5),V(-6,0.0,30),62); HL["P2"]=0.25
S["P3"]=L(V(0,3.5,4),V(0,-1.0,20),60); HL["P3"]=0.25
S["P4"]=L(V(-10,1.0,10),V(20,0.5,14),60); HL["P4"]=0.25
S["P5"]=L(V(12,6,22),V(0,0,6),55); HL["P5"]=0.25
S["P6"]=L(V(-14,5,24),V(0,0.5,5),55); HL["P6"]=0.25
names=sys.argv[2].split(',')
shots=[MKI(k,S[k],hl=HL.get(k,0.45),ext=EXT.get(k,0)) for k in names]
for s in shots: s["fps"]=60; s["n"]=1
print(run(shots,sys.argv[1],w=540,h=960))
