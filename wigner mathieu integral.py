from numpy import *
from scipy.special import mathieu_cem
import matplotlib.pyplot as plt
from matplotlib import cm
from scipy.integrate import quad

## parameters ##
i = 1.0j
x = linspace(-pi,pi,200)
p = linspace(-5,5,200)
x, p = meshgrid(x, p)
y = linspace(-pi, pi, 200)

psi = (mathieu_cem(0,-1,(x-y/2)*180/pi)[0]) 
psic = transpose(conj(mathieu_cem(0,-1,(x+y/2)*180/pi)[0]))

## defining the integral ##
def integrand(y, x, p):
    return psic*psi*exp(2*i*p*y)

## generating Wigner function ##
def W(x, p):
    return quad(integrand, -pi, pi, args=(x, p))[0]

W = vectorize(W)
# Plot the figure
fig, axes = plt.subplots()


# Contours and filled contours

cont = axes.contourf(x, p, W, 1000, cmap=cm.jet)

# Axis ticks and labels
axes.set_xlabel(r'x')
axes.set_ylabel(r'p', labelpad=-10)
cb = fig.colorbar(cont, ax=axes) 			# add colour bar
plt.show()
