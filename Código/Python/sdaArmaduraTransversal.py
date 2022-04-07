# Carregar as bibliotecas DesignScript e padrão do Python
import sys
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
import math as mt

Vmax = IN[0] # (kN)
d = min(IN[1][0][4],IN[1][1][4],IN[1][2][4]) # (m)
bw = IN[2] # (m)
fck = IN[3] # (MPa)
fyk = IN[4] # (MPa)
dest = IN[5]/1000.0 # (m)

check = 0

Tsd = (1.4*Vmax)/bw/d/1000.0 # (MPa)
Trd2i = 0.27*(1-fck/250)*fck/1.4 # (MPa)
TxT = Tsd/Trd2i

Tsw = Tsd-0.09*(fck)**(2.0/3.0) # (MPa)
fywd = fyk/1.15 # (MPa)
rsw = (1.11*Tsw)/(fywd) # S/N
rswmin = 0.06*(fck)**(2.0/3.0)/fyk # S/N
#Espaçamento dos estribos
s = 2*(3.1415*dest**2/4)/rsw/bw  # (m)
#Armadura minima (espaçamento maximo)
smax = 2*(3.1415*dest**2/4)/rswmin/bw  # (m)
if s > smax:
	s = smax
#espaçamento maximo em função do esforço cortante
Vsd = Vmax*1.4
Vrd2 = Trd2i*bw*d
if Vsd <= 0.67*Vrd2:
	smax = 0.6*d
	if smax>0.3:
		smax = 0.3
if Vsd > 0.67*Vrd2:
	smax = 0.3*d
	if smax>0.2:
		smax = 0.2
if s > smax:
	s = smax

checkneg1 = IN[1][0][2]
checkpos = IN[1][1][2]
checkneg2 = IN[1][2][2]

if checkneg1 == -1 or checkpos ==-1 or checkneg2==-1:
	check = -1

OUT = s, check, TxT