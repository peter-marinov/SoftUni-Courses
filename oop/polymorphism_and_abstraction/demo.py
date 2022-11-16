from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 2:
            raise ValueError('Cannot set name less than 2 chars')
            self.name(value)
        self.__name = value


class Cat(Animal):
    def __init__(self, name, lazyness):
        super().__init__(name)
        self.lazyness = lazyness

a = Cat('a', 10)
print(a)