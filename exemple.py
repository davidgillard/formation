#!/usr/bin/python3
#-*- encoding utf8 -*-

import csv
from collections import namedtuple
from pprint import pprint

Ville = namedtuple("Ville", "nom lat lng nbhab surf dens")

print("============= Lecture des villes de France")
lectcsv = csv.reader(open('villes_france.csv', encoding='utf8'))
villes = []
nbtotvilles = 0
for items in lectcsv:
    nbtotvilles += 1 
    cp = items[8].split('-')
    print(items[8]) # Affiche moi les codes postaux
    dept = int(cp[0][:2])
    print("##########################")
    print(dept) # Affiche moi que les deux caractéres des cp pour avoir les depts
    if not 1 <= dept <= 95:
        continue

    hab = int(items[16])
    print("°°°°°°°°°°°°°°°°°°°°°°°")
    print("Nobres d'habitant: ", hab)
    if hab == 0:
        continue

    n = items[5]
    surf = float(items[18])
    lat = float(items[20])
    lng = float(items[19])
    v = Ville(n, lat, lng, hab, surf, hab / surf)
    villes.append(v)

print("Nombres de villes considérées:", len(villes), "sur", nbtotvilles) 
print("Villes par densité croissante:",)
villes.sort(key=lambda x: x.dens)
pprint(villes[:10])