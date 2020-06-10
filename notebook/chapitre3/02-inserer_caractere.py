# -*- coding: UTF-8 -*-

# fichier : 02-inserer_caractere.py
# auteur : David GILLARD


""" Écrire un script qui recopie une chaîne en insérant un astérisque entre ses caractères.

Utilisez une boucle while.

Par exemple "Gaston" deviendra "G*a*s*t*o*n"  """

chaine = input("Veuillez saisir une chaine de caractére : ")
caractere_separation = '*'
while True:
    print(caractere_separation.join(chaine))
    break
