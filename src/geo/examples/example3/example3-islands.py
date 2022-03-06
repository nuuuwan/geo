"""Example.

See https://en.wikipedia.org/wiki/List_of_islands_of_Sri_Lanka
"""

import math
import os

import geopandas
import matplotlib.pyplot as plt
from gig import ents
from utils import colorx

from geo import geodata
from geo.examples.example3.CENTROID_TO_INFO import (CENTROID_TO_INFO,
                                                    NOT_AN_ISLAND)

AREA_FACTOR = 65000 / 5.357395893586317
COLOR_OTHER = '#f0f0f0'
RESOLUTION_DPI = 1200
MIN_AREA, MAX_AREA = 0.1, 150
DO_DISPLAY_NON_ISLANDS = False
HA_IN_KM2 = 100


def render_district(district):
    district_id = district['id']
    district_name = district['name']
    print(f'# {district_id} ({district_name})')
    gpd_df0 = geodata.get_region_geodata(district_id, 'district')
    d0 = gpd_df0.to_dict()
    d0 = {
        'id': d0['id'],
        'geometry': d0['geometry'],
    }
    multipolygon = list(d0['geometry'].values())[0]
    d = {
        'id': [],
        'name': [],
        'geometry': [],
        'centroid': [],
        'color': [],
        'area': [],
    }

    n_islands = 0
    for i, polygon in enumerate(list(multipolygon)):
        area_est = polygon.area * AREA_FACTOR
        centroid = (round(polygon.centroid.y, 6), round(polygon.centroid.x, 6))
        area = None
        if MIN_AREA <= area_est <= MAX_AREA:
            info = CENTROID_TO_INFO.get(centroid, 'Unknown')
            if ' - ' in info:
                name, area = info.split(' - ')
                area = (float)(area)
            else:
                name = info

            if name == 'Unknown':
                print(centroid, ': \'Unknown\',')
                os.system('open -a firefox ' +
                          '"https://www.google.com/maps/search/%f+%f"' %
                          (centroid[0], centroid[1]))

            if name != NOT_AN_ISLAND:
                d['id'].append(i)
                d['name'].append(name)
                d['geometry'].append(polygon)
                d['centroid'].append(centroid)
                d['color'].append(colorx.random_hex())
                d['area'].append(area)
                n_islands += 1
                continue

        if DO_DISPLAY_NON_ISLANDS:
            d['id'].append(i)
            d['name'].append('')
            d['geometry'].append(polygon)
            d['centroid'].append(centroid)
            d['color'].append(COLOR_OTHER)
            d['area'].append(area)

    if n_islands == 0:
        print('No islands!')
        return None

    gpd_df = geopandas.GeoDataFrame(d)
    gpd_df.plot(color=gpd_df['color'])
    for idx, row in gpd_df.iterrows():
        name = row['name']
        if row['area'] and not math.isnan(row['area']):
            area = (float)(row['area'])
            if area < 1:
                label = f'{name} ({area * HA_IN_KM2:.0f}ha)'
            else:
                label = f'{name} ({area:.0f}km²)'
        else:
            label = f'{name}'

        plt.text(
            row['centroid'][1],
            row['centroid'][0],
            label,
            fontsize=4,
            ha='center',
        )
    plt.title(f'{district_name} District ({n_islands} islands)')
    image_file = f'{__file__}-{district_id}.png'
    plt.savefig(image_file, dpi=RESOLUTION_DPI)
    os.system(f'open -a firefox {image_file}')


if __name__ == '__main__':
    URL_ISLANDS = 'https://en.wikipedia.org/wiki/List_of_islands_of_Sri_Lanka'
    os.system(f'open -a firefox {URL_ISLANDS}')
    for district in ents.get_entities('district'):
        render_district(district)
