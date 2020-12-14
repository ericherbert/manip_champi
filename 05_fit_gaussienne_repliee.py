

import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np


def gauss(x,A,x0,sigma):
    return A * np.exp(-(x-x0)**2/(2*sigma**2))

def gauss_repliee(x,A,x0,sigma):
    return gauss(x,A,x0,sigma) + gauss(-x,A,x0,sigma)


x = np.arange(-2.5,7.5,1)
y = np.array([0,1,2,3,4,5,4,3,2,1])

n = len(x)


#### normale


# valeurs initiales de l'amplitude, moyenne et écart type
A = 1
mean = np.mean(y)
sigma = 1

popt,pcov = curve_fit( gauss, x, y, p0=[ A, mean, sigma])

print("Amplitude\tMean\tstd")
print(popt)
perr = np.sqrt(np.diag(pcov))
print(perr)

plt.figure('fit gaussienne')
plt.plot(x,y,'ro',label='data')
plt.plot(x,gauss(x,*popt),'r+:',label='fit')


### repliee

xr = x[ x>0 ]
yr = y[ x>0 ]
ym = y[ x<0 ]
yr = yr + np.pad( ym, (len(yr)-len(ym),0), constant_values=(0,0))[::-1]

popt,pcov = curve_fit( gauss_repliee, xr, yr, p0=[ A, mean, sigma])

print("Amplitude\tMean\tstd")
print(popt)
perr = np.sqrt(np.diag(pcov))
print(perr)

plt.plot( xr, yr,'ko', label='data')
plt.plot( xr, gauss_repliee(xr,*popt),'k+:',label='fit')

plt.plot([0,0],plt.ylim(),'-')
plt.xlabel('X')
plt.ylabel('f')

plt.show()




