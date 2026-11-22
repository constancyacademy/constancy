exec(open('/root/w/s/m4_lib.py').read())
TW="const k=Math.min(1,T/1.65);const D=34+560*Math.pow(1-k,1.6);const dx=0.857,dz=0.514;return {p:[28+dx*D,128+40*(1-k),-28+dz*D],t:[28,118+30*(1-k),-28],fov:58};"
sh=[shot("warm","return {p:[0,60,300],t:[0,20,0],fov:60};",dayT=840),S_("m4_tower",TW,50,pre="{if(window.__PC)window.__PC.forEach(g=>g.visible=false);}")]
print(run(sh,'/root/w/m4t',w=1080,h=1920,wait=False))
