

#évolution du nombre de noeuds fantomes. Il faut ajuster x, V1, V3 aux fits des données expérimentales ou mettre directement les mesures de V1 et V3


import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np


def Number(x,y0,tau):
    return y0 * np.exp(x/tau)

def Ghosts(V1,V3):
    return 1- V1/V3 * V3[0]/V1[0]

def PARAMS():
    x   = np.arange( 0, 20, 2)
    V1  = Number( x, y0=3, tau=5)
    V3  = Number( x, y0=1, tau=3)
    return x,V1,V3


x,V1,V3 = PARAMS()
ghosts  = Ghosts( V1, V3)


plt.close('all')
plt.figure('Vertices')
plt.plot(x,V1)
plt.plot(x,V3)

plt.figure('ghosts')
plt.plot(x,ghosts,'o')

plt.show(block=0)


