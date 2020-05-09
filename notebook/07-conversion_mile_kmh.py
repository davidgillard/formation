# -*- coding: UTF-8 -*-

# fichier : 07-conversion_mile_kmh.py
# auteur : David GILLARD


""" Écrire un script qui convertit en mètres par seconde, en km/h et en nœuds 
une vitesse saisie en miles/heure (mph).

Rappels :

1 mile = 1609 m
1 nœud = 1 mille/h
1 mille = 1852 m (on dit aussi un mille nautique ou un nautique)
Tester les conversions pour 1 mph. """

import math

mph = float(input("Veuillez saisir la vitesse en miles/heure: "))
facteur_de_conversion = 0.62137119
kilometres_heure = mph / facteur_de_conversion
print("corresponds à {:.2f}".format(kilometres_heure), "km/h")
ms = kilometres_heure / 3.6
print("corresponds à {:.2f}".format(ms), "m/s")
kn = kilometres_heure / 1.852
print("corresponds à {:.2f}".format(kn), "knot")

