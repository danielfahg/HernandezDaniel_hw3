import numpy as np
import matplotlib.pylab as plt

print("por favor revisar este punto con python 2")

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
plt.figure()
plt.plot(datos[:, 0], datos[:, 1])
plt.savefig("HernandezDaniel_signal.pdf")



