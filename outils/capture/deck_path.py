import math,json
def crPts(K,step):
  out=[]
  for i in range(len(K)-1):
    p0=K[max(0,i-1)];p1=K[i];p2=K[i+1];p3=K[min(len(K)-1,i+2)]
    L=math.hypot(p2[0]-p1[0],p2[1]-p1[1]); n=max(2,math.ceil(L/step))
    for k in range(n):
      t=k/n;t2=t*t;t3=t2*t
      out.append([0.5*(2*p1[j]+(-p0[j]+p2[j])*t+(2*p0[j]-5*p1[j]+4*p2[j]-p3[j])*t2+(-p0[j]+3*p1[j]-3*p2[j]+p3[j])*t3) for j in (0,1)])
  out.append(list(K[-1][:2])); return out
def deckSample(K,step=4):
  P2=crPts([k[:2] for k in K],step); L=[0]
  for i in range(1,len(P2)): L.append(L[-1]+math.hypot(P2[i][0]-P2[i-1][0],P2[i][1]-P2[i-1][1]))
  KL=[0]
  for i in range(1,len(K)): KL.append(KL[-1]+math.hypot(K[i][0]-K[i-1][0],K[i][1]-K[i-1][1]))
  sc=L[-1]/KL[-1]; S=[]
  for i,p in enumerate(P2):
    s=L[i]/sc; j=0
    while j<len(K)-2 and KL[j+1]<s: j+=1
    t=min(1,max(0,(s-KL[j])/max(1e-6,KL[j+1]-KL[j]))); e=t*t*(3-2*t)
    S.append([p[0],p[1],K[j][2]+(K[j+1][2]-K[j][2])*e])
  return S
F110=[[-500,1185,8],[-440,1166,12],[-320,1128,19],[-120,1066,22],[100,1000,22],[300,950,22],[500,922,18],[640,916,12],[760,930,8]]
