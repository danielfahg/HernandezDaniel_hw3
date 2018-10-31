import numpy as np
import matplotlib.pylab as plt
#import scipy
#from scipy.misc import imread #no funciona
from matplotlib.pyplot import imread
from scipy.fftpack import fft, fftfreq

print("Por avor revisar este punto con Python 2")
#4.1
arrIma=imread("arbol.png")#arrIma=scipy.misc.imread("arbol.png")

#BORRA BLOQUE O LINEA
#print("arrIma", arrIma, np.shape(arrIma))

#https://pypi.org/project/imread/ puede ayudar a que funcione el metodo, o que debo instlarle a mi computador
#https://stackoverflow.com/questions/9298665/cannot-import-scipy-misc-imread

#4.2
FouZ=np.fft.fft2(arrIma)

#BORRA bloque
#print(FouZ)
#print(np.shape(FouZ))

plt.figure()

plt.savefig("HernandezDaniel_FT2D.pdf")

