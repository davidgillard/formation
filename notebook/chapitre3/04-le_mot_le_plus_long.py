# -*- coding: UTF-8 -*-

# fichier : 04-le_mot_le_plus_long.py
# auteur : David GILLARD


""" Saisir une phrase (par exemple cet énoncé) et afficher le mot le plus long 
qu'elle contient.
"""

phrase = "Saisir une phrase (par exemple cet énoncé) et afficher le mot le plus long qu'elle contient"
tmp = ""
for mots in phrase:
    if mots.isalpha() or mots == " ": # on s'affranchit des caractéres non alphanumerique
        tmp += mots

print(f"Le mot le plus long dans la phrase est:", max(tmp.split(' ')[::-1], key=len))