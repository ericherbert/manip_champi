# Traitement champi

contient les codes utilisés pour faire des extractions simples depuis les gpickle

## 05 fit gaussienne repliée
Fit gaussien.
Remplacer *x* et *y* par leurs valeurs respectives. Si la distribution prend des valeurs négatives, utiliser le fit *normal*, si distribution d'une valeur absolue, prendre le fit *replié* 


## 06 ghost estimator
calcul le ratio 1-(V1+1)/(V3+1). Le +1 est une bidouille pour éviter les divisions par 0.

## 07 sphericity estimator
calul le ratio 2xl1/(l1+l2) avec l1>l2 les valeurs propres du tenseur d'inertie. Remplacer *x* et *y* par les coorodnnées des noeuds V1 ou V3. Pour les V2, il faut multiplier par la longeur du tronçon associé.


## Distribution masse

Calcul de la distribution de la masse dans le thalle. Attention à bien mettre le centre repéré sur ImageJ dans Distribution_masse 

1. Distribution_masse.py => Sort des fichiers texte, contenant la position X et Y et la longueur de chaque segment défini par un noeud de degré 2
1. plot_distribution_masse.py => Plot and save la distribution

## Comptage noeuds

1. get_all_nodes.py => appelle comptage_noeud et sort un fichier appelé all_nodes.txt contenant les listes de noeud avec leurs degré
1. comptage_noeuds.py => sous programme de get_all_nodes.py
1. read_time.py => va chercher s'il existe dans log.txt la série temporelle correspondant aux temps experimentaux et l'ajoute dans all_nodes.txt.
