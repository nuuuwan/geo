"""Utils for accessing geo data."""

import os
import geopandas

from utils import www


def get_all_geodata(sub_region_type):
    """Get geo data for entire country."""
    url = os.path.join(
        'https://raw.githubusercontent.com',
        'nuuuwan/geo-data/master',
        '%s.json' % (sub_region_type),
    )
    return www.read_json(url)


def get_region_geodata(region_id, sub_region_type):
    """Get geo data for region."""
    geodata = get_all_geodata(sub_region_type)
    return geodata[geodata['id'].str.slice(stop=len(region_id)) == region_id]
