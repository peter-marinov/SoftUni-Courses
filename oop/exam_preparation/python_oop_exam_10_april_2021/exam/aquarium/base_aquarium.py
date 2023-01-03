from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) == 0:
            raise ValueError("Aquarium name cannot be an empty string.")

        self.__name = value

    @abstractmethod
    def calculate_comfort(self):
        ...

    @abstractmethod
    def add_fish(self, fish):
        ...

    @abstractmethod
    def remove_fish(self, fish):
        ...

    @abstractmethod
    def add_decoration(self, decoration):
        ...

    @abstractmethod
    def feed(self):
        ...

    @abstractmethod
    def __str__(self):
        ...

