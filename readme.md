#  A Journey Through the Solar System — Powered by Python

##  Mission Log by Charley Yeung

This is the final assessment of the Module Fundamentals of Computing. In this assessment, students are required to write a Python programme to display information about the solar planets. Below is the briefing.

This project is the result of everything I’ve learned in my journey through Fundamentals of Computing. I wanted to create something more than just lines of code — a small universe where users could meet the planets, ask them questions, learn their stories, and maybe even count their moons.

To keep things neat and intelligent, I gave each planet its own digital passport, built using Python classes. Every Planet object carries its own profile, including:

- Name
- Mass (×10²⁴ kg)
- Distance from the Sun (×10⁶ km)
- Orbital period (in Earth days)
- Rotation period (in hours)
- Number of moons 
- Diameter
- Average temperature

This isn’t just about displaying data — it’s about making that data come alive. Through menus, prompts, and a simple but warm interface, the Solar System becomes a little more comprehensive.

Data was carefully sourced from NASA and Wikipedia to ensure accuracy. The interface was made more intuitive through a Tkinter GUI, where users could take a mini quiz and then explore planets using dropdown menus.

---

##  Unit Tests: Keeping My Starship Safe

Just like how engineers run checks before launching a rocket, I created a test plan using Python’s `unittest` framework. The test file is named `main_test.py`.

These tests made sure that:

- Planets can be created correctly with valid data.
- Key properties like mass, orbital period, and number of moons are stored correctly.
- Invalid planet names raise appropriate errors (e.g. `ValueError` if the planet doesn't exist in the data).
- The planetary data remained consistent across queries.

Here's a brief taste of what the test file looks like:

```python
import unittest
from planet import Planet

class TestPlanetData(unittest.TestCase):
    def test_create_planet_instance(self):
        earth = Planet("Earth")
        self.assertEqual(earth.mass, 5.97)
        self.assertEqual(earth.moons, 1)

    def test_invalid_planet(self):
        with self.assertRaises(ValueError):
            Planet("Sun")  

    def test_orbital_period(self):
        venus = Planet("Venus")
        self.assertAlmostEqual(venus.orbit, 224.7, places=1)

    def test_temperature_range(self):
        mars = Planet("Mars")
        self.assertLess(mars.temperature, 0)
```

This assignment was more than just coding. It was storytelling through data. With each line, I travelled to different planets, turning scientific facts into an interactive experience. 
