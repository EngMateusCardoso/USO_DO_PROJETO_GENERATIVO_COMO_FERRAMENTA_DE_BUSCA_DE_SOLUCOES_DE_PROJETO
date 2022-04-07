# Carregar as bibliotecas DesignScript e padrão do Python
import sys
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
import math as mt

# ENTRADAS #
#Geométricos
bw = IN[0] # Dimensão Base do pilar (m)
h = IN[1] # Dimensão Altura do pilar (m)
c = IN[2]/100.0 # Cobrimento do concreto (m)
l = IN[3] # Comprimento da Viga (m)
# Armadura
dlong = IN[4]/1000.0 # Diâmetro da Armadura (m)
dest = IN[5]/1000.0 # Diâmetro do Estribo (m)
#Materiais
fck = IN[6] # fck em (MPa)
fyk = IN[7] # fyk em (MPa)
fctm = 0.3*fck**(2.0/3.0) #(MPa)
dagreg = IN[8]/1000.0 # Diâmetro máximo do Agregado (m)
#Cargas
g = IN[9] #(kNm)
q = IN[10] #(kNm)
#Lista do'calculo da seção'
d = IN[11][1][4] # (m)
nbar = len(IN[11][1][0]) # Numero de barras da positiva
# Saber qual seção coom barra externa mais próxima a LN
lista = [abs(-IN[11][0][4]*IN[11][0][3]+IN[11][0][1][-1]+h/2), abs(-IN[11][1][4]*IN[11][1][3]-IN[11][1][1][-1]+h/2), abs(-IN[11][2][4]*IN[11][2][3]+IN[11][2][1][-1]+h/2)]
minlist = min(lista)
for i in range(3):
	if minlist == lista[i]:
		break
ah = abs(IN[11][i][0][-1]-IN[11][i][0][-2]) #Esta na Lista i a barra

# ABERTURA CARACTERISTICA DE FISSURA

ssi = fyk/(1.4*1.15)*(g+0.4*q)/(g+q) #(MPa)
aa = c + dest + dlong*1.04/2 # (m)
b = ah/2 # (m)
if IN[11][i][1][-1] == h/2-aa or IN[11][i][1][-1] == -h/2+aa : # Se tiver só uma camada c é aa
	av = aa
	c = av
else:
	av = max(0.02,dlong*1.04,0.5*dagreg) # Espaçamento entre as barras vertical (m)
	c = av/2 # (m)
dd = 7.5*dlong # (m)
Acri = (aa+b)*(c+dd) # (m²)
As = 3.1415*dlong**2/4 # (m²)
rcri = As/Acri # S/U

wk1 = dlong/(12.5*2.25)*ssi/210000*(3*ssi/fctm) # (m)
wk2 = dlong/(12.5*2.25)*ssi/210000*(4/rcri+45) # (m)
wk = min(wk1,wk2) # (m)

# DEFORMAÇÃO EXCESSIVA IMEDIATA

P = g+0.3*q # Combinação quase permanente (kNm)
Ic = bw*h**3/12 #(m^4)
Ecs = min((0.8+0.2*fck/80),1)*5600*(fck)**(0.5) # (MPa)
alpe = 210000/Ecs # S/U
a1 = bw/2 # (m)
a2 = alpe*nbar*As # (m²)
a3 = -d*a2 # (m³)
xii = (-a2+(a2**2-4*a1*a3)**(0.5))/(2*a1) # (m)
Iii = bw*xii**3/12+alpe*nbar*As*(xii-d)**2 # (m^4)
Mr = 1.5*fctm*1000*Ic/(h/2) # (kNm)
Ma = (P*l**2)/8 # (kNm)
Im = (Mr/Ma)**3*Ic+(1-(Mr/Ma)**3)*Iii # (m^4)

a = 5*P*l**4/(384*Im*Ecs)/1000 # (m)

# DEFORMAÇÃO EXCESSIVA DEFERIDA NO TEMPO

at = a*(2.39505)

OUT = wk, a, at