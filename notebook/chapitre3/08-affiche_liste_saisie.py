# -*- coding: UTF-8 -*-

# fichier : 08-affiche_liste_saisie.py
# auteur : David GILLARD

""" Écrire un script qui saisit des nombres et les stocke sous forme de flottants dans une liste, 
jusqu'à terminer par la saisie d'une chaîne vide en appuyant sur Entrée.
Afficher la liste résultante.
"""


# S=input()
# L=[]
# while S!=4:
#     L.append(S)
#     if S=="4":
#         break
#     S = input()
# print(L)

saisie = float(input())
liste = []
while liste!=4: 
    liste.append(saisie)
    if saisie == "4":
        break
    saisie = input()
print(liste)



# a = []
# for i in range(int(input())):
#     a.append(float(input()))
# print(a)

