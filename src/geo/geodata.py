"""Utils for accessing geo data."""

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
