from abc import ABC, abstractmethod


class Animal(ABC):
    EATABLE_FOOD = []
    ANIMAL_WEIGHT_PER_PEACE_OF_FOOD = 0

    @abstractmethod
    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @staticmethod
    def make_sound():
        pass

    def feed(self, food):
        if food.__class__.__name__ not in self.EATABLE_FOOD:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += self.ANIMAL_WEIGHT_PER_PEACE_OF_FOOD * food.quantity
        self.food_eaten += food.quantity


class Bird(Animal):
    @abstractmethod
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        values = [self.name, str(self.wing_size), str(self.weight), str(self.food_eaten)]
        # return f"{self.__class__.__name__} [{', '.join(values)}]"
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal):
    @abstractmethod
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        values = [str(value) for value in self.__dict__.values()]
        # return f"{self.__class__.__name__} [{', '.join(values)}]"
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"