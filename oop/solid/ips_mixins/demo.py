import abc


class StrFromDictMixin:
    def __str__(self):
        return '; '.join(f'{key}: {value}' for key, value in self.__dict__.items())


class Shape(abc.ABC):
    @property
    @abc.abstractmethod
    def area(self):
        pass


class Rectangle(Shape, StrFromDictMixin):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.height * self.height

    # def __str__(self):
    #     return f'width={self.width} height={self.height}'


class Circle(Shape, StrFromDictMixin):
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return self.radius * self.radius * 2

    # def __str__(self):

c = Circle(10)
print(c)
