# -*- coding: UTF-8 -*-

# fichier : 18-palindrome.py
# auteur : David GILLARD


"""  
Soit la chaîne de caractères suivante :

adn = "tgaattctatgaatggactgtcccaaagaagtagggacccac"
Afficher la chaîne dna, palindrome de la chaine adn.

Conseil : N'utilisez que la gestion des indices de la chaîne adn. """

adn = "tgaattctatgaatggactgtcccaaagaagtagggacccac"
print(f"La séquence initiale vaut : {adn}")
dna = adn[::-1]
print(f"La séquence inversé vaut : {dna}")