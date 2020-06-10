# -*- coding: UTF-8 -*-

# fichier : 11-triangle_mirroir.py
# auteur : David GILLARD

"""
Écrire un script qui affiche, à l'aide de boucles, la suite de symboles suivante :

*                  *
**                **
***              ***
****            ****
*****          *****
******        ******
*******      *******
********    ********
*********  *********
********************

"""
hauteur = int(input("Veuillez saisir la hauteur : "))

for i in range(1, int(hauteur/2)):
    print('*'*i + ' '*(hauteur-2*i) + '*'*i)
