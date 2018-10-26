import numpy as np
import matplotlib.pylab as plt

print("Por favor revisar este punto con Python 2")

#2.1
arDatos=np.genfromtxt("WDBC.dat", delimiter=",")

#BORRA BLOQUE
#print("arDatos", arDatos)
#print("np.shape(arDatos)", np.shape(arDatos))
#print("(arDatos[i,j]", arDatos[len(arDatos[:, 0])-1, 2])
#print("arDatos[:, 1]", arDatos[:, 1])

#2.2

#esta funcion calcula el elemento sigma_{P, S} de la matriz de covarianza
def CalCov(arrP, arrS):
	valMenPromP=arrP-( np.mean(arrP) )
	valMenPromS=arrS-( np.mean(arrS) )
	sumando=(valMenPromP*valMenPromS)/( float(len(t)-1) )
	cova=np.sum(sumando)
	return cova
