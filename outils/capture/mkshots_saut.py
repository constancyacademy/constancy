import sys,json; sys.path.insert(0,'/root/cap'); from mk import *
cam=open('/root/cap/camF.js').read().strip()
a=sys.argv  # job out name n w h CP
n=int(a[4]); w=int(a[5]); h=int(a[6]); CP=a[7]
js=setup(-30,750,3.14159,1111)+";window.__LOGF=1;window.__FW&&window.__FW.pts&&(window.__FW.pts.visible=false);window.__CP="+CP+";"+"{const W6=window.__W();W6.scene.traverse(o=>{if(o.isSprite&&o.material&&o.material.blending===2){o.visible=false;}});}"
job(a[1],'/root/cap/'+a[2],[shot(a[3],n,500,js,cam)],w,h)
