# -*- coding: UTF-8 -*-

# fichier : 09-borne.py
# auteur : David GILLARD

""" Écrire un script qui saisit deux bornes entières a et b, avec a < b (utiliser une saisie 
filtrée). Afficher la somme des nombres multiples de 3 et de 5 strictement compris entre ces 
bornes. Puis afficher la somme des nombres multiples de 3 ou de 5.
"""

a = int(input("Entrez un entier a compris [1 .. 100] : "))
while not(1 <= a <= 100) :
    a = int(input('Entrez un entier a compris [1 .. 100], S.V.P. : '))
b = int(input("Entrez un entier b supérieur à a et compris [1 .. 100] : "))
while not(1 <= b <= 100) :
    b = int(input('Entrez un entier b supérieur à a et compris [1 .. 100], S.V.P. : '))

# Une premiére solution
somme = 0
for i in range(a, b):
    if i%3 == 0 and i%5 == 0:
        somme += i
print(somme)

# une seconde solution plus condensé 
#print(sum(i for i in range(a, b) if i%3 == 0 and i%5 ==0))
