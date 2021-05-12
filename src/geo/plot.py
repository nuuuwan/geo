"""Geo utils."""

import os
import geopandas
import matplotlib.pyplot as plt

VERSION = '2021-05-07'


def get_all_geodata(sub_region_type):
    """Get geo data for entire country."""
    return geopandas.read_file(os.path.join(
        '/Users/nuwan.senaratna/Not.Dropbox/DEV/GITHUB_MIRROR/sl-topojson',
        '%s.%s.json' % (sub_region_type, VERSION),
    ))


def get_region_geodata(region_id, sub_region_type):
    """Get geo data for region."""
    geodata = get_all_geodata(sub_region_type)
    n = len(region_id)
    return geodata[geodata['id'].str.slice(stop=n) == region_id]


def plot_geodata(
    geodata,
    title,
    sub_title,
    footer_text,
    region_to_color_map,
):
    """Plot region_id."""
    plt.rc('font', family='Futura')

    fig, ax = plt.subplots()
    geodata.plot(
        ax=ax,
        label='name',
        color=geodata['id'].map(region_to_color_map),
    )

    # sub-region labels
    n = len(geodata)
    if n < 30:
        geodata['center'] = geodata['geometry'].centroid
        geodata_copy = geodata.copy()
        geodata_copy.set_geometry("center", inplace=True)
        texts = []
        for x, y, label in zip(
            geodata_copy.geometry.x,
            geodata_copy.geometry.y,
            geodata_copy['name'],
        ):
            if label == '[unknown]':
                continue
            texts.append(plt.text(
                x,
                y,
                label,
                fontsize=5,
                horizontalalignment='center',
            ))

    BASE_FONT_SIZE = 16

    def draw_text(x, y, text, p_font_size=1):
        fig.text(
            x=x,
            y=y,
            s=text,
            fontsize=BASE_FONT_SIZE * p_font_size,
            horizontalalignment='center',
        )

    draw_text(0.5, 0.94, title, 1)
    draw_text(0.5, 0.90, sub_title, 0.75)
    draw_text(0.5, 0.06, footer_text, 0.5)

    plt.axis('off')
    plt.show()


if __name__ == '__main__':
    import gig.attrs
    entity_type = 'gnd'
    region_geodata = get_region_geodata('LK', entity_type)
    ethnicity_data = gig.attrs.get_table_data(
        'census',
        'ethnicity_of_population',
        entity_type=entity_type,
    )
    region_to_color_map = {}
    entity_ids = list(region_geodata['id'])
    for entity_id in entity_ids:
        if entity_id not in ethnicity_data:
            color = 'black'
        else:
            d = ethnicity_data[entity_id]
            sinhalese = d['sinhalese']
            tamil = d['sri_lankan_tamil'] + d['indian_tamil']
            moor = d['moor'] + d['malay']

            total_population = d['total_population']
            p_sinhalese = sinhalese / total_population

            if sinhalese > total_population * 0.9:
                color = 'red'
            elif tamil > total_population * 0.9:
                color = 'orange'
            elif moor > total_population * 0.9:
                color = 'green'
            else:
                color = 'gray'

        region_to_color_map[entity_id] = color

    region_geodata = get_region_geodata('LK', entity_type)
    plot_geodata(
        region_geodata,
        'Sri Lanka',
        'With %s Boundaries' % entity_type,
        'Source: http://www.statistics.gov.lk/',
        region_to_color_map=region_to_color_map,
    )

    # region_geodata = get_region_geodata('LK-11', 'dsd')
    # plot_geodata(region_geodata, 'Colombo District with DSD Boundaries')

    # region_geodata = get_region_geodata('LK-1127', 'gnd')
    # plot_geodata(region_geodata, 'Thimbirigasyaya with GND Boundaries')
