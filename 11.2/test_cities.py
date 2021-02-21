import unittest
from city_functions import where_do_you_live


class CityFunctionsCase(unittest.TestCase):
    """This class for testing functions from 'city_functions.py'."""

    def test_city_country(self):
        """Testing correct result => 'United States, Texas - population 1_000_000'"""

        place = where_do_you_live('united states', 'texas')
        self.assertEqual(place, 'United States, Texas - population 1000000')

    def test_city_country_population(self):
        """Testing correct result => 'Russia, Moscow - population 13_000_000'"""

        place = where_do_you_live('russia', 'moscow', 13_000_000)
        self.assertEqual(place, 'Russia, Moscow - population 13000000')