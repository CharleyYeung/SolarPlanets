from utils import f_to_c

planet_dict = {
    "Mercury": {
        "mass_10_24kg": 0.330,
        "distance_from_sun_10_6_km": 57.9,
        "rotation_period_hours": 1407.6,
        "orbital_period_days": 88.0,
        "number_of_moons": 0,
        "diameter": 4879.4,
        "temperature": 333
    },
    "Venus": {
        "mass_10_24kg": 4.87,
        "distance_from_sun_10_6_km": 108.2,
        "rotation_period_hours": -5832.5,
        "orbital_period_days": 224.7,
        "number_of_moons": 0,
        "diameter": 12104,
        "temperature": 867
    },
    "Earth": {
        "mass_10_24kg": 5.97,
        "distance_from_sun_10_6_km": 149.6,
        "rotation_period_hours": 23.9,
        "orbital_period_days": 365.2,
        "number_of_moons": 1,
        "diameter": 12756,
        "temperature": 59
    },
    "Mars": {
        "mass_10_24kg": 0.642,
        "distance_from_sun_10_6_km": 228.0,
        "rotation_period_hours": 24.6,
        "orbital_period_days": 687.0,
        "number_of_moons": 2,
        "diameter": 6779,
        "temperature": -85
    },
    "Jupiter": {
        "mass_10_24kg": 1898,
        "distance_from_sun_10_6_km": 778.5,
        "rotation_period_hours": 9.9,
        "orbital_period_days": 4331,
        "number_of_moons": 95,
        "diameter": 139820,
        "temperature": -166
    },
    "Saturn": {
        "mass_10_24kg": 568,
        "distance_from_sun_10_6_km": 1432.0,
        "rotation_period_hours": 10.7,
        "orbital_period_days": 10747,
        "number_of_moons": 274,
        "diameter": 116460,
        "temperature": -220
    },
    "Uranus": {
        "mass_10_24kg": 86.8,
        "distance_from_sun_10_6_km": 2867.0,
        "rotation_period_hours": -17.2, 
        "orbital_period_days": 30589,
        "number_of_moons": 28,
        "diameter": 50724,
        "temperature": -195
    },
    "Neptune": {
        "mass_10_24kg": 102,
        "distance_from_sun_10_6_km": 4515.0,
        "rotation_period_hours": 16.1,
        "orbital_period_days": 59800,
        "number_of_moons": 16,
        "diameter": 49244,
        "temperature": -330
    }
}

class Planet:
    def __init__(self, name):
        data = planet_dict.get(name)
        if not data:
            raise ValueError(f"Planet {name} not found")
        self.data = data
        self.name = name
        self.mass = data["mass_10_24kg"]
        self.distance = data["distance_from_sun_10_6_km"]
        self.rotation = data["rotation_period_hours"]
        self.orbit = data["orbital_period_days"]
        self.moons = data["number_of_moons"]
        self.diameter = data["diameter"]
        self.temperature = data["temperature"]

    def everything(self):
        return (
            f"Planet Name: {self.name}\n"
            f"Planet Mass(10²⁴ kg): {self.mass}\n"
            f"Planet Diameter(km): {self.diameter}\n"
            f"Distance from the Sun(10⁶ km): {self.distance}\n"
            f"Hours per rotation: {self.rotation}\n"
            f"Days per orbit: {self.orbit}\n"
            f"Number of Moons: {self.moons}\n"
            f"Surface Temperature: {self.temperature}°F ({f_to_c(self.temperature)}°C)"
        )

    def get_mass(self):
        return f"Planet Mass: {self.mass} ×10²⁴ kg.\n"

    def get_distance(self):
        return f"Distance from the Sun: {self.distance} ×10⁶ km.\n"

    def get_rotation(self):
        return f"It takes {self.rotation} hours to rotate.\n"

    def get_orbit(self):
        return f"It takes {self.orbit} days to move around the sun.\n"

    def get_moon(self):
        return "It has one moon.\n" if self.moons == 1 else f"It has {self.moons} moons.\n"

    def get_diameter(self):
        return f"The diameter: {self.diameter} km.\n"

    def get_temperature(self):
        return f"Surface Temperature: {self.temperature}°F ({f_to_c(self.temperature)}°C)"



def main():
    pass


if __name__ == "__main__":
    main()
