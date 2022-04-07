"""Utils for accessing geo data."""

import os
import ssl

import geopandas
from gig.ent_types import ENTITY_TYPE, get_entity_type
from shapely.geometry import Point, mapping, shape
from utils.cache import cache
from utils.timex import SECONDS_IN

CACHE_NAME = 'geo'

# pylint: disable=W0212
ssl._create_default_https_context = ssl._create_unverified_context


@cache(CACHE_NAME, SECONDS_IN.YEAR)
def get_all_geodata(region_type):
    """Get Geo/TopoJSON data for entire country by region type.
    Args:
        region_type (str): Region Type ('province', 'district' etc)

    Returns:
        Geo-spatial data as GeoPandasFrame

    """

    file_ext = 'topojson'
    return geopandas.read_file(
        os.path.join(
            'https://raw.githubusercontent.com',
            'nuuuwan/geo-data/main',
            '%s.%s' % (region_type, file_ext),
        ),
    )


@cache(CACHE_NAME, SECONDS_IN.YEAR)
def get_region_geodata(region_id, sub_region_type):
    """Get Geo/TopoJSON data for a particular region, by sub_region_type.

    Args:
        region_id (str): Region ID (e.g. LK-1, LK-23)
        region_type (str): Region Type ('province', 'district' etc)

    Returns:
        Geo-spatial data as GeoPandasFrame

    """
    geodata = get_all_geodata(sub_region_type)
    if region_id == 'LK':
        return geodata
    return geodata[geodata['id'].str.slice(stop=len(region_id)) == region_id]


@cache(CACHE_NAME, SECONDS_IN.YEAR)
def _get_region_to_geo(region_type):
    """Get region to geo index."""
    geo_data = get_all_geodata(region_type)
    n_regions = len(geo_data['geometry'])
    region_to_geo = {}
    for i in range(0, n_regions):
        region_id = geo_data['id'][i]
        region_to_geo[region_id] = mapping(geo_data['geometry'][i])
    return region_to_geo


@cache(CACHE_NAME, SECONDS_IN.YEAR)
def get_region_geo(region_id):
    """Get Geo/TopoJSON of a region.

    Args:
        region_id (str): Region ID (e.g. LK-1, LK-23)

    Returns:
        Geo-spatial data as GeoPandasFrame

    """
    region_type = get_entity_type(region_id)
    region_to_geo = _get_region_to_geo(region_type)
    return region_to_geo.get(region_id, {})


@cache(CACHE_NAME, SECONDS_IN.YEAR)
def _get_latlng_region(lat_lng, region_type, parent_region_id=None):
    """Find the region which a given location is located in."""
    lat, lng = lat_lng
    point = Point(lng, lat)  # Note: Direction change!

    region_to_geo = _get_region_to_geo(region_type)
    for region_id in region_to_geo:
        if parent_region_id and (parent_region_id not in region_id):
            continue
        geo = region_to_geo[region_id]

        multi_polygon = shape(geo)
        for polygon in multi_polygon:
            if polygon.contains(point):
                return region_id

    return None


@cache(CACHE_NAME, SECONDS_IN.YEAR)
def get_latlng_regions(lat_lng):
    """Find the regions which a given location is located in.

    Args:
        lat_lng (pair of floats): Latitude and Longitude as pair of floats

    Returns:
        Map of region type to region ID

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
