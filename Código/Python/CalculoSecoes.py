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
L = IN[3] # Comprimento da Viga (m)
# Armadura
dlong = IN[4]/1000.0 # Diâmetro da Armadura (m)
dest = IN[5]/1000.0 # Diâmetro do Estribo (m)
 #Materiais
fck = IN[6] # fck em (MPa)
fyk = IN[7] # fyk em (MPa)
fcd = fck/1.4*1000000.0 # fcd em (Pa)
fyd = fyk/1.158*1000000.0 # Tensão de escoamento do aço (Pa)
dagreg = IN[8]/1000.0 # Diâmetro máximo do Agregado (m)
# Solicitações
Cargas = IN[9] # lista com as cargas
M1 = Cargas[0] # Momento no ponto 1 (kNm)
Mpos = Cargas[1] # Momento max no meio (kNm)
M2 = Cargas[2] # Momento no ponto 2 (kNm)
Mdneg1 = M1*1.4*1000 # Momento de Calculo Negativo 1 (Nm)
Mdpos = Mpos*1.4*1000 # Momento de Calculo positivo max (Nm)
Mdneg2 = M2*1.4*1000 # Momento de Calculo Negativo 2 (Nm)

# MEDIDAS IMPORTANTES
# d e d'
dl = c+dest+1.04*dlong/2 # Mossa da armadura 0,04 (m)
d = h-dl # (m)

# Espaçamentos
diamcomfusco = 1.04*dlong # 0.04 saliência da mossa do ferro (m)
ah = max(0.02,diamcomfusco,1.2*dagreg) # Espaçamento entre as barras horizontal (m)
av = max(0.02,diamcomfusco,0.5*dagreg) # Espaçamento entre as barras vertical (m)
sh = ah+diamcomfusco # Espaçamento entre eixos de barras horizontal minimo (m)
sv = av+diamcomfusco # Espaçamento entre eixos de barras vertical minimo (m)
slivrex = bw-2*dl # Espaço livre para colocação das barras em x (m)
slivrey = h-2*dl # Espaço livre para colocação das barras em y (m)


#FUNÇÕES DE DIMENSIONAMENTO

def calculoAs(bw, d, c, fcd, fyd, Md) : # calculo de As 
	if fcd <= 50*1000000/1.4: # fck<50
		gama = 0.8 # Gama e alphac diferentes com o fck
		alphac = 0.85
	else : # fck>50 gama e alphac obedecem a formula
		gama = 0.8-(fcd*1.4/1000000-50)/400 
		alphac = 0.85*(1-(fcd*1.4/1000000-50)/200)
	KMD = Md/(bw*d*d*fcd)
	KX = (1-(1-2*KMD/alphac)**0.5)/gama # KX = x/d
	KZ = 1-gama*KX/2
	As = Md/(KZ*d*fyd) # As 
	return As, KX

# DETALHAMENTO DA SEÇÃO

def detalhamento(bw, h, dlong, dl, As, slivrex, slivrey, sh, sv): # Posiciona as barras na parte inferior da viga
	x1 = -bw/2+dl # Coordenadas com origem no canto inferior esquerdo da seção da viga
	x2 = bw/2-dl
	y = -h/2+dl
	nbar = round(As/((mt.pi*dlong**2.0)/4)) # Numero de barras para resistir ao esforço
	if nbar<(As/((mt.pi*dlong**2.0)/4)): # Se arredondou para baixo soma +1
		nbar=nbar+1 # Numero de barras para resistir ao esforço numero inteiro
	if nbar>2: # Se vai ter mais de duas barras vamos entrar na função distribuição
		pn=[]
		pn, ncamadas, nbx =distribuicao(pn, x1, x2, y, nbar, slivrex, slivrey, sh, sv)
	else:
		nbar=2
		pn=[[x1,y],[x2,y]] # No caso de ter só 2 barras
		ncamadas=1
		nbx=2 # Numero de barras na primeira camada
	px=[]
	py=[]
	for i in range(len(pn)):
		px.append(pn[i][0]) # Lista com as coordenadas x das barras (seguindo o sistema comentado anteriormente)
		py.append(pn[i][1]) # Lista com as coordenadas y das barras
	Asreal=nbar*((mt.pi*(dlong)**2.0)/4)
	return px, py, ncamadas, Asreal, nbar, nbx 
# Esse esta dentor do detalhamento
def distribuicao(pn, x1, x2, y, nbar, slivrex, slivrey, sh, sv): # Distribuição com mais de 2 barras
	nbx = round(slivrex/sh) # Número de barras que cabe em slivrex (ou seja na primeira camada) Obs.: é o que cabe não o que vai ter
	if nbx<(slivrex/sh):
		nbx = nbx+1 # Arredonda para cima pq nbx é numero de barras não de espaços, entendeu ?
	ncamadas = (nbar-nbx)/2+1 # Numero de camadas
	if ncamadas<=1:
		ncamadas = 1
	ncamadas = round(ncamadas+0.1) # Arredondar para cima sempre uma vez que ncamadas é multiplo de 0.5
	nbarf = nbar # Numero de barras que falta posicionar
	ncamadasf = ncamadas # Numero de camadas que falta posicionar
	if nbar<nbx:
		nbx = nbar # nbx precisa ser a partir daqui o numero de barras na 1ª camada
	sxreal = slivrex/(nbx-1) # Espaçamento em x real entre as barras 
	for i in range(int(nbx)): # Esse 'for' posiciona as barras na primeira camada
		pn.append([x1+sxreal*(i),y])
	ncamadasf = ncamadas-1
	nbarf=nbarf-nbx
	while nbarf>0:
		if nbarf==1:
			pn.append([x1,y+(ncamadas-ncamadasf)*sv]) # Posiciona barra única no canto esquerdo
			break # Se só tinha uma barra pode acabar o laço
		else:
			pn.append([x1,y+(ncamadas-ncamadasf)*sv]) # Posiciona barra a esquerda na camada
			pn.append([x2,y+(ncamadas-ncamadasf)*sv]) # Posiciona barra a direita na camada
			nbarf=nbarf-2
		ncamadasf=ncamadasf-1
		nbarf=nbarf-2
		if ncamadasf==0:
			break
	return pn, ncamadas, nbx

# VERIFICAÇÕES

def calcdreal(h, dl, nbx, nbar, sv):
	ncamadas = (nbar-nbx)/2+1 # Numero de camadas dessa vez não arredondei
	sy = 0
	for i in range(int(round(ncamadas+0.1))):
		sy = sy + 2*i*sv # 2 barras i*sv é a distancia
		t=i
	if (ncamadas%1)==0: # Caso
		sy = sy
	else :
		sy = sy-t*sv
	ycg = sy/nbar
	dreal = h-dl-ycg
	return dreal, ycg
# Calculo de As minimo
def calcAsmin(fck, bw, h):
	tabelaro = [0.15, 0.15, 0.15, 0.164, 0.179, 0.194, 0.208, 0.211, 0.219, 0.226, 0.233, 0.239, 0.245, 0.251, 0.256] 
	i = (fck-20)/5 # Tabela acima começa do fck 20 e segue de 5 em 5
	romin = tabelaro[int(i)]
	Asmin = romin/100*bw*h # As minimo em (m²)
	return Asmin
# Verificar As maximo
def CalcAsmax(bw, h, Asreal, Asmin):
	Asmax = 0.04*bw*h -Asmin # As maximo em (m²)
	return Asmin
# Verificações geometricas
def verifgeo(ncamadas, slivrey, sv, slivrex, sh):
	check = 0
	if ncamadas*sv > 0.5*slivrey: # Verificar se não tem camadas demais para o numero de camadas cabe na seção
		check = -1 # Camadas demais
	if slivrex<sh:	# Verificar se cabe mais de uma barra na camada horizontal
		check = -1
	return check
# Verificação da Consideração de Armadura Concentrada
def ArmConcen(ycg, h):
	check = 0
	if ycg>0.1*h:
		check = -1
	return check

def calculo(d, bw, c, fcd, fyd, Md, fck, h, dlong, dl, slivrex, slivrey, sh, sv): #Dimensionamento definitivo
	dadot = d
	cont = 0
	check = 0
	Asmin = calcAsmin(fck, bw, h)
	Asmax = 0.04*bw*h-((mt.pi*dlong**2.0)/4)*2
	while True: # Considera o d inicial depois atuailza conforme o CG da armadura muda
		As, KX = calculoAs(bw, dadot, c, fcd, fyd, Md)
		if As<Asmin and As>0:
			As = Asmin
		px, py, ncamadas, Asreal, nbar, nbx = detalhamento(bw, h, dlong, dl, As, slivrex, slivrey, sh, sv) # Detalhamento 
		dreal, ycg = calcdreal(h, dl, nbx, nbar, sv) # calcula o centro de massa da armadura para calcular o dreal
		if dreal<dadot:
			dadot = dreal
		if dreal>=dadot: # Se for isso da ok
			Checkdreal = 0
			break
		if cont ==1000:  # para segraça caso não tenha convergencia
			Checkdreal = -1
			break
		cont = cont+1
	TxAs = (Asreal-Asmin)/(Asmax - Asmin)
	dmin =2*(Md/bw/fcd)**0.5
	Txd = dmin/dreal
	TxAC = ycg/0.1*h
	CheckGeo = verifgeo(ncamadas, slivrey, sv, slivrex, sh)
	CheckConcen = ArmConcen(ycg, h)
	if CheckGeo==-1 or CheckConcen==-1 or Checkdreal==-1:
		check = -1
	return px, py, check, KX, dreal, TxAs, Txd, TxAC

pxneg1, pyneg1, checkneg1, KXneg1, drealneg1, TxAsneg1, Txdneg1, TxACneg1 = calculo(d, bw, c, fcd, fyd, Mdneg1, fck, h, dlong, dl, slivrex, slivrey, sh, sv)
pxpos, pypos, checkpos, KXpos, drealpos, TxAspos, Txdpos, TxACpos = calculo(d, bw, c, fcd, fyd, Mdpos, fck, h, dlong, dl, slivrex, slivrey, sh, sv)
pxneg2, pyneg2, checkneg2, KXneg2, drealneg2, TxAsneg2, Txdneg2, TxACneg2 = calculo(d, bw, c, fcd, fyd, Mdneg2, fck, h, dlong, dl, slivrex, slivrey, sh, sv)

def invert(py): #Coreção do eixo z nas armaduras negativas 
	for i in range(len(py)):
		py[i]=-py[i]
	return py

pyneg1 = invert(pyneg1)
pyneg2 = invert(pyneg2)

OUT = [pxneg1, pyneg1, checkneg1, KXneg1, drealneg1, TxAsneg1, Txdneg1, TxACneg1], [pxpos, pypos, checkpos, KXpos, drealpos, TxAspos, Txdpos, TxACpos], [pxneg2, pyneg2, checkneg2, KXneg2, drealneg2, TxAsneg2, Txdneg2, TxACneg2]