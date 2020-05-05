#!/usr/bin/python3
#-*- encoding utf8 -*-
""" Il s'agit d'une fonction qui parcours une liste 
qui contient plusieurs listes imbriquées"""

liste_films = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91, ["Graham Chapman",["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]


"""cette fonction prends en argument 'ma_liste' qui 
peut contenir n'importe quelle type de liste (imbriquées y compris)
tout les éléments sont fournis dans une liste 
qui s'affiche à l'écran
"""
def print_lol(ma_liste):
    for chaque_film in ma_liste:
        if isinstance(chaque_film, list):
            print_lol(chaque_film)
        else:
            print(chaque_film)

print_lol(liste_films)