import sys,json; sys.path.insert(0,'/root/cap')
exec(open('/root/cap/jrec.py').read().split('shots=[')[0])
MONT="const J=window.__JET;J.visible=true;const z=-1300-85*T;J.position.set(-22,98.5,z);J.rotation.set(0,Math.PI,0);J.rotation.z=0.15*Math.sin(T*2);return {p:[-22,105,z+30],t:[-22,93.5,z-190],fov:60};"
shots=[J("warm","return {p:[0,60,300],t:[0,20,0],fov:60};"), J("jet2_montE",MONT,n=48,w=9000)]
run(shots,'/root/w/jf',w=1080,h=1920)
