# -*- coding: UTF-8 -*-

# fichier : 06-suite-triple.py
# auteur : David GILLARD

""" À l'aide d'une boucle, écrire un script qui affiche sur une ligne une suite de 12 nombres 
dont chaque terme soit égal au triple du terme précédent.
"""

for i in range(13):
    print(f" ",3**i, end="")