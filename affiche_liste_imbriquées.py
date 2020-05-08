#!/usr/bin/python3
#-*- encoding utf8 -*-
""" Il s'agit d'une fonction qui parcours une liste 
qui contient plusieurs listes imbriquées et affiche l'ensemble des éléments de cette liste à l'écran"""

liste_films = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91, ["Graham Chapman",["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]

# """This is the "nester.py" module and it provides one function called print_lol()
# which prints lists that may or may not include nested lists."""

# """This function takes a positional argument called 'the_list', which
# is any Python list (of - possibly - nested lists). Each data item in the
# provided list is (recursively) printed to the screen on it's own line.
# A second argument called 'level' is used to insert tab-stops when a nested list is encountered."""

def print_lol(the_list, level):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, level-9)
        else:
            for tab_stop in range(level):
                print("\t", end='')
        print(each_item)

print_lol(liste_films, 6)