import sys; sys.path.insert(0,'/home/claude/rushes/outils/capture')
exec(open('/home/claude/rushes/outils/capture/mkshots_povconsole_repérage.py').read().split('if __name__')[0])
X=-40; DT=560
NO=CLOUD+open("/root/w/noufo.js").read()
pre=notraf+place([("or",X-46,LZ,math.pi/2)])+"window.__lt=null;"
body=carjs(X-40,27,LZ)+"const tx=Math.min(cx+1.5,%f+6);return {p:[%f,0.5,%f-3.6],t:[tx,0.85,%f],fov:55};"%(X,X,LZ,LZ)
def S_(name,b,n,js=""):
  s=shot(name,b,dayT=DT,n=n,toff=0,wait=4000,js=NO+js); s["far"]=20000; return s
sh=[shot("warm","return {p:[0,60,300],t:[0,20,0],fov:60};",dayT=DT),
 S_("pov2_car",body,72,pre),
 S_("pov2_heli","const M=window.__HM;const hx=-75+42*T,hz=-10,hy=165;M.position.set(hx,hy,hz);M.rotation.set(0,Math.PI/2,0.08);return {p:[hx-24+8*T,hy+9,hz+24],t:[hx+6,hy-6,hz],fov:60};",42,GRAB),
 S_("pov2_stade","return {p:[-175+100-48*T,46-6*T,985+62-10*T],t:[-175,8,985],fov:60};",42,"{const W8=window.__W();if(window.__HM)window.__HM.visible=false;}"),
 S_("pov2_drone","return {p:[430-85*T,150,430-25*T],t:[0,45,-40],fov:60};",46,"{if(window.__HM)window.__HM.visible=false;}"),
]
run(sh,'/root/w/pv2',w=1080,h=1920)
