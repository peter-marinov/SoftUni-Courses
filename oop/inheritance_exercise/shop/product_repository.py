from inheritance_exercise.shop.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name):
        for product in self.products:
            if product.name == product_name:
                return product

    def remove(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)

    def __repr__(self):
        output_str = [f'{product.__dict__["name"]}: {product.__dict__["quantity"]}' for product in self.products]
        return f'\n'.join(output_str)
