exec(open('/root/w/vi/sc8.py').read().split('\nnames=')[0])
def AQ(a0,da,d0,dd,h0,dh,ty,fov,tp=0.0):
  T="(T-%f)"%tp
  return ("const a=(%f+(%f)*%s)*Math.PI/180;const d=%f-(%f)*%s;"%(a0,da,T,d0,dd,T))+L(V("Math.cos(a)*d","%f+(%f)*%s"%(h0,dh,T),"Math.sin(a)*d+6"),V(0,ty,6),fov)
def ORB2(a0,da,r,h,ty,fov,cz=6):
  return ("const a=(%f+(%f)*T)*Math.PI/180;"%(a0,da))+L(V("%f*Math.cos(a)"%r,h,"%f*Math.sin(a)+%f"%(r,cz)),V(0,ty,cz),fov)
# plan 1
S["W1"]=AQ(140,14,46,9,1.8,0.6,3.0,50)
S["W2"]=AQ(162,-14,46,9,1.8,0.6,3.0,50)
S["W3"]=AQ(150,10,40,6,2.5,0.0,3.0,50)
# salon
for k,(h,ty,fov) in {"N1":(1.5,2.8,66),"N2":(2.0,2.6,66),"N3":(1.7,3.2,70)}.items():
  S[k]=L(V("-9+6*T",h,-5.5),V("-6+7*T",ty,7),fov); HL[k]=0.22
# piscine
S["P7"]=L(V("-14+9*T",2.0,18),V("-10+9*T",0.5,6),60); HL["P7"]=0.25
S["P8"]=L(V("-12+8*T",4.5,12),V("-6+8*T",0.0,6),62); HL["P8"]=0.25
S["P9"]=L(V("-14+9*T",0.8,14),V("-10+9*T",2.0,5),60); HL["P9"]=0.25
# plan 5
S["Q5"]=ORB2(94,12,40,9,1.5,55)
S["Q6"]=ORB2(94,12,36,11,0.5,52)
names=sys.argv[2].split(',')
offs=[float(x) for x in sys.argv[3].split(',')] if len(sys.argv)>3 else [0,1.2]
shots=[MKI("x",S["W1"],hl=0.3)]; shots[0]["fps"]=60; shots[0]["n"]=1
for k in names:
  for o in offs:
    sh=MKI(k+"o%02d"%int(round(o*10)),S[k],o=o,hl=HL.get(k,0.3),ext=EXT.get(k,0)); sh["fps"]=60; sh["n"]=1; shots.append(sh)
print(run(shots,sys.argv[1],w=1080,h=1920))
