# -*- coding: UTF-8 -*-

# fichier : 10-triangle_mirroir.py
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
saisie = 10

for i in range(1, 10): # réalisation du premier triangle
    print("*"*i)

for j in range(saisie, 0, -1): # saisie =5 --> 4, 3, 2, 1
    s = j - 1 #4
    for k in range(0,j): #i=4 --> 0, 1, 2, 3, 4
        print("*",end="")
    print()
    for l in range(0, saisie - s): # 5-3 = 2
        print(" ",end="")

############################################################
# avec saisie d'une saisie de triangle
# saisie = int(input("Merci de saisir un entier : "))
# a = saisie - 1
# for j in range(0, saisie):
#     for k in range(0, a):
#         print(end=" ")
#     a = a - 1
#     for l in range(0, j+1):
#         print("*", end="")
#     print()

#############################################################


# code recuperer sur youtube
#########################################################
# j=1
# while j <= 5:
#     b = 1
#     while b <= 5-j:
#         print(" ", end="")
#         b = b + 1
#     k=1
#     while k <= j:
#         print("*", end="")
#         k = k+1
#     print()
#     j = j+1 
#############################################################

