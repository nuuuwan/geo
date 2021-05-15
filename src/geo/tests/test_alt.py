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
