# -*- coding: UTF-8 -*-

# fichier : 01-affectations_parallèles.py
# auteur : David GILLARD

"""Assigner les valeurs respectives 3, 5 et 7 à trois variables a, b et c en utilisant des affectations parallèles.

Effectuer les opérations a-b/c, (a-b)/c, a/b/c et a/b*c et afficher les résultats."""

a, b, c = 3, 5, 7

print(a - b / c)
print((a - b)/c)
print(a/b/c)
print(a/b*c)