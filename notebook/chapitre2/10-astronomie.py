# -*- coding: UTF-8 -*-

# fichier : 10-astronomie.py
# auteur : David GILLARD


""" En astronomie, une approximation classique est : 1 année vaut :  𝜋×107  secondes.

Quelle est l'erreur relative de cette approximation pour une année non bissextile ?

Rappel : L'erreur relative d'une approximation  𝑎  par rapport à une valeur réelle  𝑟  

se calcule en prenant : (a - r) / r """

import math

#Une année non bissextile est de 365 jours 

erreur_relative  =  (math.pi * 107 - 365) / 365

print(erreur_relative)
