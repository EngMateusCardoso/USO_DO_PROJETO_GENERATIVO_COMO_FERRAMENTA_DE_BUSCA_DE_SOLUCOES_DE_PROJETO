# Carregar as bibliotecas DesignScript e padrão do Python
import sys
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
import math as mt

cargas = IN[1] # [M1,Mpos,M2] em (kNm)
Vmax = IN[2] # Cortante máxima (kN)
bw = IN[3] # (m)
fck = IN[4] # (MPa)
fyk = IN[5] # (Mpa)
dlong = IN[6]/1000 # (m)
L = IN[7] # (m)
d = min(IN[0][0][4], IN[0][1][4], IN[0][2][4]) # usa a altura útil minima para o calculo de Vc (m)


fctd = 0.15*(fck)**(2.0/3.0) # (kN)
fbd = 2.25*fctd # (MPa)
Vc = 0.6*fctd*bw*d*1000 # (kN)
al = d*(Vmax*1.4/(2*(Vmax*1.4-Vc)))
if al<0.5*d:
	al = 0.5*d
if al>d:
	al = d
# COMPRIMENTOS DE ANCORAGEM
lb = dlong/4*fyk/1.15/fbd # comprimento de ancoragem reto básico (m)
lbgancho = 0.7*lb #comprimento de ancoragem com gancho (m)
ad = al + lb # comprimento a acrescentar a barras sem gancho
e = dlong*3.5
# Comprimento das barras 

P = IN[8]
Va = IN[9]
M1 = cargas[0]
M2 = cargas[2]
a = -P/2
b = Va
c = -M1
x1 = (-b+(b**2-4*a*c)**(0.5))/(2*a)
x2 = (-b-(b**2-4*a*c)**(0.5))/(2*a)

#comprimentos da armadura negativa (superior)
psi1 = 0 + e # ponto superior de inicio do trecho 1 
psf1 = x1 + ad # ponto superior de fim do trecho 1
if M1 == 0: # Nesse caso não fazemos essa seção
	psf1 = 0 + e+0.025 # não pode zerar o comprimento do cilindro
psi3 = x2 - ad
if M2==0:
	psi3 = L - e -0.025 # não pode zerar o comprimento do cilindro
psf3 = L - e
if psf1>=psi3: # as barras de um lado chegam no outro lado
	if psf1>=L-e: # condição que a ancoragem sai da viga
		psf1=L-e
		psi3=psf1+0.025
		psf3=psi3+0.025
	elif psi3<=0+e:
		psi3=0+e
		psf1=psi3-0.025
		psi1=psf1-0.025
	elif len(IN[0][0][0])>=len(IN[0][2][0]): # se tiver mais barras no lado 1 
		psi3 = psf1+0.025 # Barras do lado 1 prevalecem 
	elif len(IN[0][0][0])<len(IN[0][2][0]):
		psf1 = psi3-0.025
psi2 = psf1
psf2 = psi3

#comprimentos da armadura positiva (inferior)
pii1 = 0 + e # ponto inferior de inicio do trecho1
pii2 = x1 - ad
if pii2<0+e:
	pii2 = 0 + e
pif1 = pii2
pif2 = x2 + ad
if pif2>L-e:
	pif2 = L - e
pii3 = pif2
pif3 = L - e
if pii1==pif1:
	pii1=pii1-0.025
if pii3==pif3:
	pif3=pif3+0.025

pi = []
pf = []
# Pontos inicial e final
#superior
for i in range(len(IN[0][0][0])): # de M1
	pi.append(psi1)
	pf.append(psf1)
for i in range(2): # da armadura de sustentação
	pi.append(psi2)
	pf.append(psf2)
for i in range(len(IN[0][2][0])): # de M2
	pi.append(psi3)
	pf.append(psf3)
#inferior
for i in range(2): # da armadura de sustentação
	pi.append(pii1)
	pf.append(pif1)
for i in range(len(IN[0][1][0])): # de Mpos
	pi.append(pii2)
	pf.append(pif2)
for i in range(2): # da armadura de sustentação
	pi.append(pii3)
	pf.append(pif3)

OUT = pi, pf