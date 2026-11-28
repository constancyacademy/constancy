exec(open('/root/w/vi/fin.py').read().split('\nnames=')[0])
def AP(a,d0,dd,h0,dh,ty,fov):
  c,s=math.cos(math.radians(a)),math.sin(math.radians(a))
  return L(V("(%f)*(%f-(%f)*T)"%(c,d0,dd),"%f+(%f)*T"%(h0,dh),"(%f)*(%f-(%f)*T)+6"%(s,d0,dd)),V(0,ty,6),fov)
S["J1"]=AP(135,62,20,1.5,0.6,1.5,50)
S["J2"]=AP(120,58,20,3.0,0.0,1.0,50)
S["J3"]=AP(150,62,20,2.5,0.5,1.2,50)
S["J4"]=AP(105,50,16,2.5,0.3,1.2,52)
names=sys.argv[2].split(',')
shots=[]
for k in names:
  for o in (0,1.2):
    sh=MKI(k+"o%d"%int(o*10),S[k],o=o,hl=0.3); sh["fps"]=60; sh["n"]=1; shots.append(sh)
print(run(shots,sys.argv[1],w=540,h=960))
