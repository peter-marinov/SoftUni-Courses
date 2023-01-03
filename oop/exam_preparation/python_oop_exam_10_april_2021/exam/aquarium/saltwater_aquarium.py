from project.aquarium.base_aquarium import BaseAquarium


class SaltwaterAquarium(BaseAquarium):
    INITIAL_CAPACITY = 25

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_CAPACITY)

    def calculate_comfort(self):
        return sum([d.comfort for d in self.decorations])

    def add_fish(self, fish):
        if self.capacity == 0:
            return "Not enough capacity."

        if type(fish).__name__ == 'SaltwaterFish':
            self.fish.append(fish)
            self.capacity -= 1
            return f"Successfully added {type(fish).__name__} to {self.name}."
        else:
            return 'Water not suitable.'

    def remove_fish(self, fish):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        fish_names = [fish.name for fish in self.fish]
        if not fish_names:
            fish_names = ['none']
        output = f"{self.name}:\n" \
                 f"Fish: {' '.join(fish_names)}\n" \
                 f"Decorations: {len(self.decorations)}\n" \
                 f"Comfort: {self.calculate_comfort()}"

        return output
