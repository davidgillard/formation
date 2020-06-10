# -*- coding: UTF-8 -*-

# fichier : 05-suite_fibonacci.py
# auteur : David GILLARD

""" Le programme suivant affiche les 8 premiers termes de la suite de Fibonacci, dont chaque terme est égal à la somme des deux précédents :

a, b, c = 1, 1, 1
while c < 9:
    print b,
    a, b, c = b, a+b, c+1
Pour bien comprendre le fonctionnement de cette boucle, ajouter à ce script l'affichage 
des valeurs permettant de construire la table d'état suivante :

variable	            a	b	c
valeur initiale	        1	1	1
valeur au tour suivant	...	...	...
valeur au tour suivant	...	...	...
                        ...	...	...
"""

a, b, c = 1, 1, 1
print("variable\t\t a\t b\t c")
print("valeur initiale\t\t 1\t 1\t 1")

while c < 9:
    a, b, c = b, a+b, c+1
    print("valeur au tour suivant\t", a,"\t", b,"\t",c)
