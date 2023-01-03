from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.successful_missions = 0
        self.not_completed_missions = 0

    def __check_if_astronaut_exists(self, name):
        for astronaut in self.astronaut_repository.astronauts:
            if astronaut.name == name:
                return True

    def __check_if_planet_exists(self, name):
        for planet in self.planet_repository.planets:
            if planet.name == name:
                return True

    def __get_astronaut_by_name(self, name):
        for astronaut in self.astronaut_repository.astronauts:
            if astronaut.name == name:
                return astronaut

    def __get_planet_by_name(self, name):
        for planet in self.planet_repository.planets:
            if planet.name == name:
                return planet

    def __sort_astronauts_with_enough_oxygen(self):
        MIN_OXYGEN_LEVEL = 30
        astronauts_list = []

        astronauts_list = [a for a in self.astronaut_repository.astronauts if a.oxygen > MIN_OXYGEN_LEVEL]
        astronauts_list = sorted(astronauts_list, key=lambda x: -x.oxygen)

        return astronauts_list

    def add_astronaut(self, astronaut_type: str, name: str):
        if self.__check_if_astronaut_exists(name):
            return f"{name} is already added."

        if astronaut_type not in ["Biologist", "Geodesist", "Meteorologist"]:
            raise Exception("Astronaut type is not valid!")

        if astronaut_type == 'Biologist':
            new_astronaut = Biologist(name)
        elif astronaut_type == 'Geodesist':
            new_astronaut = Geodesist(name)
        else:
            new_astronaut = Meteorologist(name)
        self.astronaut_repository.astronauts.append(new_astronaut)

        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        if self.__check_if_planet_exists(name):
            return f"{name} is already added."

        new_planet = Planet(name)
        new_planet.items.extend(items.split(', '))
        self.planet_repository.planets.append(new_planet)

        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        if not self.__check_if_astronaut_exists(name):
            raise Exception(f"Astronaut {name} doesn't exist!")

        astronaut = self.__get_astronaut_by_name(name)
        self.astronaut_repository.astronauts.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        AMOUNT = 10

        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(AMOUNT)

    def send_on_mission(self, planet_name: str):
        if not self.__check_if_planet_exists(planet_name):
            raise Exception("Invalid planet name!")

        planet = self.__get_planet_by_name(planet_name)
        astronauts_list = self.__sort_astronauts_with_enough_oxygen()

        if not astronauts_list:
            self.not_completed_missions += 1
            raise Exception("You need at least one astronaut to explore the planet!")

        number_of_astronauts_used = 1

        for astronaut in astronauts_list[:5]:
            while True:
                if astronaut.oxygen <= 0 or not planet.items:
                    break
                astronaut.backpack.append(planet.items.pop())
                astronaut.breathe()
                if astronaut.oxygen <= 0:
                    number_of_astronauts_used += 1
                    astronaut.oxygen = 0

        if planet.items:
            self.not_completed_missions += 1
            return 'Mission is not completed.'

        self.successful_missions += 1
        return f"Planet: {planet.name} was explored. {number_of_astronauts_used} " \
               f"astronauts participated in collecting items."

    def report(self):
        output = [f"{self.successful_missions} successful missions!",
                  f"{self.not_completed_missions} missions were not completed!",
                  "Astronauts' info:"
                  ]

        for astronaut in self.astronaut_repository.astronauts:
            output.append(str(astronaut))

        return '\n'.join(output)





