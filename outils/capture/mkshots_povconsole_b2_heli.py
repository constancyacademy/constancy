import sys; sys.path.insert(0,'/home/claude/rushes/outils/capture')
exec(open('/home/claude/rushes/outils/capture/mkshots_povconsole_repérage.py').read().split('if __name__')[0])
NO=CLOUD+open("/root/w/noufo.js").read()+"{if(window.__PC)window.__PC.forEach(g=>g.visible=false);}"
HB="const M=window.__HM;M.visible=true;const hx=-75+42*T,hz=-10,hy=134;M.position.set(hx,hy,hz);M.rotation.set(0,Math.PI/2,0.08);return {p:[hx-34+8*T,182-4*T,hz-37],t:[hx+6,146.5,hz],fov:60};"
s1=shot("pov6_heli",HB,dayT=560,n=44,wait=4000,js=NO+GRAB); s1["far"]=20000
print(run([shot("warm","return {p:[0,60,300],t:[0,20,0],fov:60};",dayT=560),s1],'/root/w/pv10',w=1080,h=1920,wait=False))
