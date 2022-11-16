from inheritance_exercise.shop.product import Product


class Drink(Product):
    def __init__(self, name):
        super().__init__(name, 10)