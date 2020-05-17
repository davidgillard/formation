# -*- coding: UTF-8 -*-

# fichier : 11-produit_scalaire.py
# auteur : David GILLARD


""" Le produit scalaire

On représente des vecteurs en dimension 3  (𝑥,𝑦,𝑧)  par des listes de 3 éléments.

Saisir deux listes de trois flottants. Par exemple :

v = [1.0, 2.0, 3.0]
w = [4.0, 5.0, 6.0]
Écrire un script qui calcule et affiche le produit scalaire de ces deux vecteurs et 
le cosinus de l'angle entre ces deux vecteurs.

Quel est le cosinus de l'angle entre les vecteurs  𝑣  et  𝑤  ?

Rappels :

Le produit scalaire de deux vecteurs  𝑣(𝑣𝑥,𝑣𝑦,𝑣𝑧)  et  𝑤(𝑤𝑥,𝑤𝑦,𝑤𝑧)  est  𝑝𝑠=(𝑣𝑥.𝑤𝑥+𝑣𝑦.𝑤𝑦+𝑣𝑧.𝑤𝑧) .
La norme d'un vecteur  𝑣(𝑥,𝑦,𝑧)  est  |𝑣|=√𝑥2+𝑦2+𝑧2.
Le cosinus entre deux vecteurs v et w est  𝑝𝑠/(|𝑣|.|𝑤|) .
 """

import math

v = [1.0, 2.0, 3.0]
w = [4.0, 5.0, 6.0]

ps = v[0] * w[0] + v[1] * w[1] + v[2] * w[2]
print("Le produit scalaire vaut : {:.2f}".format(ps))

v_abs = math.sqrt(v[0]**2 + v[1]**2 + v[2]**2)
w_abs = math.sqrt(w[0]**2 + w[1]**2 + w[2]**2)

cosinus = ps / (v_abs * w_abs)
print("Le cosinus de l'angle entre les deux vecteurs v et w vaut : {:.2f}".format(cosinus))

