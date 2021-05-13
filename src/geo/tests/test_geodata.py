"""Tests."""

import unittest
import geopandas
from geo import geodata


class TestGeoData(unittest.TestCase):
    """Tests."""''

    def test_get_all_geodata(self):
        """Test."""
        geo_data = geodata.get_all_geodata('province')
        self.assertTrue(isinstance(
            geo_data,
            geopandas.geodataframe.GeoDataFrame,
        ))

    def test_get_region_geodata(self):
        """Test."""
        geo_data = geodata.get_region_geodata('LK', 'province')
        self.assertTrue(isinstance(
            geo_data,
            geopandas.geodataframe.GeoDataFrame,
        ))

    def test_get_region_geo(self):
        """Test."""
        geo = geodata.get_region_geo('LK-11')
        self.assertEqual(
            geo['type'],
            'MultiPolygon',
        )

    def test_get_latlng_region(self):
        """Test."""
        latlng = [6.9157, 79.8636]
        self.assertEqual(
            geodata.get_latlng_regions(latlng),
            {
                'province': 'LK-1',
                'district': 'LK-11',
                'dsd': 'LK-1127',
            },
        )
