class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
            Zoo.__animals += 1
        elif species == 'fish':
            self.fishes.append(name)
            Zoo.__animals += 1
        elif species == 'bird':
            self.birds.append(name)
            Zoo.__animals += 1


    def get_info(self, species):
        if species == 'mammal':
            print(f"Mammals in {self.name}: {', '.join(self.mammals)}")
        elif species == 'fish':
            print(f"Fishes in {self.name}: {', '.join(self.fishes)}")
        elif species == 'bird':
            print(f"Birds in {self.name}: {', '.join(self.birds)}")

        # print(f"Total animals: {len(self.mammals) + len(self.fishes) + len(self.birds)}")
        print(f"Total animals: {Zoo.__animals}")


zoo_name = input()
zoo = Zoo(zoo_name)

number_of_animals = int(input())
for animal in range(number_of_animals):
    animal_specie, type_of_animal = input().split(' ')
    zoo.add_animal(animal_specie, type_of_animal)

selected_type = input()
zoo.get_info(selected_type)
