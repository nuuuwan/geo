"""Utils for accessing geo data."""

import os
import ssl
import geopandas

from shapely.geometry import mapping, Point, shape, Polygon

from utils.cache import cache

from gig.ent_types import get_entity_type, ENTITY_TYPE

CACHE_NAME = 'geo.20210513'

# pylint: disable=W0212
ssl._create_default_https_context = ssl._create_unverified_context


def get_all_geodata(sub_region_type):
    """Get geo data for entire country."""
    return geopandas.read_file(
        os.path.join(
            'https://raw.githubusercontent.com',
            'nuuuwan/geo-data/master',
            '%s.json' % (sub_region_type),
        ),
    )


def get_region_geodata(region_id, sub_region_type):
    """Get geo data for region."""
    geodata = get_all_geodata(sub_region_type)
    return geodata[geodata['id'].str.slice(stop=len(region_id)) == region_id]


@cache(CACHE_NAME)
def _get_region_to_geo(region_type):
    """Get region to geo index."""
    geo_data = get_all_geodata(region_type)
    n_regions = len(geo_data['geometry'])
    print(n_regions)
    region_to_geo = {}
    for i in range(0, n_regions):
        region_id = geo_data['id'][i]
        region_to_geo[region_id] = mapping(geo_data['geometry'][i])
    return region_to_geo


@cache(CACHE_NAME)
def get_region_geo(region_id):
    """Get geo of region."""
    region_type = get_entity_type(region_id)
    region_to_geo = _get_region_to_geo(region_type)
    return region_to_geo.get(region_id, {})


@cache(CACHE_NAME)
def _get_latlng_region(lat_lng, region_type, parent_region_id=None):
    """Find the region which a given location is located in."""
    lat, lng = lat_lng
    point = Point(lng, lat)  # Note: Direction change!

    region_to_geo = _get_region_to_geo(region_type)
    for region_id in region_to_geo:
        if parent_region_id and (parent_region_id not in region_id):
            continue
        geo = region_to_geo[region_id]

        polygon_or_multi_polygon = shape(geo)

        if isinstance(polygon_or_multi_polygon, Polygon):
            if polygon_or_multi_polygon.contains(point):
                return region_id
        else:
            for polygon in polygon_or_multi_polygon:
                if polygon.contains(point):
                    return region_id
    return None


def get_latlng_regions(lat_lng):
    """Find the regions (province, district, dsd and gnd) which a given
        location is located in.
    """
    region_map = {}
    parent_region_id = ''
    for region_type in [
        ENTITY_TYPE.PROVINCE,
        ENTITY_TYPE.DISTRICT,
        ENTITY_TYPE.DSD,
        ENTITY_TYPE.GND,
    ]:
        region_id = _get_latlng_region(lat_lng, region_type, parent_region_id)
        if not region_id:
            break
        region_map[region_type] = region_id
        parent_region_id = region_id
    return region_map
