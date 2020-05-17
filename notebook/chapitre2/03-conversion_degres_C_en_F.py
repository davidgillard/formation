# -*- coding: UTF-8 -*-

# fichier : conversion_degres_C_en_F.py
# auteur : David GILLARD 

"""Instruction: Saisir une température en degrés Celsius ( 𝑇𝐶 ), puis la convertir en degré Fahrenheit ( 𝑇𝐹 ). Faire également la conversion inverse.
On donne :  𝑇𝐹=1,8×𝑇𝐶+32 
Afficher une valeur approchée, avec deux décimales, de 20 °F exprimés en °C.

infomation utile : FORMULE POUR CONVERTIR LES DEGRÉS CELSIUS ET FAHRENHEIT
Convertir les Celsius en Fahrenheit en appliquant la formule suivante: Celsius * 9/5 + 32.

Pour convertir des Fahrenheit en Celsius il suffit de faire: (Fahrenheit - 32) * 5/9;

Afficher une valeur approchée, avec deux décimales, de 20 °F exprimés en °C. """

T_C = 60 # initialisation de la température en degrés
print("Conversion de degrés celsius en degrés Fahrenheit")
print("pour une température de", T_C, "degrés celsius")
print("{}".format("#"*23))
T_F = T_C * 9/5 + 32
print("{:.2f}".format(T_F), "degrés fahrenheit")
print("{:#^26}".format(" conversion inverse "))
T_C = (T_F - 32)*5/9
print("{:.2f}".format(T_C), "degrés celsius")