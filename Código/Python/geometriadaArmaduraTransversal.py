# Carregar as bibliotecas DesignScript e padrão do Python
import sys
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
from math import cos
from math import sin
from math import radians

# As entradas para este nó serão armazenadas como uma lista nas variáveis IN.

b = [IN[0]]
h = [IN[1]]
lp = [IN[2]]
c = [float(IN[3])]
dt = [IN[4]]
st = [IN[5][0]*100]
dg = [0]
pbase = IN[6]

# Insira o código abaixo desta linha
	
estribos=[]
for i in range(len(dt)):
	rmin=3*(dt[i]/1000) #raio da dobra
	gn=max(4*dt[i]/1000,0.05) #Comprimento do gancho
	cob0=c[i]/100+dt[i]/2000
	cob1=cob0+rmin
	x0=cob0
	x1=cob1
	x2=b[i]-cob1
	x3=b[i]-cob0
	y0=cob0
	y1=cob1
	y2=h[i]-cob1
	y3=h[i]-cob0
	plx=[(x1+rmin*cos(radians(135)))+gn*cos(radians(45)),x1+rmin*cos(radians(135)), x1, x1,x2, x2, x3,x3, x2, x2,x1, x1, x0,x0, x1, x1-rmin*cos(radians(135)),(x1-rmin*cos(radians(135)))+gn*cos(radians(45))]
	ply=[(y1+rmin*sin(radians(135)))+gn*cos(radians(45)),y1+rmin*sin(radians(135)), y1, y0,y0, y1, y1,y2, y2, y3,y3, y2, y2,y1, y1, y1-rmin*sin(radians(135)),(y1-rmin*sin(radians(135)))+gn*cos(radians(45))]
	
	estribo=[]
	for j in range(1,int(lp[i]/(st[i]/100))+1,1):
		p = []
		for k in range(len(plx)):
			ax=plx[k]-b[i]/2
			ay=ply[k]-h[i]/2
			u=(ax*cos(radians(dg[i]))-ay*sin(radians(dg[i])))
			v=(ax*sin(radians(dg[i]))+ay*cos(radians(dg[i])))
			p.append(Point.ByCoordinates(pbase[i].Z+j*st[i]/100,u+pbase[i].X,v+pbase[i].Y))
		curvas=[]
		for l in range(0,len(p)+1,3):
			curvas.append(Line.ByStartPointEndPoint(p[l],p[l+1]))
			if l+3<len(p):
				curvas.append(Arc.ByCenterPointStartPointEndPoint(p[l+2],p[l+1],p[l+3]))
		estribo.append(PolyCurve.ByJoinedCurves(curvas,0.001))
	estribos.append(estribo)
	
	
# Atribua a sua saída para a variável OUT.
OUT = estribos