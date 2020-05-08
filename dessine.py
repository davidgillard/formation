#!/usr/bin/python3
#-*- encoding utf8 -*-

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.filterwarnings("ignore")

carte = Basemap(projection='stere', lat_0=46.60611, lon_0=1.87528, resolution='l', llcrnrlon=-5, urnrnrlon=11, urcrnrlat=51)
carte.drawcoastlines(linewidth=0.25)
carte.drawcountries(linewidth=0.25)
carte.fillcontinents(color='#CAAF68', lake_color='#D3FFFF')
carte.drawmapboundary(fill_color='#D3FFFF')
carte.drawmeridians(np.arange(0, 360, 2), linewidth=0.1)
carte.drawparallels(np.arange(-90, 90, 2), linewidth=0.1)
plt.title('Communes à faible densité de population')

for v in villes[:200]:
    x, y = map(v.lng, v.lat)
    map.plot(x, y, marker='o', color='Red', markersize=3)

plt.savefig("figure.png", dpi=300)
plt.show()