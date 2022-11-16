from inheritance_exercise.zoo.animal import Animal


class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)
