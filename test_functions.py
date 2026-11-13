

from fitting_functions import *


m=2
x=3
b=4

print(linear(m, x, b))

x_units="meters"
y_units="kg"

print(slope_units(x_units, y_units))

print(print_equation(m, b, slope_units))
