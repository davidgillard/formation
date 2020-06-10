# -*- coding: UTF-8 -*-

# fichier : 02-volume_cone.py
# auteur : David GILLARD

"""Ecrire un programme qui à partir de la saisie d'un rayon et d'une hauteur, calcul le volume
d'un cone droit (on rappelle que le volume du cône est donné par : V = (pi*r^2*h)/3 ou r et h 
sont respectivement le rayon et la hauteur du cylindre """


import math

print(""" 
Veuillez entrer les valeurs de r et h  
(en séparant ces valeurs à l'aide de virgules) :""")
r, h = eval(input())              # le eval verifie que les deux valeurs ont été saisies
 
volume = (math.pi * r * r * h)/ 3
print("Le volume du cône est de : {:.2f}".format(volume), "m3")