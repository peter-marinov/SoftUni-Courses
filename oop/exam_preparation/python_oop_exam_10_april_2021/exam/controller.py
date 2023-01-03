from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository
        self.aquariums: list = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        aquarium_mapper = {"FreshwaterAquarium": FreshwaterAquarium, "SaltwaterAquarium": SaltwaterAquarium}
        if aquarium_type not in aquarium_mapper:
            return "Invalid aquarium type."

        new_aquarium = aquarium_mapper[aquarium_type](aquarium_name)
        self.aquariums.append(new_aquarium)

        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        decoration_mapper = {"Ornament": Ornament, "Plant": Plant}
        if decoration_type not in decoration_mapper:
            return "Invalid decoration type."

        new_decoration = decoration_mapper[decoration_type]()
        self.decorations_repository.add(new_decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        decoration = self.decorations_repository.find_by_type(decoration_type)
        aquarium = self.__find_aquarium_by_name(aquarium_name)
        if decoration == 'None':
            return f"There isn't a decoration of type {decoration_type}."

        aquarium.add_decoration(decoration)
        self.decorations_repository.remove(decoration)
        return f"Successfully added {decoration_type} to {aquarium_name}."

    def find_aquarium_by_name(self, aquarium_name_):
        for aquarium_obj in self.aquariums:
            if aquarium_obj.name == aquarium_name_:
                return aquarium_obj

    def __find_aquarium_by_name(self, aquarium_name):
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                return aquarium

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        fish_mapper = {"FreshwaterFish": FreshwaterFish, "SaltwaterFish": SaltwaterFish}
        if fish_type not in fish_mapper:
            return f"There isn't a fish of type {fish_type}."

        aquarium = self.__find_aquarium_by_name(aquarium_name)
        new_fish = fish_mapper[fish_type](fish_name, fish_species, price)

        return aquarium.add_fish(new_fish)

    def feed_fish(self, aquarium_name: str):
        aquarium = self.__find_aquarium_by_name(aquarium_name)

        fed_count = len(aquarium.fish)
        for fish in aquarium.fish:
            fish.eat()

        return f"Fish fed: {fed_count}"

    def calculate_value(self, aquarium_name: str):
        aquarium = self.__find_aquarium_by_name(aquarium_name)
        fish_sum = sum([fish.price for fish in aquarium.fish])
        decorators_sum = sum(decorator.price for decorator in aquarium.decorator)
        total_value = fish_sum + decorators_sum
        return f"The value of Aquarium {aquarium_name} is {total_value:.2f}."

    def report(self):
        return '\n'.join([str(aquarium) for aquarium in self.aquariums])


