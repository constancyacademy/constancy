from h import *
import math
def dawn(h0,rate=0.0):
  # heure h0 au debut du plan, avance de rate heures/s (0 = fige)
  return "const W6=window.__W();W6.G.dawn=Math.max(0,8-(%f+%f*T));if(W6.P)W6.P.dayT=0.5;"%(h0,rate)
def m3(name,body,h0,n=1,o=0,js="",wait=2500,rate=0.0):
  s=shot(name,body,dayT=0.5,n=n,toff=o,wait=wait,js="{const W6=window.__W();W6.G.dawn=Math.max(0,8-%f);W6.P.dayT=0.5;}"%h0+js,pre=dawn(h0,rate)); s["far"]=6000; return s
