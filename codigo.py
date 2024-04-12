import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.io

#1
array4 = np.random.rand(10,40,30,10)

#2
array3 = array4.copy()[:,:,:,2]
