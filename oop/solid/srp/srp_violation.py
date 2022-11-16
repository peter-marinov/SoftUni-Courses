class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # SRP Violation - calculate area for both triangle and rectangle
    def print_triangle_area(self):
        area = self.width * self.height / 2
        print(area) # SRP Violation - calculation and printing

    def print_rectangle_area(self):
        area = self.width * self.height
        print(area) # SRP Violation - calculation and printing


tr = Shape(10, 5)
rect = Shape(10, 5)

tr.print_triangle_area()
rect.print_rectangle_area()
