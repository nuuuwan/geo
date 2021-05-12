"""Tests."""

import unittest
import geopandas
from geo import geodata


class TestGeoData(unittest.TestCase):
    """Tests."""

    def test_get_region_geodata(self):
        """Test."""
        gd = geodata.get_region_geodata('LK', 'province')
        self.assertTrue(isinstance(
            gd,
            geopandas.geodataframe.GeoDataFrame,
        ))
