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

print(data)
print("height=", y)
print("Mass=", x)

y_units= "mm"
x_units= "g"

slope_units= slope_units(x_units, y_units)

print(print_equation(slope, intercept, x_units, y_units)) #The equation of the line is: y= -0.03499999999999992 mm/g x+ 45.75000000000001 mm

fig = plt.figure()
plt.scatter(t, y, label='Data')
plt.plot(t, linear(t, slope, intercept),label='Linear Fit') 
plt.legend(loc='best')
plt.xlabel("time (s)") 
plt.ylabel("distance in x direction (meters)")
plt.show()

fig.savefig('dataplot.png')
