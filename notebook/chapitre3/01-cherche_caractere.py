# -*- coding: UTF-8 -*-

# fichier : 01-cherche_caractere.py
# auteur : David GILLARD


""" Écrire un script qui détermine si une chaîne contient ou non le caractère "e". 
Affichez son nombre d'occurrences.

Utilisez une boucle while.  """

index = 0 # Initialisation de mon itérable
chaine = "Que vous etes joli! Que vous me semblez beau!" # ici la chaine qui va être parcouru à la recherche de e
#len(chaine) retourne la taille de la chaine de caractére
nombre_caractere = 0

while index < len(chaine):
    contenu_chaine = chaine[index]
    print(contenu_chaine)
    index = index + 1
if contenu_chaine not in 'e':
    nombre_caractere = chaine.count("e")
    print(f"La lettre e est contenu {nombre_caractere} fois dans la chaine suivante: {chaine}")
else:
    print("La chaine ne contient pas le caractére e")