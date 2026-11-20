import math,sys; sys.path.insert(0,'/root/cap/lib'); from cl import *
A="return {p:[1170-15*T,1.8,175-3*T],t:[1060-10*T,3,132],fov:58};"
B="const th=-0.4+1.3*T;return {p:[1069+10*Math.cos(th),3.2,131+10*Math.sin(th)],t:[1069,3.5,131],fov:56};"
C="return {p:[998+9*T,26,178],t:[1012+9*T,0,150],fov:58};"
D="const th=2.2+1.2*T;return {p:[1142+14*Math.cos(th),4,232+14*Math.sin(th)],t:[1142,2.5,232],fov:56};"
E="return {p:[1160-6*T,9+8*T,250],t:[1000,2,150],fov:60};"
A2="return {p:[1150-20*T,1.6,133],t:[1110-20*T,2.6,128],fov:58};"
B2="const th=-0.6+1.2*T;return {p:[1069+11*Math.cos(th),3.0,131+11*Math.sin(th)],t:[1069,4.0,131],fov:56};"
