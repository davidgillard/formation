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

#hauteur = int(input("Veuillez saisir une hauteur : " ))

for i in range(1, 11):
    print('*'*(11-i) + ' '*(2*(i-1)) + '*'*(11-i))
for i in range(1, 11):
    print('*'*i + ' '*(20-2*i) + '*'*i) 