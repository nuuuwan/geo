"""Tests."""

import unittest
from geo import alt


class TestAltitude(unittest.TestCase):
    """Tests."""''

    def test_get_altitude(self):
        """Test."""
        for [lat, lng, expected_altitude] in [
            [7.0008, 80.7733, 2504],
            [6.8096, 80.4994, 2161],
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
