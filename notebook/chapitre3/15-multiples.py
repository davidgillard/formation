# -*- coding: UTF-8 -*-

# fichier : 15-multiples.py
# auteur : David GILLARD

""" Écrire un programme qui, étant données deux bornes entières a et b, additionne les nombres 
à la fois multiples de 3 et de 5 compris entre ces bornes.

Pour, par exemple, a = 0, b = 32, on obtient : 0 + 15 + 30 = 45.

"""

a = int(input("Entrez un entier a correspondant à la borne basse comprise [0 .. 100] : "))
while not(0 <= a <= 100) :
    a = int(input('Entrez un entier a correspondant à la borne basse comprise [0 .. 100], S.V.P. : '))
b = int(input("Entrez un entier b correspondant à la borne haute comprise [0 .. 100] : "))
while not(0 <= b <= 100) :
    b = int(input('Entrez un entier b correspondant à la borne haute comprise [0 .. 100], S.V.P. : '))

somme = 0
premiere_operande = True

for i in range(a, b):
    if i%3 == 0 and i%5 == 0:
        somme += i
        if i == premiere_operande:
            print(i, end="")
            premiere_operande = False
        else:
            print("+ ", i, end="")
        #somme = i
print("=", somme)
