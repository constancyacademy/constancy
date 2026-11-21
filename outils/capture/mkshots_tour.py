from h import *
import sys
TX,TZ=-150,1422
S={
"tour_montee":(61,"const y=2.5+32*T;const th=1.35+0.4*T;return {p:[%f+27*Math.cos(th),y,%f+27*Math.sin(th)],t:[%f,y+10,%f],fov:60};"%(TX,TZ,TX,TZ)),
"tour_orbite-vigie":(31,"const th=1.2+0.9*T;return {p:[%f+24*Math.cos(th),72,%f+24*Math.sin(th)],t:[%f,63,%f],fov:58};"%(TX,TZ,TX,TZ)),
"tour_piste-avion":(32,"return {p:[%f+4+9*T,76-4*T,%f+12+3*T],t:[%f+90+6*T,0,%f+20],fov:62};"%(TX,TZ,TX,TZ)),
"tour_ville-large":(31,"return {p:[%f+58-12*T,88-5*T,%f+84-9*T],t:[%f-8,32,%f-95],fov:62};"%(TX,TZ,TX,TZ)),
"tour_recul":(47,"const k=T/1.6;const e=1-Math.pow(1-k,2);return {p:[%f+16+56*e,68+30*e,%f+22+70*e],t:[%f-10*e,58-8*e,%f-30*e],fov:58};"%(TX,TZ,TX,TZ)),
}
sel=sys.argv[1].split(',')
w,h=(1080,1920) if (len(sys.argv)>2 and sys.argv[2]=='full') else (540,960)
shots=[]
for k in sel:
  n,b=S[k]
  if w==540: 
    for t in (0, (n-1)/30): shots.append(shot("%s_t%02d"%(k,int(t*10)),b,dayT=840,toff=t,wait=1500,js=notraf))
  else: shots.append(shot(k,b,dayT=840,n=n,wait=2500,js=notraf))
print(run(shots,'/root/cap/s1'+('f' if w==1080 else 'r'),w=w,h=h))
