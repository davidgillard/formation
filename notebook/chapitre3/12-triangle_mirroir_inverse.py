# -*- coding: UTF-8 -*-

# fichier : 12-triangle_mirroir_inverse.py
# auteur : David GILLARD

""" Écrire un script qui affiche, à l'aide de boucles, la suite de symboles suivante :

********************
*********  *********
********    ********
*******      *******
******        ******
*****          *****
****            ****
***              ***
**                **
*                  *

"""
hauteur = int(input("Veuillez saisir une hauteur : " ))

for i in range(1, int(hauteur/2)):
    print("*"*(int(hauteur/2-i)) + " "*(2*(i-1)) +"*"*(int(hauteur/2-i)))