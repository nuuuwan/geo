"""Tests."""

import unittest
from geo import alt

LAT_LNG_320 = 6.9189, 79.8592
ALT_320 = 100
LAT_LNG_PIDURUTALAGALA = 7.0008, 80.7733
ALT_PIDURUTALAGALA = 2504
LAT_LNG_SRI_PADA = 6.8096, 80.4994
ALT_SRI_PADA = 2161


class TestAltitude(unittest.TestCase):
    """Tests."""''

    def test_get_altitude(self):
        """Test."""
        for [[lat, lng], expected_altitude] in [
            [LAT_LNG_PIDURUTALAGALA, ALT_PIDURUTALAGALA],
            [LAT_LNG_SRI_PADA, ALT_SRI_PADA],
        ]:
            self.assertEqual(
                alt.get_altitude([lat, lng]),
                expected_altitude,
            )

    def test_get_horizon(self):
        """Test."""
        for [obj_height, expected_horizon] in [
            [0, 0],
            [1, 3570.1541983505417],
            [2, 5048.960685131149],
            [100, 35701.680632709715],
        ]:
            self.assertEqual(
                alt.get_horizon(obj_height),
                expected_horizon,
            )

    def test_get_observed_height_info(self):
        """Test."""
        self.assertEqual(
            alt.get_observed_height_info(
                LAT_LNG_320,
                ALT_320,
                LAT_LNG_SRI_PADA,
                ALT_SRI_PADA,
            ),
            {
                'base_height': 101.87622235835856,
                'd_sub_to_obj_km':  71.73658496419974,
                'obj_height': 2161,
                'observed_height': 2059.1237776416415,
                'alpha_deg': 99.68857445825606,
                'beta_deg': 1.6441640810614901,
            },
        )

        self.assertEqual(
            alt.get_observed_height_info(
                LAT_LNG_320,
                ALT_320,
                LAT_LNG_PIDURUTALAGALA,
                ALT_PIDURUTALAGALA,
            ),
            {
                'base_height': 337.980254238245,
                'd_sub_to_obj_km':  101.33624713939635,
                'obj_height': 2504,
                'observed_height': 2166.019745761755,
                'alpha_deg': 84.88017934540761,
                'beta_deg': 1.2244867811775353,
            },
        )
