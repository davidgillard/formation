# -*- coding: UTF-8 -*-

# fichier : 06-calcul_periode_pendule.py
# auteur : David GILLARD


""" Instruction : Écrire un script qui fasse saisir la longueur 𝑙 d'un pendule simple et 
qui calcule sa période 𝑇 .

Rappel : 𝑇=2𝜋√𝑙/𝑔, où 𝑔 est l'accélération de la pesanteur, 𝑔 = 9,81 m/s2

Afficher le résultat sans oublier les unités !

Quelle est la période correspondant à un pendule suspendu en haut de la tour Eiffel ( 𝑙 = 300 m) ? """

import math

l = float(input("Veuillez saisir la longueur du pendule: "))
g = 9.81

T = 2 * math.pi * math.sqrt(l / g)
print("La période du pendule pour une longueur de l est de {:.2f}".format(T), "m/s2")