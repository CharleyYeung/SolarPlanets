import unittest
from planet import planet_dict, Planet

class TestPlanetData(unittest.TestCase):

    def test_planet_dict_has_earth(self):
        self.assertIn("Earth", planet_dict)
        self.assertEqual(planet_dict["Earth"]["number_of_moons"], 1)

    def test_create_planet_instance(self):
        earth = Planet("Earth") 
        self.assertEqual(earth.name, "Earth")
        self.assertEqual(earth.data["mass_10_24kg"], 5.97)
        self.assertEqual(earth.data["number_of_moons"], 1)

    def test_planet_fields_consistency(self):
        for name, data in planet_dict.items():
            with self.subTest(planet=name):
                self.assertIn("mass_10_24kg", data)
                self.assertIn("distance_from_sun_10_6_km", data)
                self.assertIn("number_of_moons", data)
                self.assertIsInstance(data["number_of_moons"], int)


class TestPlutoPresence(unittest.TestCase):
    def test_pluto_not_in_planet_dict(self):
        self.assertNotIn("Pluto", planet_dict)


if __name__ == "__main__":
    unittest.main()
