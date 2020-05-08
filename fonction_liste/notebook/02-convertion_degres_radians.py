# -*- coding: UTF-8 -*-

# fichier : conversion_degres_en_radians.py
# auteur : David GILLARD

"""Saisir les valeurs degrés, minutes et secondes d'un angle, puis le convertir en radians.  
Faire également la conversion inverse depuis une saisie en radians.

Afficher une valeur approchée, avec deux décimales, de 1 radian exprimé en degrés."""

import math

degre = 75
minute = 19
seconde = 20
radian = (75 + minute/60 + seconde/3600) * math.pi/180
print("{:.2f}".format(radian), "degres")

saisie_radian = 1.31
dms = saisie_radian * 180/math.pi
print("{:.2f}".format(dms), "Radians")