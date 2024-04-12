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




