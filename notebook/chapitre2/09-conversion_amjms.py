# -*- coding: UTF-8 -*-

# fichier : 09-conversion_amjms.py
# auteur : David GILLARD


""" Écrire un script qui convertit un (grand) nombre entier de secondes en un nombre d'années,
de mois, de jours, d'heures, de minutes et de secondes. Pour cet exercice, on considérera 
que tous les mois ont 30 jours et qu'une année comporte 365 jours.

Effectuez le calcul pour  10^8  secondes." """

nombre_seconde = 1000000000 # nombre de secondes initié dans le programme

nombre_seconde_par_jour = 3600 * 24 # nombre de seconde dans une journée
print("{:.2f}".format(nombre_seconde_par_jour), "secondes par jour")
nombre_seconde_par_an = nombre_seconde_par_jour * 365 # ici on simplifie en considérant que le nombre de jours dans l'année est toujours de 365
print("{:.2f}".format(nombre_seconde_par_an), "secondes par an")
nombre_seconde_par_mois = nombre_seconde_par_jour * 30 # ici on considere qu'un mois est toujours de 30 jours
print("{:.2f}".format(nombre_seconde_par_mois), "secondes par mois")

nombre_annee = nombre_seconde // nombre_seconde_par_an
print("{:.2f}".format(nombre_annee), "année") # représentation de la valeur de secondes en années
nombre_seconde_restante = nombre_seconde % nombre_seconde_par_an
print("{:.2f}".format(nombre_seconde_restante), "secondes restantes") # nombre de seconde 

nombre_mois = nombre_seconde // nombre_seconde_par_mois
print("{:.2f}".format(nombre_mois), "mois")
nombre_seconde_restante = nombre_seconde % nombre_seconde_par_mois
print("{:.2f}".format(nombre_seconde_restante), "secondes restantes")

nombre_jours = nombre_seconde // nombre_seconde_par_jour
print("{:.2f}".format(nombre_jours), "jours")
nombre_seconde_restante = nombre_seconde % nombre_seconde_par_jour
print("{:.2f}".format(nombre_seconde_restante), "secondes restantes")

nombre_heures = nombre_seconde_restante // 3600
print("{:.2f}".format(nombre_jours), "heures")
nombre_seconde_restante = nombre_seconde_restante % 3600
print("{:.2f}".format(nombre_seconde_restante), "secondes restantes")

nombres_minutes = nombre_seconde_restante // 60
print("{:.2f}".format(nombre_jours), "minutes")
nombre_seconde_restante = nombre_seconde_restante % 60
print("{:.2f}".format(nombre_seconde_restante), "secondes restantes")


print("Nombre de secondes à convertir :", nombre_seconde) 
print("Cette durée correspond à", nombre_annee, "années de 365 jours, plus") 
print(nombre_mois, "mois de 30 jours,", end=' ') 
print(nombre_jours, "jours,", end=' ') 
print(nombre_heures, "heures,", end=' ') 
print(nombres_minutes, "minutes et", end=' ') 
print(nombre_seconde_restante, "secondes.")