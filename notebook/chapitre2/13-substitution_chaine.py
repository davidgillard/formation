# -*- coding: UTF-8 -*-

# fichier : 13-substitution_chaine.py
# auteur : David GILLARD


""" Soit la chaîne de caractères suivante :

dna = "tgaattctatgaatggactgtcccaaagaagtagggacccac"

Écrire un script qui affiche la chaîne dna après avoir remplacé la lettre "a" par "t" puis 
la lettre "t" par "g"."""

dna = "tgaattctatgaatggactgtcccaaagaagtagggacccac"
print("chaine initiale :", dna)

première_substitution = dna.replace('a', 't')
print("première substitution :", première_substitution)
seconde_subsitution = première_substitution.replace('t', 'g')
print("seconde substitution :", seconde_subsitution)