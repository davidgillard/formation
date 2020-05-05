#!/usr/bin/python3
#-*- encoding utf8 -*-

liste_films = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91, ["Graham Chapman",["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]

def print_lol(ma_liste):
    for chaque_film in ma_liste:
        if isinstance(chaque_film, list):
            print_lol(chaque_film)
        else:
            print(chaque_film)

print_lol(liste_films)