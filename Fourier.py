import numpy as np
import matplotlib.pylab as plt

print("Por favor revisar este punto con python 2")

#3.1

#BORRA BLOQUE
#links de investigacion>
#https://www.google.com/search?client=ubuntu&channel=fs&q=read+a+.dat+python&ie=utf-8&oe=utf-8
#https://stackoverflow.com/questions/11798800/reading-a-binary-dat-file-as-an-array
#https://stackoverflow.com/questions/49329010/how-to-decode-a-dat-file-in-python
#https://www.kaggle.com/questions-and-answers/27699
#https://docs.scipy.org/doc/numpy-1.15.1/reference/generated/numpy.fromfile.html
#//////////////////////////////
#genformtxt funciona segun la profesora para el .dat
#ayuda obedecer a la termianl su sugerencia para lo de git

#arreglos de signal.dat y incompletos.dat respectivamente
datos=np.genfromtxt("signal.dat", delimiter=" , ")
datosInc=np.genfromtxt("incompletos.dat", delimiter=" , ")

#BORRA BLOQUE
#preuba de datos
#print(datos)
#print("datos[:,iesimo]", datos[:,0])
#print("np.shape(datos)", np.shape(datos) )
#print("datos[iesimo,iesimo]", len(datos), datos[len(datos)-1, 1])
#/////////////////////
#prueba de datosInc
#print("datosInc", datosInc)
#print("datosInc[iesimo,iesimo]", datosInc[len(datosInc[:,0])-1,1])
#print("np.shape(datosInc)", np.shape(datosInc) )
#print("np.shape(datos)", np.shape(datos) )
#print("datos[iesimo,iesimo]", len(datos), datos[len(datos)-1, 1])

#3.2
#graficamos a datos, los tomamos como si no tuvieran unidades
plt.figure()
plt.plot(datos[:, 0], datos[:, 1], label="$signal.dat$")
plt.xlabel("$t$")
plt.ylabel("$f(t)$")
plt.legend(loc=0)
plt.savefig("HernandezDaniel_signal.pdf")

#3.3
#Teniendo en cuenta la seccion de Fourier con la que nos ense(n)aron en la magistral este tema, aunque ahi solo se usan los paquetes.
#la funcion dada por datos no es periodica

N = len(datos[:, 0]) # numero de puntos en el intervalo completo, es numero de filas en arreglo datos

#ESTO SE NECESITA?
#f = 200.0 # frecuencia en Hz
#dt = 1 / (f * 32 ) #32 samples por unidad de frecuencia

#def funSumandok(k, n):
#	return datos[k]*(np.exp(-1.0*(1j)*2.0*np.pi*k*( float(n)/float(N) ) )

#la funcion que da la transformada de Fourier G(n/N) es para n dado
def TransforFourier(n):
	TranFoun=[]
	for k in range(0, N ): #for i in range(0, N ):
		TranFoun.append( datos[k, 1]*(np.exp(-1.0*(1j)*2.0*np.pi*k*float(n)/float(N) ) ) ) #TranFoun.append( funSumandok(i, n) )
	return sum(TranFoun)

print(TransforFourier(1.0))
print("TransforFourier(0.0) es ", TransforFourier(0.0), "Vs np.sum(datos[:, 1]) que es", np.sum(datos[:, 1]))







