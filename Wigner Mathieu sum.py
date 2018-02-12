from numpy import *
from scipy.special import mathieu_sem, mathieu_cem
import matplotlib.pyplot as plt
from matplotlib import cm


i = 1.0j

for zeta in range (-2, 2):

    x = linspace(-pi,pi,200)
    p = linspace(-5,5,200)
    x, p = meshgrid(x, p)

    psi = (mathieu_cem(0,-1,(x-(zeta/2))*180/pi)[0])                 
    psic = transpose(conj(mathieu_cem(0,-1,(x+(zeta/2))*180/pi)[0]))
    W = (psic*psi*exp(2*i*p*zeta))/3                                 



# Plot the figure
fig, axes = plt.subplots(figsize=(8,6))
# Make room for the x-axis label which would get clipped otherwise
fig.subplots_adjust(bottom=0.15)



# Contours and filled contours
cv = axes.contour(x, p, W, color='k')
cont = axes.contourf(x, p, W, 1000, cmap=cm.jet)


# Axis ticks and labels
axes.set_xlabel(r'x')
axes.set_ylabel(r'p', labelpad=-10)
cb = fig.colorbar(cont, ax=axes) 			# add colour bar
plt.title('Ce(order=0, q=-1, x)')
plt.show()



                             
