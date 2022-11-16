class Catalogue:
    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self,fist_letter: str):
        return [product for product in self.products if product[0] == fist_letter]

    def __repr__(self):
        n1 = '\n'
        # reversed_list = self.products.sort()
        # print(reversed_list)
        self.products.sort()
        return f"Items in the {self.name} catalogue:\n{n1.join(self.products)}"

catalogue = Catalogue("Furniture")

catalogue.add_product("Sofa")

catalogue.add_product("Mirror")

catalogue.add_product("Desk")

catalogue.add_product("Chair")

catalogue.add_product("Carpet")

print(catalogue.get_by_letter("C"))

print(catalogue)