# -*- coding: UTF-8 -*-

# fichier : 19-calcul_vitesse.py
# auteur : David GILLARD


""" Affecter les variables temps et distance par les valeurs 6.892 s et 19.7 m.

Calculer et afficher la valeur de la vitesse ( 𝑣𝑖𝑡𝑒𝑠𝑠𝑒=𝑑𝑖𝑠𝑡𝑎𝑛𝑐𝑒/𝑡𝑒𝑚𝑝𝑠 ).

Améliorer l’affichage en imposant un chiffre après le point décimal, sans oublier l'unité ! 
 """

temps = 6.892
distance = 19.7
vitesse = distance / temps
print("La vitesse est de : {:.1f}".format(vitesse), "m/s")

