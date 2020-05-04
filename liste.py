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