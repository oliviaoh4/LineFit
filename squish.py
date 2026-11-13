import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.stats import norm
from fitting_functions import *

data=np.loadtxt("data.squish.csv", delimiter=",", dtype=str)

d= data[1:,0].astype(np.float32)
print(d)
f= data[1:, 1].astype(np.float32)
print(f)
