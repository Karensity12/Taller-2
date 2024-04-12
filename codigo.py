import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.io

#1
array4 = np.random.rand(10,40,30,100)

#2
array3 = array4.copy()[:,:,:,2]


#3
print(f"Tamaño:", array3.size)
print(f"Forma", array3.shape)
print(f"Dimension:",array3.ndim)
print(f"Bites cada elemento:",array3.itemsize)
print(f"Tipo:",array3.dtype)
print(f"Total bites:",array3.nbytes)

#4
array2 = np.reshape(array3,(400,30))

#5
def dataframe(array2):
    return pd.DataFrame(array2)

#6
def cargar_mat(ruta):
    return scipy.io.loadmat(ruta)
def cargar_csv(ruta):
    return pd.read_csv(ruta)

#7
def suma(matriz, eje = None):
    return np.sum(matriz, axis = eje)
def resta(matriz, eje = None):
    return np.substract.reduce(matriz, axis = eje)
def division(matriz, eje = None):
    return np.divide(matriz, axis = eje)
def logaritmo(matriz, eje = None):
    return np.log(matriz, axis = eje)
def promedio(matriz, eje = None):
    return np.mean(matriz, axis = eje)
def desviacion(matriz, eje = None):
    return np.std(matriz, axis = eje)

#8

#9
class Graficar:
    def __init__(self, datos):
        self.datos = datos
    def graficar(self, datos):
        plt.plot(datos)
        plt.show()
    
    def graficar_h(self,datos):
        plt.hist(datos)




