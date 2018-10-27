import numpy as np
import matplotlib.pylab as plt

print("Por favor revisar este punto con Python 2")

#2.1
#quitamos la columna 0 porque tiene la identificacion de los pacientes que no nos interesa para este analisis
arDatos=(np.genfromtxt("WDBC.dat", delimiter=","))[:,1:] #arDatos=np.genfromtxt("WDBC.dat", delimiter=",")

#1.Necesitamos poner 0s y 1s en vez de M y B: y si: 1. sacamos solo la segunda columan de tipo string 2. la traducimos con una 
#funcion a solo 1.0 y 0.0 3. cambiamos a arDatos para que tenga solo numeros y hallar covarianza bien

#BORRA BLOQUE
print("arDatos", arDatos)
#print("np.shape(arDatos)", np.shape(arDatos))
#print("(arDatos[i,j]", arDatos[len(arDatos[:, 0])-1, 2])
#print("arDatos[:, 1]", arDatos[:, 1])
print("columna 2", arDatos[:, 1])

#la columna 2 tiene letras, pero es importante porque son los diagnosticos la cambiamos por M=0.0 y B=1.0
print("Como la columna con indice 1 tiene letras B o M, los cambiamos por numeros tales que B=1.0 y M=0.0")
def BMPorNum():
	arDatosNum=np.copy(arDatos)
	#print(arDatosNum)
	for i in range( 0, len(arDatosNum) ):
		#print("arDatosNum[i, 1]", arDatosNum[i, 1])		
		if  arDatosNum[i, 1]=="B":
			arDatosNum[i, 1]=1.0

		else:
			arDatosNum[i, 1]=0.0
	return arDatosNum
			
arDatNum=BMPorNum()
print("arDatNum", arDatNum)

#2.2

#esta funcion calcula el elemento sigma_{P, S} de la matriz de covarianza
def CalCov(arrP, arrS):
	valMenPromP=arrP-( np.mean(arrP) )
	valMenPromS=arrS-( np.mean(arrS) )
	sumando=(valMenPromP*valMenPromS)/( float(len(t)-1) )
	cova=np.sum(sumando)
	return cova
