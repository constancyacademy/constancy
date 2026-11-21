import sys; sys.path.insert(0,'/root/cap')
from h import *
TX,TZ=-150,1422
S={
# A: depuis la mer, haut, fonce vers l'aéroport, piste + tour + ville derrière
"A":(45,"const k=T;return {p:[-620+70*k,150-30*k,1900-95*k],t:[-120+20*k,10,1380],fov:62};"),
# B: rase la piste vers +x
"B":(47,"return {p:[-560+85*T,7,1572],t:[-460+85*T,4,1520],fov:66};"),
# C: vigie 3/4, radar, piste derrière
"C":(36,"const th=-1.15+0.55*T;return {p:[%f+26*Math.cos(th),74,%f+26*Math.sin(th)],t:[%f,64,%f],fov:56};"%(TX,TZ-0,TX,TZ)),
# D: Terminal 3, travelling devant les portes
"D":(36,"return {p:[330+60*T,24,1505],t:[420+60*T,12,1430],fov:62};"),
# E: recul large
"E":(45,"const k=Math.min(1,T/1.5);const e=1-Math.pow(1-k,2);return {p:[-150+40*e,90+80*e,1700+160*e],t:[-80,10,1250],fov:62};"),
}

S["A2"]=(62,"return {p:[-800+120*T,74-20*T,1700-30*T],t:[-340+120*T,0,1490],fov:64};")
S["C2"]=(32,"const th=-1.9+0.5*T;return {p:[%f+36*Math.cos(th),68,%f+36*Math.sin(th)],t:[%f,60,%f],fov:54};"%(TX,TZ,TX,TZ))
S["D2"]=(47,"return {p:[340+55*T,42,1522],t:[420+55*T,14,1426],fov:62};")
S["A3"]=(62,"return {p:[-105-20*T,112-16*T,1850-125*T],t:[-150,38,1422],fov:62};")
sel=sys.argv[1].split(','); mode=sys.argv[2] if len(sys.argv)>2 else 'r'
shots=[]
for k in sel:
  n,b=S[k]
  if mode=='r':
    for t in (0,(n-1)/30): shots.append(shot("%s_t%02d"%(k,int(t*10)),b,dayT=840,toff=t,wait=1500,js=notraf))
  else: shots.append(shot("ap_"+k,b,dayT=840,n=n,wait=2500,js=notraf))
out='/root/cap/ap'+('f' if mode=='f' else 'r')
print(run(shots,out,w=1080 if mode=='f' else 540,h=1920 if mode=='f' else 960,wait=False))
