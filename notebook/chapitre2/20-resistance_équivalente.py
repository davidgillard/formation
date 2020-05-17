# -*- coding: UTF-8 -*-

# fichier : 20-resistance_équivalente.py
# auteur : David GILLARD


""" En électronique, les résistances sont des composants très fréquents.
Les résistances peuvent être associées en série ou en parallèle. Dans les deux cas, on veut 
calculer la résistance équivalente du montage.

Sachant que :

la résistance équivalente 𝑅𝑒𝑞 de deux résistance 𝑅1 et 𝑅2 en série est : 𝑅𝑒𝑞=𝑅1+𝑅2  ;
la résistance équivalente 𝑅𝑒𝑞 de deux résistance 𝑅1 et 𝑅2 en parallèle est telle que :

1/𝑅𝑒𝑞 = (1/𝑅1)+(1/𝑅2).

Afficher la résistance équivalente de deux résistance de 100 ohms.

Rappel : Pour additionner deux fractions, il faut les ramener au même dénominateur : 

𝑎/𝑏+𝑐/𝑑=𝑎𝑑/𝑏𝑑+𝑏𝑐/𝑏𝑑=𝑎𝑑+𝑏𝑐/𝑏𝑑  """

R1 = 10
R2 = 30
Req_serie = R1 + R2
Req_parallele = (R1*R2) / (R1+R2)

print(f"La résitance équivalente pour un montage en serie pour les valeurs de R1: {R1} et R2: {R2} est de {Req_serie} ohms")
print(f"La résitance équivalente pour un montage en parallele pour les valeurs de R1: {R1} et R2: {R2} est de {Req_parallele} ohms")
