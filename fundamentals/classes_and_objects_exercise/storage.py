# class Storage:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.storage = []
#
#     def add_product(self, product: str):
#         if len(self.storage) < int(self.capacity):
#             if type(product) == str and not any(char.isdigit() for char in product):
#                 self.storage.append(product)
#         # print(self.storage)
#
#     def get_products(self):
#         return self.storage

class Storage:
    storage = []

    def __init__(self, capacity):
        self.capacity = capacity
        # self.storage = []

    def add_product(self, product: str):
        if self.capacity > 0:
            Storage.storage.append(product)
            self.capacity -= 1
        # print(self.storage)

    def get_products(self):
        return Storage.storage


storage = Storage(2)
storage.add_product("apple")
storage.add_product(5)
storage.add_product("potato2")
storage.add_product("tomato")
storage.add_product("bread")
print(storage.get_products())
