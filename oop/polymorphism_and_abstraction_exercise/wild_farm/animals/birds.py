from polymorphism_and_abstraction_exercise import Bird


class Owl(Bird):
    EATABLE_FOOD = ['Meat']
    ANIMAL_WEIGHT_PER_PEACE_OF_FOOD = 0.25

    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)

    @staticmethod
    def make_sound():
        return 'Hoot Hoot'


class Hen(Bird):
    EATABLE_FOOD = ['Vegetable', 'Fruit', 'Meat', 'Seed']
    ANIMAL_WEIGHT_PER_PEACE_OF_FOOD = 0.35

    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)

    @staticmethod
    def make_sound():
        return 'Cluck'
