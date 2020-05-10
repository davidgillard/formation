# -*- coding: UTF-8 -*-

# fichier : 08-type_de_triangle.py
# auteur : David GILLARD


""" Saisir trois longueurs a, b et c. Déterminer si elles permettent de construire un triangle 

(voir 04-perimetre_aire_triangle.py pour les contraintes de construction d'un triangle à partir de trois longueurs).

Dans l'affirmative, préciser si le triangle est rectangle, isocèle (deux côtés égaux), 

équilatéral ou quelconque. Sinon, afficher : "Les longueurs saisies ne forment pas un triangle !" """

import math
from sys import exit 

print(""" 
Veuillez entrer les longueurs des 3 côtés 
(en séparant ces valeurs à l'aide de virgules) :""") 
a, b, c = eval(input())              # le eval verifie que les trois valeurs ont été saisies
if a < (b+c) and b < (a+c) and c < (a+b):  # condition pour identifier un triangle
    print("Ces valeurs déterminent bien un triangle")
    d = (a + b + c) /2
    perimetre = a + b + c
    print("Le périmètre du triangle vaut: {:.2f}".format(perimetre))
    aire = math.sqrt(d * (d - a) * (d - b) * (d - c))
    print("Longueur des côtés =", a, b, c) 
    print ("L'aire de ce triangle est: {:.2f}".format(aire))
    if a*a + b*b == c*c or b*b + c*c == a*a or a*a + c*c == b*b: # à partir du théoréme de pythagore
        print("le triangle est rectangle")
    elif a == b and b == c: # si a == b == c alors équlatéral
        print("le triangle est équilatéral")
    elif a == b or a == c or b == c: # si deux cotés égaux alors isocéle
        print("le triangle est isocele")  
else:
    print("au vue des valeurs saisie il ne s'agit pas d'un triangle")
    exit()