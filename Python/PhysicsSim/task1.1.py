import math
import sympy as sym

#Exercise 1.1: The volume of a cone
d_bar = 3.23151
sigma_d = 0.0452627
h_bar = 7.39641
sigma_h = 0.0452627

#formula for cone volume
V_bar = (math.pi/12)*(d_bar**2)*h_bar
print(V_bar)

#derivatives of the volume formula with respect firstly to d_bar, then h_bar
VderD = (math.pi/12)*2*d_bar*h_bar
VderH = (math.pi/12)*(d_bar**2)

#uncertainty of V_bar
sigma_V = math.sqrt((VderD**2)*(sigma_d**2)) + ((VderH**2)*(sigma_h**2))
print(sigma_V)

#computing the relative uncertainties firstly of d_bar, then h_bar and finally V_bar
relSigma_d = round((sigma_d/d_bar), 5)
relSigma_h = round((sigma_h/h_bar), 5)
relSigma_V = round((sigma_V/V_bar), 5)
print("D: {}, H: {}, V: {}".format(relSigma_d, relSigma_h, relSigma_V))