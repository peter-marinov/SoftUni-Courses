from polymorphism_and_abstraction_exercise import Mammal


class Mouse(Mammal):
    EATABLE_FOOD = ['Vegetable', 'Fruit']
    ANIMAL_WEIGHT_PER_PEACE_OF_FOOD = 0.1

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    @staticmethod
    def make_sound():
        return 'Squeak'


class Dog(Mammal):
    EATABLE_FOOD = ['Meat']
    ANIMAL_WEIGHT_PER_PEACE_OF_FOOD = 0.4

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    @staticmethod
    def make_sound():
        return 'Woof!'


class Cat(Mammal):
    EATABLE_FOOD = ['Vegetable', 'Meat']
    ANIMAL_WEIGHT_PER_PEACE_OF_FOOD = 0.3

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    @staticmethod
    def make_sound():
        return 'Meow'


class Tiger(Mammal):
    EATABLE_FOOD = ['Meat']
    ANIMAL_WEIGHT_PER_PEACE_OF_FOOD = 1

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    @staticmethod
    def make_sound():
        return 'ROAR!!!'

