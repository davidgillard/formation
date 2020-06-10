# -*- coding: UTF-8 -*-

# fichier : 01-entier-divisible.py
# auteur : David GILLARD

"""L'utilisateur saisie un entier positif et le programme annonce combien de fois de suite cette entier 
est divisible par 2 """

entier= int(input("Veuillez saisir un entier positif : "))
while entier < 1:
    entier = int(input("Veuillez saisir un entier STRICTEMENT POSITIF, s.v.p. : "))
save = entier

cpt = 0
while entier % 2 == 0:
    entier /= 2
    cpt += 1


print(f"l'entier {save} est {cpt} fois divisible par 2.")