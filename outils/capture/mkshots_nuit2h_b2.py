# nuit2h_b2 : corrections du verdict du 26/11 22h00 (caméra à 80 cm, bitume sous 35 %, voiture entière devant le club, Hyper entière au-dessus du bouton jusqu'à la boucle)
exec(open('/home/claude/constancy/rushes/outils/capture/mkshots_nuit2h_b1.py').read())
def N1(x0,d0,d1,h,ty,fov=62,k=2.6):
  return CARX(x0,-115.5,20,3)+L(("cx+Math.max(%s,%s-%s*T)"%(d1,d0,k),"cy+%s"%h,"cz+0.35"),("cx-30","cy+%s"%ty,"cz-0.35"),fov)
S["A1"]=N1(-20,11,6.0,0.8,6.0)
S["A2"]=N1(-50,11,6.0,0.8,6.0)
S["A3"]=N1(-50,10,6.5,0.85,5.0,64)
def N2(dz,h,th,fov):
  return CARX(-60,-115.5,18)+L(("cx+0.6","cy+%s"%h,"%s"%(-115.5+dz)),("cx","cy+%s"%th,"-124"),fov)
S["B1"]=N2(8,1.3,2.4,72)
S["B2"]=N2(9.5,1.6,3.4,66)
def N3(back,h,ty,fov=64):
  return CARZ(-171.6,120,18)+L(("cx+0.4","cy+%s"%h,"cz-%s"%back),("cx","cy+%s"%ty,"cz+60"),fov)
S["C1"]=N3(10,2.2,12.8)
S["C2"]=N3(11,2.0,16)
S["A4"]=N1(5,11,6.0,0.8,6.0)
def N2b(x0,dz,h,th,fov):
  return CARX(x0,-115.5,18)+L(("cx+0.6","cy+%s"%h,"%s"%(-115.5+dz)),("cx","cy+%s"%th,"-124"),fov)
S["B3"]=N2b(-52,8,1.3,2.4,72)
S["C3"]=N3(10,2.2,17)
def N1v(x0,v,a,d0,d1,k,h,ty,fov=62):
  return CARX(x0,-115.5,v,a)+L(("cx+Math.max(%s,%s-%s*T)"%(d1,d0,k),"cy+%s"%h,"cz+0.35"),("cx-30","cy+%s"%ty,"cz-0.35"),fov)
S["A6"]=N1v(-1,16,2,9.5,5.0,2.4,0.8,6.0)
def N2c(x0,v,dz,h,th,fov):
  return CARX(x0,-115.5,v)+L(("cx+0.6","cy+%s"%h,"%s"%(-115.5+dz)),("cx","cy+%s"%th,"-124"),fov)
S["B4"]=N2c(-67.4,12,8,1.3,2.4,72)
S["A7"]=N1v(-1,16,2,10.5,7.0,1.9,0.8,6.0)
S["A8"]=N1v(-76.5,11,0,10.5,6.8,2.0,0.8,6.0)
S["A9"]=N1v(-76.5,11,0,10.5,6.8,2.0,0.8,6.0,58)
S["A10"]=N1v(-78,12,0,12.5,7.5,2.7,0.7,5.2,56)
S["A11"]=N1v(-77,11.5,0,11.5,6.8,2.5,0.7,6.4,58)
S["A12"]=CARX(-76.5,-115.5,11,0)+"const u=Math.min(1,T/1.9),e=u*u*(3-2*u);"+L(("cx+Math.max(6.8,10.5-2.0*T)","cy+0.8","cz+0.35+2.6*(1-e)"),("cx-30","cy+6.0","cz-0.35-1.5*(1-e)"),62)
S["A13"]=CARX(-76.5,-115.5,11,0)+"const u=Math.min(1,T/1.9),e=u*u*(3-2*u);const dd=Math.max(6.8,10.5-2.0*T),off=0.35+1.8*(1-e);"+L(("cx+dd","cy+0.8","cz+off"),("cx-30","cy+6.0","cz-off*30/dd"),62)
