"""Tests."""
import time
import random
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

    def test_get_latlng_region_perf(self):
        """Test."""
        t_calls = []
        n_calls = 10
        for _ in range(0, n_calls):
            latlng = [6 + random.random() * 3, 80.25 + 0.5 * random.random()]

            t_start = time.time()
            region = geodata.get_latlng_regions(latlng)
            t_calls.append(time.time() - t_start)

            self.assertTrue('province' in region, [latlng, region])

        self.assertTrue(max(t_calls) < 0.1, t_calls)
