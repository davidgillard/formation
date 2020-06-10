# -*- coding: UTF-8 -*-

# fichier : 07-multiple_de_7.py
# auteur : David GILLARD

""" Écrire un script qui calcule les 50 premiers termes de la table de multiplication par 13, 
mais n'affiche que les termes qui sont multiples de 7.
"""

for i in range(51):
    if (13*i%7)==0:
        print (f"13*",i, "=",13*i)