#!/usr/bin/python3
# -*- encoding utf8 -*-

# definition d'une liste et affichage d'un film
movies = ["The Holy Grail", 1975, "The life of Brian", 1979, "The meaning of life", 1983]
print(movies[2])


# définition d'une liste et affiche l'ensemble de la liste par un boucle for
films = ["The Holy Grail", "the life of Brian", "The meaning of life"]
for chaque_film in films:
    print(chaque_film)

liste_films = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91, ["Graham Chapman",["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]

print(liste_films[4][1][3])
print("#######################################################")
for les_films in liste_films:
    print(les_films)
print("#######################################################")

list_prenoms = ['Michael', 'Terry', 'Marina', 'David']
isinstance(list_prenoms, list) # renvoie si list_prenom est une liste (True) sinon (False)
nbres_prenoms = len(list_prenoms) # nbres_prenoms stocke la taille de la liste list_prenoms
status_nbres_prenoms = isinstance(nbres_prenoms, int)
print(status_nbres_prenoms)
print("le nombre de prénom contenu dans la liste est de : %i " %nbres_prenoms)


# réécriture de ce qui est au dessus en utilisant isinstance afin de controler l'existence d'une liste
# liste_films = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91, ["Graham Chapman",["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]
print("#########################################################")
print("boucle for sur les listes")
print("#########################################################")
for les_films in liste_films:
    if isinstance(les_films, list):
        for liste_imbrique in les_films:
            if isinstance(liste_imbrique, list):
                for contenu in liste_imbrique:
                    print(contenu)
            else:
                print(liste_imbrique)
    else:
        print(les_films)