# -*- coding: UTF-8 -*-

# fichier : 10-créer_triangle.py
# auteur : David GILLARD

""" Écrire un script qui prend en parametre un entier (n) qui représente la hauteur du triangle, 
et permet d'afficher un triangle isocele formé d'étoile:

     *
    ***
   *****
  *******
 *********
***********

"""

# hauteur = int(input("veuillez saisir la hauteur du triangle : "))
# nombre_etoile = 1
# nombre_espace = hauteur - 1
# for i in range(hauteur):
#     print(nombre_espace*" "+nombre_etoile*"*")
#     nombre_etoile +=2
#     nombre_espace -=1 
import math

hauteur = 5
for i in range(1, hauteur):
    print(" "*(hauteur-i) + "*"*int(abs((i*3/2))) + " "*(hauteur-i))