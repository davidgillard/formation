# -*- coding: UTF-8 -*-

# fichier : 12-produit_vectoriel.py
# auteur : David GILLARD


""" Le produit vectoriel

On représente les vecteurs en dimension 3 et en repère orthonormé par des listes de 3 éléments.

Saisir deux listes de trois flottants. Par exemple :

v = [1.0, 2.0, 3.0]
w = [4.0, 5.0, 6.0]
Écrire un script qui calcule et affiche le produit vectoriel de ces deux vecteurs et le sinus 
de l'angle géométrique entre ces deux vecteurs.

Rappels :

Le produit vectoriel 𝑝𝑣(𝑝𝑣𝑥,𝑝𝑣𝑦,𝑝𝑣𝑧) de deux vecteurs 𝑣(𝑣𝑥,𝑣𝑦,𝑣𝑧) et 𝑤(𝑤𝑥,𝑤𝑦,𝑤𝑧) est :

𝑝𝑣𝑥=𝑣𝑦.𝑤𝑧−𝑣𝑧.𝑤𝑦 
𝑝𝑣𝑦=𝑣𝑧.𝑤𝑥−𝑣𝑥.𝑤𝑧 
𝑝𝑣𝑧=𝑣𝑥.𝑤𝑦−𝑣𝑦.𝑤𝑥 

Le sinus entre deux vecteurs  𝑣  et  𝑤  est  |𝑝𝑣|/(|𝑣|.|𝑤|)
 """

import math

v = [1.0, 2.0, 3.0]
w = [4.0, 5.0, 6.0]

pvx = v[1] * w[2] - v[2] * w[1]
pvy = v[2] * w[0] - v[0] * w[2]
pvz = v[0] * w[1] - v[1] * w[0]

print("Les coordonnées du produit vectoriel sont : {:.2f} {:.2f} {:.2f} ".format(pvx, pvy, pvz))


sinus = 

#cosinus = ps / (v_abs * w_abs)
#print("Le cosinus de l'angle entre les deux vecteurs v et w vaut : {:.2f}".format(cosinus))

