#!/usr/bin/python
# -*- coding: UTF-8 -*-
#MAURÍCIO BALBONI
import sys
def MDireto(nset,bsize,D):
	hit=0
	miss=[0]*3
	tamOffset = log2((bsize*8)/32) +2
	tamIndice = log2(nset/1)
	CacheD=[-1]*(nset/1)
	for i in range(len(D)):
		D[i]=(D[i] >> (tamOffset + tamIndice),(D[i] >> tamOffset & ((2^tamIndice)-1))) #Tag #Indice
	for i in range(len(D)):
		if CacheD[D[i][1]] == D[i][0]:
			hit=hit+1
		else:
			if CacheD[D[i][1]] < 0:
				miss[0]=miss[0]+1 										#Cache vazia
			elif CacheD[D[i][1]] >-1 and CacheD[D[i][1]] != D[i][0]:
				miss[1]=miss[1]+1
			CacheD[D[i][1]]=D[i][0]	
	Printa(hit,miss,len(D))

def Associativa2(nset,bsize,D):
	hit=0
	miss=[0]*3
	tamOffset=log2(bsize);
	tamIndice = log2(nset/2)
	CacheD=[-1]*(nset)
	for i in range(len(D)):
		D[i]=(D[i] >> (tamOffset + tamIndice),(D[i] >> tamOffset & ((2^tamIndice)-1))) #Tag #Indice
	for i in range(len(D)):
		if CacheD[D[i][1]] == D[i][0] or CacheD[D[i][1]*2] == D[i][0]:
			hit=hit+1
		else:
			if CacheD[D[i][1]] < 0 and CacheD[D[i][1]*2] < 0:
				miss[0]=miss[0]+1
				CacheD[D[i][1]]=D[i][0] 										#Cache vazia
			elif ((CacheD[D[i][1]] >-1 and CacheD[D[i][1]] != D[i][0]) or (CacheD[D[i][1]*2] >-1 and CacheD[D[i][1]*2] != D[i][0])):
				if CacheD[D[i][1]] == -1:
					miss[1]=miss[1]+1
					CacheD[D[i][1]]=D[i][0]
				elif CacheD[(D[i][1])*2] == -1:
					miss[1]=miss[1]+1
					CacheD[D[i][1]*2]=D[i][0]
				else:
					miss[1]=miss[1]+1
					CacheD[D[i][1]]=D[i][0]
	Printa(hit,miss,len(D))

def Associativa4(nset,bsize,D):
	hit=0
	miss=[0]*3
	tamOffset=log2(bsize)
	tamIndice = log2(nset/4)
	CacheD=[-1]*(nset)
	for i in range(len(D)):
		D[i]=(D[i] >> (tamOffset + tamIndice),(D[i] >> tamOffset & ((2^tamIndice)-1))) #Tag #Indice
	for i in range(len(D)):
		if ((CacheD[D[i][1]] == D[i][0]) or (CacheD[D[i][1]*2] == D[i][0]) or (CacheD[D[i][1]*3] == D[i][0]) or (CacheD[D[i][1]*4] == D[i][0])):
			hit=hit+1
		else:
			if ((CacheD[D[i][1]] < 0) and (CacheD[D[i][1]*2] < 0) and (CacheD[D[i][1]*3] < 0) and (CacheD[D[i][1]*4] < 0)):
				miss[0]=miss[0]+1
				CacheD[D[i][1]]=D[i][0] 										#Cache vazia
			elif ((CacheD[D[i][1]] >-1 and CacheD[D[i][1]] != D[i][0]) or (CacheD[D[i][1]*2] >-1 and CacheD[D[i][1]*2] != D[i][0]) or (CacheD[D[i][1]*3] >-1 and CacheD[D[i][1]*3] != D[3*i][0]) or (CacheD[D[i][1]*4] >-1 and CacheD[D[i][1]*4] != D[i][0])):
				if CacheD[D[i][1]] == -1:
					miss[1]=miss[1]+1
					CacheD[D[i][1]]=D[i][0]
				elif CacheD[D[i][1]*2] == -1:
					miss[1]=miss[1]+1
					CacheD[D[i][1]*2]=D[i][0]
				elif CacheD[D[i][1]*3] == -1:
					miss[1]=miss[1]+1
					CacheD[D[i][1]*3]=D[i][0]
				elif CacheD[D[i][1]*4] == -1:
					miss[1]=miss[1]+1
					CacheD[D[i][1]*4]=D[i][0]
				else:
					miss[1]=miss[1]+1
					CacheD[D[i][1]]=D[i][0]	
	Printa(hit,miss,len(D))

def TotalA(nset,bsize,D):
	hit=0
	miss=[0]*3
	capac=0
	tamOffset=log2(bsize);
	CacheD=[-1]*(nset)*4
	for i in range(len(D)):
		D[i]=(D[i] >> (tamOffset + 1)) #Tag #Indice
	for j in range(len(D)):
		cont=0
		for i in range(capac):
			if CacheD[i]==D[j]:
				hit=hit+1
				cont=-1
				break
			else:
				cont=cont+1
		if cont>-1:
			if(capac<len(CacheD)):
				CacheD[capac]=D[j]
				miss[0]=miss[0]+1
				capac=capac+1
			else:
				CacheD[capac]=D[j]
				miss[2]=miss[2]+1
				capac=capac+1
	Printa(hit,miss,len(D))
	
def Printa(hit,miss,tD):
	print "Total de Acessos: ", tD
	print "Hit: ",hit
	print "Total Miss: ", miss[0]+miss[1]+miss[2]
	print "Miss Compulsorio: ",miss[0]
	print "Miss Conflito: ",miss[1]
	print "Miss Capacidade: ",miss[2]
	print ""
	print "Porcentagens: "
	print "Porcetagem de hit: ", int(float(hit)/tD*100.0),"%"
	print "Porcentagem de miss: ", int((miss[0]+miss[1]+miss[2])/float(tD)*100.0),"%"
	print "Procentagem de Miss Compulsorio: ",(float(miss[0])/(float(miss[0]+miss[1]+miss[2]))*100),"%"
	print "Porcentagem de Miss Conflito: ",(float(miss[1])/(float(miss[0]+miss[1]+miss[2]))*100),"%"
	print "Porcentagem de Miss Capacidade: ",(float(miss[2])/(float(miss[0]+miss[1]+miss[2]))*100),"%"
	print ""
	
def log2(n):
	if n>1:
		return log2(n/2)+1
	else:
		return 0

#-----------------------------------------MAIN ---------------------------------------------
lcomando=sys.argv
print lcomando															#coloca todos os valores no arquivo
a=open(lcomando[len(lcomando)-1],"r")
r=a.readlines()
contD=0
contI=0
for i in range(len(r)): 												#tira o \n
	r[i]=r[i].rstrip()
	r[i]=int(r[i])
for i in range(len(r)/2):
	if r[i*2] != 0:
		contD=contD+1
	if r[i*2+1] != 0:
		contI=contI+1
Da=[0]*contD 														#cria um vetor com o tamanho do arquivo
I=[0]*contI
for i in range(contD): 												#preencher 
	if r[i*2] != 0:
		Da[i]=r[i*2]
for i in range(contI):
	if r[(i*2)+1] != 0:
		I[i]=r[(i*2)+1]
if len(lcomando)<8:	
	MDireto(1024,4,Da)
	MDireto(1024,4,I)
else:
	lcomando[1]=int(lcomando[1])
	lcomando[2]=int(lcomando[2])
	lcomando[3]=int(lcomando[3])
	lcomando[4]=int(lcomando[4])
	lcomando[5]=int(lcomando[5])
	lcomando[6]=int(lcomando[6])
	if int(lcomando[3])==1:
		MDireto(lcomando[1],lcomando[2],Da)
	elif lcomando[3]==2:
		Associativa2(lcomando[1],lcomando[2],Da)
	elif lcomando[3]==4:
		Associativa4(lcomando[1],lcomando[2],Da)
	else:
		TotalA(lcomando[1],lcomando[2],Da)
	if lcomando[6]==1:
		MDireto(lcomando[4],lcomando[5],I)
	elif lcomando[6]==2:
		Associativa2(lcomando[4],lcomando[5],I)
	elif lcomando[6]==4:
		Associativa4(lcomando[4],lcomando[5],I)
	else:
		TotalA(lcomando[4],lcomando[5],I)
