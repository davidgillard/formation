# -*- coding: UTF-8 -*-

# fichier : 04-traitement_chaine.py
# auteur : David GILLARD

""" A partir d'une variable s contenant "Dark side of the moon", écrire l'expression 
permettant, à partir de cette variable, de construire cette même chaine avec la première
lettre de chaque mot en majuscules, encadré de caractères =, l'ensemble sur une largeur 
de 60 caractères :
========================Dark Side Of The Moon========================

"""

s = "Dark side of the moon"
print("[{:=^60}]".format(s.title()))


