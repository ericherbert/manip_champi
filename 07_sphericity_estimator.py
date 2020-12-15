# estimation de la sphericité d'un nuage de point, basé sur les vecteurs propre de la matrice d'inertie. 
# x,y sont les coordonnées des noeuds, qui peuvent être calculées (synthetic=1) ou provenir d'un fichier gpickle (synthetic=0). Dans ce dernier cas, il faut également définir filepath et filename dans localisation()


import matplotlib.pyplot as plt
import numpy as np


def matrice_inertie(x,y,weight) :
#    # x, y coordonnées des masses identiques
#    x0  = np.mean(x)
#    y0  = np.mean(y)
#    A1  = np.sum( (x-x0)**2 )
#    A4  = np.sum( (y-y0)**2 )
#    A2  = np.sum( (x-x0)*(y-y0) )
#    A3  = A2
    # x, y coordonnées des masses variables
    x0  = np.sum(weight*x) / np.sum(weight)
    y0  = np.sum(weight*y) / np.sum(weight)
    A1  = np.sum( weight*(x-x0)**2 )
    A4  = np.sum( weight*(y-y0)**2 )
    A2  = np.sum( weight*(x-x0)*(y-y0) )
    A3  = A2
    
    I = np.array( [[A1,A2], [A3,A4]] )
    cdm = np.array([x0,y0])
    return I,cdm

def Linalg(I):
    # extraction valeurs propres / vecteurs propres
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
    E, P = np.linalg.eig(I)
    D = np.diag(E)
    return E,P
    
def Sphericite(D):
    l2 = np.min(E)
    l1  = np.max(E)
    return 2*l2/(l1+l2)

def localisation(   filepath='./Fichiers_test/gpickle/',
                    filename='bin_FFT_regMovie_2_14_graph_r1_p5.gpickle') :
    
    import networkx as nx
    
    # import données
    DG = nx.read_gpickle(filepath + filename) 
    # pour etre sur que l'indexation des noeuds est ordonnée
    DG = nx.convert_node_labels_to_integers(    DG, 
                                                first_label=0, 
                                                ordering='default', 
                                                label_attribute=None)  

    ###longeur totale
    ltot=0
    for e in DG.edges(data=True):
            ltot+=e[2]['weight']

    graph = DG
    graph = nx.convert_node_labels_to_integers(graph, first_label=0, 
                                               ordering='default', 
                                               label_attribute=None)

    degrees = np.array([degree for node, degree in nx.degree(graph)], dtype=int) 
    nodes   = np.array([node for node, degree in nx.degree(graph)], dtype=int) 
    
    indices_hyphes = np.where(degrees==2)[0]  ## degrees=2 intermédiaires
    nodes_degre2 = nodes[indices_hyphes]
    
    # pour chaque noeud de degré 2 on récupère la position et la longueur du segment associé
    weight = np.array([])
    x_ord = np.array([])
    y_ord = np.array([])

    for inc in nodes_degre2:
#        print(list(DG.adj[inc]))
        weight = np.append( weight, DG[inc][list(DG.adj[inc])[0]]['weight'])
        x_ord = np.append( x_ord, DG.nodes[inc]['x'])
        y_ord = np.append( y_ord, DG.nodes[inc]['y'])

    coord = np.append(  [x_ord], [y_ord], axis=0)
    coord = np.append( coord, [weight], axis=0)

    print(filename)
    print('Longueur totale:\t' + str(ltot))
    
    return coord
   
def PARAMS(synthetic):
    if synthetic:
        shift_x = 1
        shift_y = 1
        num = 100
        x   = np.random.rand(num)
        y   = np.random.rand(num)
        x   = extension(shift_x,x)
        y   = extension(shift_y,y)
        weight = np.ones(num)
    elif not synthetic:
        coord = localisation()       
        x   = coord[0,:]
        y   = coord[1,:]
        weight = coord[2,:]
    return x,y,weight

def extension(alpha,x):
    return alpha*x


if __name__ == "__main__":
    # get data
    x,y,weight = PARAMS(synthetic=0)
    # compute Inertial matrix
    I,cdm   = matrice_inertie(x,y,weight)
    # get eigenvalues and eignevectors
    E,P   = Linalg(I) # valeurs propres
    # compute sphericity
    sphericite = Sphericite(E)
    print('sphericite :\t' + str(sphericite))

    # then plot
    plt.close('all')
    plt.figure('Vertices')
    plt.plot(x,y,'ob')
    plt.plot(cdm[0],cdm[1],'or')
    plt.show(block=0)


