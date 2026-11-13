import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.stats import norm
from fitting_functions import *

data=np.loadtxt("data.squish.csv", delimiter=",", dtype=str)

x= data[1:,0].astype(np.float32)
print("x=", x)
y= data[1:, 1].astype(np.float32)
print("y=", y)

params, params_cov=scipy.optimize.curve_fit(linear,x, y)
slope=params[0]
intercept=params[1]

