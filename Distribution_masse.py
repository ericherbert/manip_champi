# coding: utf-8

import numpy as np
#from numpy import arctan2, sqrt
#import numexpr as ne
import math
import networkx as nx
import scipy.interpolate
import os as os

# Sort la localisation de chacun des noeuds de degré 2

def PARAMS():
    path = '/home/eh/DD2/recherche/hyphes_croissance/data/2019_04_09_P_S_M2/VST/'
    path_s =  '/outputData/'
    s_name = "mass_distribution"
    center = (2883,3337) # taille de l'image (6417,6825)
    return path, path_s, s_name, center

def get_distribution( path, path_s, s_name):

    allfiles = os.listdir(path)
    files = [ fname for fname in allfiles if fname.endswith('.gpickle')]
    #print files

    for inc in range(len(files)): #
#    print(files[inc])
        coord = localisation( path, files[inc], center)
        np.savetxt( path + path_s + s_name + '_' + files[inc] + '.txt', np.transpose(coord) )


def localisation( filepath, filename, center=(0,0)) :

    # import données
    DG = nx.read_gpickle(filepath + filename) 
    # pour etre sur que l'indexation des noeuds est ordonnée
    DG = nx.convert_node_labels_to_integers(DG, first_label=0, ordering='default', label_attribute=None)  

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
        x_ord = np.append( x_ord, np.subtract(DG.nodes[inc]['x'],center[0]))
        y_ord = np.append( y_ord, DG.nodes[inc]['y'] - center[1])

    coord = np.append(  [x_ord], [y_ord], axis=0)
    coord = np.append( coord, [weight], axis=0)

    print('Longueur totale:')
    print(ltot)
    
    return coord


if __name__ == "__main__":

    path, path_s, s_name, center = PARAMS()
    if not os.path.exists(path + path_s):
        os.makedirs(path + path_s)
    distribution = get_distribution( path, path_s, s_name)

