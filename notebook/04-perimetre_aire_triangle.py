# -*- coding: UTF-8 -*-

# fichier : 04-perimetre_aire_triangle.py
# auteur : David GILLARD


""" Instruction : Écrire un script qui calcule le périmètre et l'aire d'un triangle quelconque dont 
on saisira les trois côtés par la commande input().

Rappels :

L'aire vaut : 𝐴=√𝑑(𝑑−𝑎)(𝑑−𝑏)(𝑑−𝑐) où 𝑑 est le demi-périmètre ( 𝑎+𝑏+𝑐 )/2,  𝑎, 𝑏 et 𝑐 les longueurs des 
trois côtés. Pour que trois côtés forment un triangle, il faut que la longueur de chacun soit inférieure
à la somme des deux autres. Si les longueurs des côtés saisies ne forment pas un triangle, afficher 
un message d'erreur et ne pas faire les calculs."""

import math
from sys import exit 

print(""" 
Veuillez entrer les longueurs des 3 côtés 
(en séparant ces valeurs à l'aide de virgules) :""") 
a, b, c = eval(input()) 
if a < (b+c) and b < (a+c) and c < (a+b):
    print("Ces valeurs déterminent bien un triangle")
    d = (a + b + c) /2
    perimetre = a + b + c
    print("Le périmètre du triangle vaut: {:.2f}".format(perimetre))
    aire = math.sqrt(d * (d - a) * (d - b) * (d - c))
    print("Longueur des côtés =", a, b, c) 
    print ("L'aire de ce triangle est: {:.2f}".format(aire))
else:
    print("au vue des valeurs saisie il ne s'agit pas d'un triangle")
    exit()

