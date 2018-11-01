import numpy as np
import matplotlib.pylab as plt
from scipy.fftpack import fft, fftfreq
from scipy import interpolate

print("Por favor revisar este punto con python 2")

#3.1


#arreglos de signal.dat y incompletos.dat respectivamente
datos=np.genfromtxt("signal.dat", delimiter=" , ")
datosInc=np.genfromtxt("incompletos.dat", delimiter=" , ")


#3.2
#graficamos a datos, los tomamos como si no tuvieran unidades
plt.figure()
plt.plot(datos[:, 0], datos[:, 1], label="$signal.dat$")
plt.xlabel("$t$")
plt.ylabel("$f(t)$")
plt.legend(loc=0)
plt.savefig("HernandezDaniel_signal.pdf")



#3.3
def TraFou(arrY):
	arrYFou=[]#arrYFou=np.array([])
	for n in range(0, len(arrY) ):
		variable=0.0
		for k in range(0, len(arrY)  ):
			variable=variable+( arrY[k]*(np.exp(-1.0*(1j)*2.0*np.pi*k*float(n)/float(len(arrY)) ) ) )
		
		arrYFou.append(variable)
	return arrYFou

#3.4
#plt.plot(frecDatos, np.abs(datosFouYLib), c="green")
plt.figure()
datosFouY=TraFou(datos[:, 1])
#print("datosFouY", datosFouY)
disMue=( datos[len(datos[:, 0])-1, 0]-datos[0, 0])/len(datos[:, 0]) #distancia (o tiempo) por muestra o sample
datosFouFre=fftfreq(len(datos[:, 0]), disMue)
plt.plot(datosFouFre, np.abs( datosFouY), label="$T.$ $Fourier$ $de$ $signal.dat$ ")
plt.xlabel("$w$")
plt.ylabel("$F(f)(w)$")
plt.legend(loc=0)
#plt.show()
plt.savefig("HernandezDaniel_TF.pdf")

#3.5
print("Punto 3.5: Las frecuencias principales de mi se(n)al son en las que ocurren los picos mas grandes, es decir en  w=-393, -213, -143, aproximadamente 0, 143, 213, 393, en radianes por segundo ")

#3.6
#arrFouFre ya se debe haber pasado por fftfreq
def filPasBaj(fc, arrYFou, arrFouFre):
	arrYFouFil=np.copy( arrYFou )
	for i in range(0, len(arrYFou) ):
		if arrFouFre[i]>=fc:
			arrYFouFil[i]=0.0
	return arrYFouFil

plt.figure()
datosFouYFil=filPasBaj(1000.0, datosFouY, datosFouFre)
InvDatosFouYFil=np.fft.ifft(datosFouYFil)
plt.plot(datos[:, 0], InvDatosFouYFil)
plt.savefig("HernandezDaniel_filtrada.pdf")

#3.7
print("Punto 3.7: TraFou(arrY)apoyandonos en la grafica GraficaIncompletos.pdf hecha para este punto vemos que hay muchos puntos en el eje horizontal que estan muy espaciados, por lo que perdemos bastante informacion de lo que pasa en el medio de ellos, ademas de que en principio esta funcion no es continua por estos saltos notables y grandes, y la trasnformada de Fourier solo se puede calcular para funciones continuas en su forma analitica porque esta definida como una integral. Ya que falta informacion y por esto mismo la funcion resulta incompleta en ciertas partes, no es continua  y en principio nuestra aproximacion numerica de la transformada de Fourier no se estaria aplicando correctamente. Por eso no se puede.")
plt.figure()
plt.plot(datosInc[:, 0], datosInc[:, 1])
plt.savefig("GraficaIncompletos.pdf")

#3.8
#tomando mi implementacion de la tarea 2
def interpolar(arrDatos, arrX):
		
	funCuaDatosY=interpolate.interp1d(arrDatos[:,0], arrDatos[:, 1], kind='quadratic') #esto es una funcion funCuaDatosY(x) con x un numero tipo float en el eje x, la funcion retorna el valor en y para ese x segun la interpolacion cuadratica
	
	CuaDatosY=funCuaDatosY(arrX)
	
	funCubDatosY=interpolate.interp1d(arrDatos[:,0], arrDatos[:, 1], kind="cubic")
	
	CubDatosY=funCubDatosY(arrX)
	
	
	return CuaDatosY, CubDatosY

datosIncIntX=np.linspace(0.000390625, 0.028515625, 512)

datosIncIntCuaY, datosIncIntCubY= interpolar(datosInc, datosIncIntX)

#tran. Fourier:
datosIncIntCuaYFou=TraFou(datosIncIntCuaY)
datosIncIntCubYFou=TraFou(datosIncIntCubY)
datosIncIntFouFre=fftfreq(len(datosIncIntX), datosIncIntX[1]-datosIncIntX[0] )

plt.figure()
#plt.subplots(331)

plt.plot(datosFouFre, np.abs( datosFouY), label="$T.$ $Fourier$ $de$ $signal.dat$ ")
plt.xlabel("$w$")
plt.ylabel("$F(f)(w)$")

plt.plot(datosIncIntFouFre, np.abs( datosIncIntCuaYFou), label="$T.$ $Fourier$ $de$ $interpoladosCua$ ")
#plt.xlabel("$w$")
#plt.ylabel("$F(f)(w)$")

plt.plot(datosIncIntFouFre, np.abs( datosIncIntCubYFou), label="$T.$ $Fourier$ $de$ $interpoladosCubica$ ")
#plt.xlabel("$w$")
#plt.ylabel("$F(f)(w)$")

plt.legend(loc=0)

plt.savefig("HernandezDaniel_TF_interpola.pdf")



		
	












