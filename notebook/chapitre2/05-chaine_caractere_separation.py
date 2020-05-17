# -*- coding: UTF-8 -*-

# fichier : 05-chaine_caractere_separation.py
# auteur : David GILLARD


""" Instruction : Écrire un script qui fasse saisir une chaîne et un caractère de séparation, 
et qui l'insére entre les caractères de la chaîne.

Utiliser la fonction join().

Par exemple, si l'utilisateur saisit "Gaston" et choisit "*", alors le script 
affichera "G*a*s*t*o*n"."""

chaine = input("Veuillez saisir une chaine de caractére : ")
caractere_separation = '*'
print(caractere_separation.join(chaine))