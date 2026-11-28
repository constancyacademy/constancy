exec(open('/root/w/v2/shots_final.py').read())
S["P2"]=ORB(26,22,250,40,"(62+14*T)",100,46)
S["P4"]=CAMP+"const b=7.5-2.0*T,l=3.0-3.6*T,h=1.9+0.5*T;return {p:[me.x-fx*b+rx*l,my+h,me.z-fz*b+rz*l],t:[me.x+fx*30,my+11,me.z+fz*30],fov:60};"; PL["P4"]=NORING+ME(30,166)
S["P5"]=("const u=Math.min(T,1.6),d=4.5*u;const sx=31-0.18*d,sz=163-0.98*d;"+L(V("sx","1.7+0.3*T","sz"),V("-30+40*T","95+6*T",0),50)); PL["P5"]=NORING+ME(30,167)
# bomb debug : close camera, look at impact
S["B9"]=BOMB(20,200,0.45,10,3,2,62)
PL["B9"]="window.__BK=null;"
def BOMB2(a,R,tim,back,lat,ch,ty,fov):
  return BOMB(a,R,tim,back,lat,ch,fov).replace("],t:[%f,%f,%f]"%(0,0,0),"")  # placeholder
c,s=math.cos(math.radians(20)),math.sin(math.radians(20))
_b=BOMB(20,200,0.95,18,5,2.5,60)
ix,iz=VX+c*200,VZ+s*200
S["P3"]=_b.replace(",10,%f],fov"%iz,",5,%f],fov"%iz)
PL["P3"]="window.__BK=null;"
S["P3b"]=_b.replace("10.000000,%f],fov"%iz,"4.000000,%f],fov"%iz)
PL["P3b"]="window.__BK=null;"
S["P2c"]=ORB(20,40,255,75,"(58+26*T)",100,46)
S["P4c"]=CAMP+"const b=7.5-2.0*T,l=1.3-1.3*T,h=1.9+0.5*T;return {p:[me.x-fx*b+rx*l,my+h,me.z-fz*b+rz*l],t:[me.x+fx*30-rx*1.0,my+11,me.z+fz*30-rz*1.0],fov:60};"; PL["P4c"]=NORING+ME(30,166)
S["P4d"]=CAMP+"const b=8.5-2.0*T,l=1.3-1.3*T,h=4.2+0.4*T;return {p:[me.x-fx*b+rx*l,my+h,me.z-fz*b+rz*l],t:[me.x+fx*30-rx*1.0,my+6.5,me.z+fz*30-rz*1.0],fov:62};"; PL["P4d"]=NORING+ME(30,166)
