

# estimation de la sphericité d'un nuage de point, basé sur les vecteurs propre de la matrice d'inertie. 
# x,y sont les coordonnées des noeuds, ici calculées, il faut les remplacer par les données véritables.


import matplotlib.pyplot as plt
import numpy as np


def matrice_inertie(x,y) :
    # x, y coordonnées des masses identiques
    x0  = np.mean(x)
    y0  = np.mean(y)
    A1  = np.sum( (x-x0)**2 )
    A4  = np.sum( (y-y0)**2 )
    A2  = np.sum( (x-x0)*(y-y0) )
    A3  = A2
    I = np.array( [[A1,A2], [A3,A4]] )
    return I

def Linalg(I):
    # extraction valeurs propres / vecteurs propres
    E, P = np.linalg.eig(I)
    D = np.diag(E)
    return E,P
    
def Sphericite(D):
    l2 = np.min(E)
    l1  = np.max(E)
    return 2*l2/(l1+l2)

   
def PARAMS():
    x   = np.random.rand(100)
    y   = np.random.rand(100)

    shift_x = 1
    shift_y = 1

    x   = extension(shift_x,x)
    y   = extension(shift_y,y)
    return x,y

def extension(alpha,x):
    return alpha*x

x,y = PARAMS()

I   = matrice_inertie(x,y)
E,P   = Linalg(I) # valeurs propres
sphericite = Sphericite(E)
print('sphericite :')
print( sphericite )




'''
print('I')
print(I)
print('P')
print(P)
print('E')
print(E)
print('verif')
print( I - P.dot(D.dot(np.linalg.inv(P) )))
'''

plt.close('all')

plt.figure('Vertices')
plt.plot(x,y,'o')

plt.show(block=0)


