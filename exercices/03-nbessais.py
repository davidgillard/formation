# -*- coding: UTF-8 -*-

# fichier : 03-nbessais.py
# auteur : David GILLARD

"""Soit une variable nbessais contenant un nombre de tentative déjà effectuées de saisie 
d'une valeur, ne pouvant dépasser 5 essais. Soit une variable v contenant un nombre entier 
que l'on veut strictement positif, divisible par 3 (e reste de sa disivion entière par 3 
doit être nul) et strictement inférieur à 100. 

Donner l'expression logique qui est vraie lorsque la valeur n'est pas valide et qu'il est
encore possible de tenter une nouvelle saisie"""

nbessais < 5 (and v <= 0 or v >= 100 or v /3 != 0)
