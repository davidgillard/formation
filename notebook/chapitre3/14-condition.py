# -*- coding: UTF-8 -*-

# fichier : 14-condition.py
# auteur : David GILLARD

""" Que fait le programme ci-dessous, dans les quatre cas où l'on aurait défini au préalable 
que la variable a vaut 1, 2, 3 ou 15 ?

if a != 2:
    print('perdu')
elif a == 3:
    print('un instant, s.v.p.')
else :
    print('gagné’)

"""

# pour les valeurs suivante :
# 1: affiche perdu
# 2: affiche gagné
# 3: affiche perdu
# 15: affiche perdu

for a in [1, 2, 3, 15]:
    if a != 2:
        print('perdu')
    elif a == 3:
        print('un instant, s.v.p.')
    else :
        print('gagné')
