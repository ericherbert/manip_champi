

#évolution du nombre de noeuds fantomes. Il faut ajuster x, V1, V3 aux fits des données expérimentales ou mettre directement les mesures de V1 et V3


import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np


def Number(x,y0,tau):
    return y0 * np.exp(x/tau)

def Ghosts(V1,V3):
    return 1 - V1/V3 * V3[10]/V1[10]

def PARAMS(synthetic):
    if synthetic:
        x   = np.arange( 0, 100, 2)
        V1  = Number( x, y0=3, tau=50)
        V3  = Number( x, y0=1, tau=20)
    else :
        local_path = 'Fichiers_test/outputData/'
        Vi  = np.loadtxt( local_path + 'all_nodes.txt' )
        # bidouille +1 pour les problèmes de V1=0 et V3=0 pour petits t
        V1  = Vi[:,1]+1 
        V3  = Vi[:,2]+1
        x   = Vi[:,0]
    return x,V1,V3


x,V1,V3 = PARAMS(synthetic=0)
ghosts  = Ghosts( V1, V3)


plt.close('all')
plt.figure('Vertices')
plt.plot(x,V1)
plt.plot(x,V3)

plt.figure('ghosts')
plt.plot(x,ghosts,'o')

plt.show(block=0)


