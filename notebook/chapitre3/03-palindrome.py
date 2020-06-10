# -*- coding: UTF-8 -*-

# fichier : 03-palindrome.py
# auteur : David GILLARD


""" Écrire un script qui recopie une chaîne en l'inversant et qui indique si elle est un palindrome. 
Utilisez une boucle while.

Un palindrome est un texte dont l'ordre des lettres permet de le lire identiquement de gauche 
à droite ou de droite à gauche. Par exemple :

chaîne de départ	chaîne transformée	palindrome ?
"zorglub"	        "bulgroz"	        non
"radar"	            "radar"	            oui

"""
s = "radar"
i = 0

while i <= len(s)/2:
    #print(s[i])
    #print(s[::-1])
    if s[i] != s[-i -1]:
        print("c'est pas un palindrome")
    else:
        print("C'est un palindrome")
    i += 1
    break