# -*- coding: UTF-8 -*-

# fichier : 15-traitement_chaine2.py
# auteur : David GILLARD


""" Soit la chaîne de caractères suivante :

s = "abcababc"

Écrire un script créant une nouvelle chaîne en comptant le nombre de "a", en les supprimant
de la chaîne d'origine et en insérant ce nombre en fin de chaîne (pour notre 
exemple : "bcbbc3")."""

s = "abcababc"
nombre_de_caractere= s.count("a")
s = s.replace('a','')
print(f"{s}{nombre_de_caractere}")