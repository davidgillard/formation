# -*- coding: UTF-8 -*-

# fichier : 14-traitement_chaine1.py
# auteur : David GILLARD


""" Soit la chaîne de caractères suivante :

s = "abcababc"

Écrire un script créant une nouvelle chaîne en regroupant tous les "a" en début de chaîne 
tout en conservant l'ordre des autres caractères."""

s = "abcababc"
nombre_de_caractere= s.count("a")
print(nombre_de_caractere)

for caractere in s:
    b = caractere.find('a')
    print(b)
    #print(caractere, end='')


# première_substitution = dna.replace('a', 't')
# print("première substitution :", première_substitution)
# seconde_subsitution = première_substitution.replace('t', 'g')
# print("seconde substitution :", seconde_subsitution)