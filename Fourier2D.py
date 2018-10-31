import numpy as np
import matplotlib.pylab as plt
#import scipy
#from scipy.misc import imread #no funciona
from matplotlib.pyplot import imread
from scipy.fftpack import fft, fftfreq
from matplotlib.colors import LogNorm

print("Por favor revisar este punto con Python 2")
#4.1
arrIma=imread("arbol.png")#arrIma=scipy.misc.imread("arbol.png")

#BORRA BLOQUE O LINEA
#print("arrIma", arrIma, np.shape(arrIma))

#https://pypi.org/project/imread/ puede ayudar a que funcione el metodo, o que debo instlarle a mi computador
#https://stackoverflow.com/questions/9298665/cannot-import-scipy-misc-imread

#4.2
FouZ=np.fft.fft2(arrIma)
FouZShift=np.fft.fftshift(FouZ)#para centrar


#BORRA bloque
#print(FouZ)
#print(np.shape(FouZ))
#print(np.log( np.abs(FouZ) ) )
print("FouZShift", FouZShift)
print(np.abs( FouZ ))
print("max y min", np.amax(FouZ), np.amin(FouZ))

plt.figure()
#plt.imshow(arrIma) #CAMBIA POR FouZ
#np.abs() para que de la magnitud de los numeros complejos y no algo complejo, norm=LogNorm() para escala logaritmica y que se vea la diferencia entre las amplitudes pues todas parecidas y grandes de lo contrario
#plt.imshow(np.real(FouZShift), norm=LogNorm())
plt.imshow(np.abs(FouZShift), norm=LogNorm())#plt.imshow(np.log( np.abs(FouZShift) ) )
#plt.imshow(np.abs(FouZShift)  )
plt.savefig("HernandezDaniel_FT2D.pdf")

#4.3
def filtro():
	#aplicamos el filtro a FouZ
	#FouZFil=np.zeros( (len(FouZ[:, 0]),len(FouZ[0, :])) )
	for i in range(0, len(FouZ[:, 0]) ): #recorremos y accdemos a todas las filas de FouZ
		for j in range(0, len(FouZ[0, :]) ): #recorremos y accdemos a todas las columnas de FouZ
			#condiciones y acciones de filtro
			if (1500.0<=FouZ[i, j] and FouZ[i, j]<=4500.0): #OJO NO LOPIERDAS!!! if (FouZ[i, j]<=0.0):
				#FouZFil[i, j]=0.0#0.0 + (0.0*(1j)) #o 0.0 + (0.0*(1j)) o complex(0.0) o 0 ENTERO
				FouZ[i,j]=0.0
			#else:
			#	FouZFil[i, j]=FouZ[i, j]
	#return FouZFil

filtro()

FouZFilShift=np.fft.fftshift(FouZ)
#FouZFilShift=np.fft.fftshift( filtro() )

plt.figure()
#plt.imshow(arrIma) #CAMBIA POR FouZ
#np.abs() para que de la magnitud de los numeros complejos y no algo complejo, norm=LogNorm() para escala logaritmica y que se vea la diferencia entre las amplitudes pues todas parecidas y grandes de lo contrario
plt.imshow(np.abs(FouZFilShift), norm=LogNorm())#plt.imshow(np.log( np.abs(FouZShift) ) )
#plt.imshow(np.real(FouZFilShift), norm=LogNorm())
#plt.imshow(np.abs(FouZShift)  )
plt.savefig("HernandezDaniel_FT2D_filtrada.pdf")


#4.5
InvFouZFil=np.fft.ifft2(FouZ) #, norm=None
arrParaImaFil=np.array(InvFouZFil)

plt.imsave("HernandezDaniel_Imagen_filtrada.pdf", np.real(arrParaImaFil), cmap="gray")


