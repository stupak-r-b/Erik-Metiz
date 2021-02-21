import unittest
from city_functions import where_do_you_live


class CityFunctionsCase(unittest.TestCase):
    """This class for testing functions from 'city_functions.py'."""

    def test_city_country(self):
        """Testing correct result => 'United States, Texas'"""

        place = where_do_you_live('united states', 'texas')
        self.assertEqual(place, 'United States, Texas')