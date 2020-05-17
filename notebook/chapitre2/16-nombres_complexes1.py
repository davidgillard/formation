# -*- coding: UTF-8 -*-

# fichier : 16-nombres_complexes1.py
# auteur : David GILLARD


""" On donne les nombres complexes suivants :  𝑧1=−1+2𝑗  et  𝑧2=3+4𝑗 
Calculer :

1. 𝑧1+𝑧2 
2. 𝑧1−𝑧2 
3. 𝑧1−3𝑧2 
4. 𝑧1𝑧2 
5. 𝑧1/𝑧2 """

import math

z1 = complex(-1, 2)
z2 = complex(3, 4)
z = z1 + z2
print(f"l'addition de {z1} et {z2} donne : {z}")
z = z1 - z2
print(f"la soustraction de {z1} à {z2} donne : {z}")
z = z1 - 3 * z2
print(f"le soustraction de {z1} à -3*{z2} donne : {z}")
z = z1 * z2
print(f"le produit de {z1} par {z2} donne : {z}")
z = z1 / z2
print(f"la division de {z1} par {z2} donne : {z}")

