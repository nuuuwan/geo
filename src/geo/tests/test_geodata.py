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
        self.assertEqual(geo['type'], 'MultiPolygon')

    def test_get_latlng_region(self):
        """Test."""
        for [latlng, expected_regions] in [
            [
                [6.9157, 79.8636],
                {
                    'province': 'LK-1',
                    'district': 'LK-11',
                    'dsd': 'LK-1127',
                    'gnd': 'LK-1127015',
                },
            ],
            [
                [9.6615, 80.0255],
                {
                    'province': 'LK-4',
                    'district': 'LK-41',
                    'dsd': 'LK-4136',
                    'gnd': 'LK-4136080',
                },
            ],
        ]:
            self.assertEqual(
                geodata.get_latlng_regions(latlng),
                expected_regions,
            )
