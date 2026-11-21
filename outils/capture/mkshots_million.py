from h import *
import sys,math
LX=395.6
CAR="{const W9=window.__W();if(!window.__CC){const d=W9.CARS.find(c=>c.id=='nacre');const g=W9.makeCar(d);W9.scene.add(g);window.__CC=g;}window.__CC.visible=true;window.__lt=null;}"
def carjs(Z0,V):
  return "const W7=window.__W();const g=window.__CC;const cz=%f-%f*T;g.position.set(%f,0,cz);g.rotation.y=Math.PI;if(window.__lt!=null&&T>window.__lt){W7.spinWheels(g,%f,0,T-window.__lt);}window.__lt=T;"%(Z0,V,LX,V)
S={
"front":carjs(300,30)+"return {p:[%f+0.3,0.55,cz-7.5+1.2*T],t:[%f,0.75,cz],fov:52};"%(LX,LX),
"profil":carjs(250,30)+"return {p:[%f-6,0.6,cz-1.2],t:[%f,0.5,cz-1.2],fov:46};"%(LX,LX),
"drone":carjs(320,30)+"return {p:[%f+14,16,cz+18],t:[%f,0.5,cz-6],fov:60};"%(LX,LX),
"arriere":carjs(280,30)+"return {p:[%f-1.2,2.6,cz+8.5],t:[%f,0.7,cz-1],fov:58};"%(LX,LX),
"haut":"return {p:[395,140,200],t:[395,0,120],fov:60};",
}
if __name__=="__main__":
  sel=sys.argv[1].split(','); toffs=[float(x) for x in sys.argv[2].split(',')]; dt=int(sys.argv[3]) if len(sys.argv)>3 else 630
  shots=[]
  for k in sel:
    for t in toffs: shots.append(shot("%s_t%02d"%(k,int(t*10)),S[k],dayT=dt,toff=t,wait=1500,js=notraf+CAR))
  print(run(shots,'/root/cap/s5',wait=False))
