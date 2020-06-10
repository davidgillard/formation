# -*- coding: UTF-8 -*-

# fichier : 16-notes_eleves.py
# auteur : David GILLARD

""" 
Écrire une boucle qui demande à l'utilisateur d'entrer des notes d'élèves. La boucle se 
terminera quand la saisie sera négative.

Avec les notes ainsi entrées, construire progressivement une liste. Après chaque entrée 
d'une nouvelle note (et donc à chaque itération de la boucle), afficher la moyenne de toutes 
les notes déjà disponibles.
"""

notes = []
saisie = 0
moy = 0.0
somme = 0
while saisie >=0:
    notes = float(input("Veuillez saisir les notes pour arreter saisie une note négative :"))
    if saisie < 0:
        print("\nMoyenne finale = %.2f pour %d notes" % (moy, len(notes)))
    else:
        notes.append(saisie)
        somme += saisie
        nombre_note = len(notes)
        moy = somme / nombre_note
        print(f"La moyenne est de {moy}") 