#!/usr/bin/python3
# -*- encoding: utf8 -*-

import csv
from collections import namedtuple
from pprint import pprint

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

# Ces deux lignes évitent des messages d'alerte concernant des fonctions de
# matplotlib en cours de dépréciation et encore utilisées par mpl_toolkit
# (à la date d'écriture du script) - vous pouvez les commenter pour voir ces 
# messages
import warnings
warnings.filterwarnings("ignore")

Ville = namedtuple("Ville", "nom lat lng nbhab surf dens")

print("===== Lecture des villes de France")
# Source: https://sql.sh/736-base-donnees-villes-francaises
lectcsv = csv.reader(open('villes_france.csv', encoding='utf8'))
villes = []         # Part d'une liste vide
nbtotvilles = 0     # Comptage nombre total de villes, pour info.
for items in lectcsv:
    nbtotvilles += 1
    # On filtre les départements hors France métropolitaine.
    # Certaines communes ont plusieurs codes-postaux, séparés par des
    # tirets dans le fichier.
    cp = items[8].split('-')    # => Codes postaux
    dept = int(cp[0][:2])       # (département à partir du 1er code postal)
    if not 1 <= dept <= 95:
        continue    # Commune ignorée, passe à la suivante

    hab = int(items[16])        # => Population estimé, 2012
    # On filtre les communes dont la population est inconnue (nulle).
    if hab == 0:
        continue    # Commune ignorée, passe à la suivante

    n = items[5]                # => Nom de la commune
    surf = float(items[18])     # => Surface
    lat = float(items[20])      # => Latitude
    lng = float(items[19])     # => Longitude
    v = Ville(n, lat, lng, hab, surf, hab / surf)
    villes.append(v)    # Références ajoutées.

print("Nombre de villes considérées:", len(villes), "sur", nbtotvilles)
print("=== Villes par densité croissante")
villes.sort(key=lambda x: x.dens)   # Tri sur l'attribut dens des communes.
pprint(villes[:10])


# Choix de la projection, du centrage et de la mise à l'échelle.
carte = Basemap(projection='stere', lat_0=46.60611, lon_0=1.87528,
    resolution='l', llcrnrlon=-5, urcrnrlon=11, llcrnrlat=41, urcrnrlat=51)
# Tracé des lignes de cotes, pays. Couleur pour les continents/la mer.
carte.drawcoastlines(linewidth=0.25)
carte.drawcountries(linewidth=0.25)
carte.fillcontinents(color='#CAAF68', lake_color='#D3FFFF')
carte.drawmapboundary(fill_color='#D3FFFF')
# Lignes parallèles/méridiens tous les 2 degrés.
carte.drawmeridians(np.arange(0, 360, 2), linewidth=0.1)
carte.drawparallels(np.arange(-90, 90, 2), linewidth=0.1)
plt.title('Communes à faible densité de population')

for v in villes[:200]:
    # Passage de coordonnées lat/long en coordonnées sur le graphique.
    x, y = carte(v.lng, v.lat)
    carte.plot(x, y, marker='o', color='Red', markersize=3)

# Si on veut sauvegarder la figure… pour un livre par exemple…
plt.savefig("figure.png", dpi=300)
plt.show()
