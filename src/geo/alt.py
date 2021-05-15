"""Utils for altutude information."""
import os
from utils import www
from utils.cache import cache

DIM = 1201

CACHE_NAME = 'geo.alt'


@cache(CACHE_NAME)
def _load_altitude_data(min_lat_lng):
    """Load altitude data."""
    min_lat, min_lng = min_lat_lng

    url = os.path.join(
        'https://raw.githubusercontent.com/nuuuwan',
        'geo_data_altitude/master',
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
