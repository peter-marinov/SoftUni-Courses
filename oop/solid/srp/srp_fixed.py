# SRP Violation - calculate area for both triangle and rectangle
# solved bt splitting into multiple classes
import os


class Triangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height / 2


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


class ComplexShape:
    def __init__(self, shapes):
        self.shapes = shapes

    def get_complex_shape_area(self):
        the_sum = 0
        for shape in self.shapes:
            the_sum += shape.get_area()
            # if isinstance(shape, Triangle):
            #     the_sum += shape.get_triangle_area()
            # elif isinstance(shape, Rectangle):
            #     the_sum += shape.get_rectangle_area()
        return the_sum


class StdPrinter:
    def print(self, obj):
        print(obj)


class FilePrinter:
    def __init__(self, filename):
        self.filename = filename

    def print(self, obj):
        with open(self.filename, 'a') as file:
            file.write(str(obj))
            file.write(os.linesep)


printer = StdPrinter()
tr = Triangle(10, 5)
rect = Rectangle(10, 5)
cs = ComplexShape([tr, rect])

printer.print(tr.get_area())
printer.print('-' * 10)
printer.print(rect.get_area())
printer.print('-' * 10)
printer.print(cs.get_complex_shape_area())