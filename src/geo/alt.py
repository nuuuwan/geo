"""Utils for altutude information."""
import math
import os

from utils import www
from utils.cache import cache
from utils.geo import EARTH_RADIUS as EARTH_RADIUS_KM
from utils.geo import get_distance

DIM = 1201
CACHE_NAME = 'geo.alt'


@cache(CACHE_NAME)
def _load_altitude_data(min_lat_lng):
    """Load altitude data."""
    min_lat, min_lng = min_lat_lng

    url = os.path.join(
        'https://raw.githubusercontent.com/nuuuwan',
        'geo_data_altitude/main',
        '%02d.%02d.json' % (min_lat, min_lng),
    )
    data = www.read_json(url)
    return data['matrix']


@cache(CACHE_NAME)
def get_altitude(lat_lng):
    """Get altitude for lat lng."""
    lat, lng = lat_lng
    min_lat, min_lng = (int)(lat), (int)(lng)
    data = _load_altitude_data([min_lat, min_lng])

    i_x = (int)((lng - min_lng) * DIM)
    i_y = (int)((lat - min_lat) * DIM)

    return data[i_x][i_y]


def get_horizon(sub_height):
    """Get horizon distance."""
    return math.sqrt(2 * EARTH_RADIUS_KM * 1000 * sub_height + sub_height ** 2)


def _get_sub_height_from_horizon(horizon):
    """Get subject height from horizon."""
    return (horizon ** 2) / (2 * EARTH_RADIUS_KM * 1000)


def get_observed_height_info(
    sub_lat_lng,
    sub_height,
    obj_lat_lng,
    obj_height,
):
    """Get observed height and related information."""
    d_sub_to_obj = get_distance(sub_lat_lng, obj_lat_lng) * 1000
    horizon_sub = get_horizon(sub_height)
    horizon_base = d_sub_to_obj - horizon_sub
    base_height = _get_sub_height_from_horizon(horizon_base)
    observed_height = obj_height - base_height

    sub_lat, sub_lng = sub_lat_lng
    obj_lat, obj_lng = obj_lat_lng
    dlat, dlng = obj_lat - sub_lat, obj_lng - sub_lng
    return {
        'observed_height': observed_height,
        'obj_height': obj_height,
        'base_height': base_height,
        'd_sub_to_obj_km': d_sub_to_obj / 1000.0,
        'beta_deg': math.atan2(observed_height, d_sub_to_obj) * 180 / math.pi,
        'alpha_deg': 90 - math.atan2(dlat, dlng) * 180 / math.pi,
    }
