# -*- coding: UTF-8 -*-

# fichier : 10-symbole.py
# auteur : David GILLARD

""" Écrire un script qui affiche, à l'aide de boucles, la suite de symboles suivante :

*
**
***
****
*****
******
*******
********
*********
**********
 *********
  ********
   *******
    ******
     *****
      ****
       ***
        **
         *
"""
saisie = int(input("Veuillez saisir la taille de la forme :"))


for i in range(1, saisie):
    print("*"*i)

for i in range(1, saisie):
    print(" "*i + "*"* (saisie-i))
    



#############################################################
# avec saisie d'une taille de triangle
# taille = int(input("Merci de saisir un entier : "))
# a = taille - 1
# for j in range(0, taille):
#     for k in range(0, a):
#         print(end=" ")
#     a = a - 1
#     for l in range(0, j+1):
#         print("*", end="")
#     print()

#############################################################

