import numpy as np
import matplotlib.pylab as plt

print("Por favor revisar este punto con Python 2")

#2.1

arrA=np.genfromtxt("WDBC.dat", delimiter=",")
#quitamos la columna 0 porque tiene la identificacion de los pacientes que no nos interesa para este analisis
arDatos=np.copy(arrA[:,1:]) #arDatos=np.genfromtxt("WDBC.dat", delimiter=",")[:,1:]#arDatos=(np.genfromtxt("WDBC.dat", delimiter=","))[:,1:] 
#arDatos=np.genfromtxt("WDBC.dat", delimiter=",")

#Con np.genfromtxt() de tipo str vamos leyendo y si es "B" cambiar en arDatos es posicion por 1.0, y si es "M" cambiarla por 0.0
arDiag=np.genfromtxt("WDBC.dat", dtype=str, delimiter=",")

#BORRA BLOQUE
#print("arDiag",arDiag )
#print("np.shape(arDiag)", np.shape(arDiag))
#print("arrDatos[0,0]", arDatos[0,0])
#arDatos[0,0]=0.0 #si se puede asignar un numero float en vez de un nan
#1.Necesitamos poner 0s y 1s en vez de M y B: y si: 1. sacamos solo la segunda columan de tipo string 2. la traducimos con una 
#funcion a solo 1.0 y 0.0 3. cambiamos a arDatos para que tenga solo numeros y hallar covarianza bien

#BORRA BLOQUE
#print("arDatos", arDatos)
#print("np.shape(arDatos)", np.shape(arDatos))
#print("(arDatos[i,j]", arDatos[len(arDatos[:, 0])-1, 2])
#print("arDatos[:, 1]", arDatos[:, 1])
#print("columna 2", arDatos[:, 0])
#print("arDatos antes de BMPorNum()", arDatos)
#print("np.shape(arDatos) antes de BMPorNum()", np.shape(arDatos))

#la columna 2 tiene letras, pero es importante porque son los diagnosticos la cambiamos por M=0.0 y B=1.0
print("Como la columna de diagnostico tiene letras B o M, los cambiamos por numeros tales que B=1.0 y M=0.0")
def BMPorNum():
	for i in range( 0, len(arDatos[:, 0]) ):
				
		if  arDiag[i, 1]=="B":
			arDatos[i, 0]=1.0

		elif arDiag[i, 1]=="M":
			arDatos[i, 0]=0.0

BMPorNum()

#transponemos arDatos para usar implementacion propia de la clase y comparar facilmente con np.cov
arDatosTra=np.copy( np.transpose( arDatos ) )

#BORRA BLOQUE O LINEA
#print("arDatosTra", arDatosTra)

#BORRA BLOQUE	
#def BMPorNum():
#	arDatosNum=np.copy(arDatos)
#	#print(arDatosNum)
#	for i in range( 0, len(arDatosNum) ):
#		#print("arDatosNum[i, 1]", arDatosNum[i, 1])		
#		if  arDatosNum[i, 1]=="B":
#			arDatosNum[i, 1]=1.0
#
#		else:
#			arDatosNum[i, 1]=0.0
#	return arDatosNum
#print("arDatos despues de BMPorNum()", arDatos)
#print("np.shape(arDatos) despues de BMPorNum()", np.shape(arDatos))
#print("arDatos[:, 0] despues de BMPorNum()", arDatos[:, 0])

#2.2
#usando mi entrega de la clase de este tema:

#da el elemento sigma:Indi,Indj de la matriz de covarianza, la primera variable tiene indice 0
def elemMatrizCov(Indi, Indj, datos):
	i=int(Indi)
	j=int(Indj)
	datoiMenosProm= (datos[i,:])-(np.mean(datos[i, :])) #xik-xiprom
	#print(np.shape(datoiMenosProm))
	datojMenosProm= (datos[j,:])-(np.mean(datos[j, :]))
	#print
	sumando= datoiMenosProm*datojMenosProm/( float(len(datos[i,:]))-1.0 ) #ES DIVIDO N O N-1.0
	#print("sumando", sumando)
	sigmaij=np.sum(sumando)
	return sigmaij

#BORRAR BLOQUE O LINEA
#print("elemMatrizCov(i, j, arDatosTra)", elemMatrizCov(1, 0, arDatosTra))

#funcion que da la matriz de covarianza de los datos del arreglo datos con filas=variables, columnas=datos de esas variables 
def matrizCov(datos):
	cov=np.zeros( ( len(datos[:, 0]), len(datos[:, 0]) ) )
	for i in range(0, len(datos[:, 0]) ):
		for j in range( 0, len(datos[:, 0]) ):
			cov[i, j]=elemMatrizCov(i, j, datos)
	return cov
covWDBC=matrizCov(arDatosTra)
print("La matriz de covarianza de los datos de WDBC.dat es")
print(covWDBC)

#BORRA BLOQUE
#CAMBIAR DATOS POR arDatos
#print( np.shape(np.cov(arDatosTra)), "es np.shape(np.cov(arDatosTra)). Y usando np.cov(arDatosTra) da")
#print(np.cov(arDatosTra))

#BORRA BLOQUE
#esta funcion calcula el elemento sigma_{P, S} de la matriz de covarianza
#def CalCov(arrP, arrS):
#	valMenPromP=arrP-( np.mean(arrP) )
#	valMenPromS=arrS-( np.mean(arrS) )
#	sumando=(valMenPromP*valMenPromS)/( float(len(t)-1) )
#	cova=np.sum(sumando)
#	return cova

#2.3
autoVals, autoVecs=np.linalg.eig(covWDBC)

#BORRA BLOQUE
#print("np.shape(autoVecs)", np.shape(autoVecs))
#print("autoVals", autoVals, "autoVecs", autoVecs)
#print("len(autoVals)", len(autoVals))
#print("autoVals", autoVals)

#funcion que imprime cada autovector y su correspondiente autovector
def impAutoValsVecs():
	print("Los autovalores y autovectores de la matriz de covarianza de los datos de WDBC.dat son:")
	for i in range(0, len(autoVals) ):
		print( "autovalor", i+1, "es", autoVals[i] )
		print("autovector", i+1, "es", autoVecs[:,i])

impAutoValsVecs()

#BORRA BLOQUE O LINEA	
#print("autoVals", autoVals)

#2.4
print("Punto 2.4: Los paramentros mas importantes son los de indices 4 y 24 (el primer parametro tendria indice 0), tambien como no se tuvo en cuenta la primera columna porque los numeros de identificacion ID no son relevantes para un estudio asi, estos parametros mas impoertantes son los de las columnas 6 y 26 en WDBC.dat con la primera columna con numero 1, son los parametros mas importantes porque son los que al variar mas hacen que se muevan los datos entre datos de pacientes con diagnostico Benigno y pacientes con diagnostico Maligno, por esto debe haber alguna relacion entre el diagnostico y estos parametros de indices 4 y 24 (el primer parametro tendria indice 0) . Se llega a este resultado de la siguiente forma: primero, notamos que el autovalor_1= 4.43782731e+05 y el autovalor_2=7.31010042e+03 son los mas grandes de todos, y podemos aproximadamente despreciar los otros en comparacion, porque estos otros autovalores tienen por mucho orden de magnitud 2, que ya es despreciable en comparacion al valor de los primeros dos autovalores. Segundo, vemos que en el autovector_1 las componentes de mayor magnitud son las de indices 24 y 4 con orden de magnitud -1, y despues las componentes de indices 3, 14 y 23 con orden de magnitud -2 (la primera componente tendria indice 0). Ademas, vemos que en el autovector_2 las componentes de mayor magnitud son las de indices 4 y 24 con orden de magnitud -1, y despues las componentes de indices 3 y 22 con orden de magnitud -2 (la primera componente tendria indice 0). Con esto concluimos que como la direccion en que mas varian nuestros datos de los pacientes son las de el autovector_1 y autovector_2, y los parametros que al variar mas hacen que el dato de un paciente se mueva en la direccion del autovector_1 y/o el autovector_2 son los paramentros de indices 4 y 24 (el primer parametro tendria indice 0). Justamente, estos parametros de indices 4 y 24 son los mas importantes, pues son los que al variar mas hacen que se muevan los datos entre datos de pacientes con diagnostico Benigno y pacientes con diagnostico Maligno, por esto debe haber alguna relacion entre el diagnostico y estos parametros de indices 4 y 24 (el primer parametro tendria indice 0). Cabe se(n)alar que debe hacer una relacion entre el diagnostico y los parametros de indices 3, 14, 22 y 23, pero es una relacion bastante menos fuerte que la descrita anteriormente.")

#2.5
#para la proyeccion sobre PC1=autovalor_1 Y PC2=autovalor_2
#arDatos y autoVecs
#print("np.shape(arDatos)", np.shape(arDatos), "y arDatos es")
#print(arDatos)
#print("np.shape(autoVecs)", np.shape(autoVecs), "y autoVecs es")
#print(autoVecs)

arDatosPCs=np.dot( arDatos, autoVecs ) #arreglo cuyas filas son los datos respecto a los 31 autovectores como 31 ejes

#print("np.shape(arDatosPCs)", np.shape(arDatosPCs), "arDatosPCs")
#print(arDatosPCs)

def grafDatosProyectados():
	plt.figure()
	varColor="blue"
	for i in range( 0, len(arDatosPCs[:, 0]) ):
		#arDatosPCs[:, 0] es arreglo de proyecciones de cada dato de un paciente sobre PC1=autovector_1,
		#arDatosPCs[:, 1] es arreglo de proyecciones de cada dato de un paciente sobre PC2=autovector_2, los autovectores son de magnitud=1 
		if arDatos[i, 0]==0.0: #verdadero si es M
			varColor="blue"
			#plt.scatter([ arDatosPCs[i, 0] ], [ arDatosPCs[i, 1] ], c=varColor, label=r"$Maligno$")
		elif arDatos[i, 0]==1.0: #verdadero si es benigno
			varColor="green"
			#plt.scatter([ arDatosPCs[i, 0] ], [ arDatosPCs[i, 1] ], c=varColor, label=r"$Benigno$")
		#plt.scatter(arDatosPCs[:, 0], arDatosPCs[:, 1])
		plt.scatter([ arDatosPCs[i, 0] ], [ arDatosPCs[i, 1] ], c=varColor)
	plt.xlabel("$PC1=e_{1}$")
	plt.ylabel("$PC2=e_{2}$")
	#plt.legend(loc=0)
	plt.title("$Maligno=azul$ $y$ $Benigno=verde$")		
	plt.savefig("HernandezDaniel_PCA.pdf")

grafDatosProyectados()

#2.6
print("///////////////////////////////PUNTO2.6/////////////////////")
print("Basado en el resultado de la grafica HernandezDaniel_PCA.pdf considero que el metodo de PCA si es util para ayudar a realizar el diagnostico, porque se puede apreciar que hay un intervalo en los valores de la componente de PC1=autovector_1, aproximadamente [-800, -200], para los que los diagnosticos son en su gran mayoria Benigno, aunque hay algunos pocos diagnosticos Maligno. Similarmente, se puede apreciar que hay un intervalo en los valores de la componente de PC2=autovector_2, aproximadamente [-200, -40], fuera del cual nuestros datos tienen siempre diagnostico Maligno. Y dentro de ese intervalo el diagnostico es principalmente Benigno si ademas los datos estan en el intervalo de PC1 mencionado al inicio, pero dentro de este intervalo para PC2 los dignosticos son casi en su totalidad Maligno si ademas los datos estan fuera del intervalo de PC1 mencionado al inicio. Entonces, hay ciertas regiones en la grafica de los datos en el plano de PC2 Vs PC1 en los que el diagnostico de nuestros datos es siempre uno, lo cual hace que sea muy util el metodo de PCA para realizar el diagnostico, pero hay otras regiones en el plano de PC2 Vs PC1 en los que si bien la gran mayoria de los datos tiene un diagnostico claro, existen algunas datos para los que el diagnostico es diferente, por eso en estas regiones no se puede afirmar a ciencia cierta cual es el diagnostico a partir de este metodo, al menos usando dos componentes principales solamente. En conclusion, a partir de nuestros datos de WDBC.dat hay regiones donde el diagnostico resulta claro y definido, en ellas pienso que el metodo de PCA podria tener sus mayores aplicaciones, aunque siendo el diagnostico de cancer de una persona algo sumamente delicado me gustaria analizar los datos con mas componentes principales y hacer mas experimentos y pruebas para asegurarce de que si funciona perfectamente. Adicionalmente, hay otras regiones donde el diagnostico no es claro por completo, por esto considero que en ellas el metodo podria ayudar y orientar el diagnostico, pero no dar un diagnostico definitivo. Por esto considero que el metodo de PCA si es util para ayudar a realizar el diagnostico")


	

