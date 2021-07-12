import unittest
import cites_funcions


class TestNameCity(unittest.TestCase):
    def test_city_country(self):
        check = cites_funcions.city('santiago', 'chile')
        self.assertEqual(check, 'Santiago, Chile')

    def test_city_country_pop(self):
        check = cites_funcions.city('santiago', 'chile', 'population = 5000000')
        self.assertEqual(check, 'Santiago, Chile - population = 5000000')


if __name__ == '__main__':
    unittest.main()