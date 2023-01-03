class Client:
    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_cart = []
        self.bill = 0.00
        self.ordered_meals = {}

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        if value[0] != "0":
            raise ValueError("Invalid phone number!")
        if len(value) != 10:
            raise ValueError("Invalid phone number!")
        for number in value:
            if not number.isdigit():
                raise ValueError("Invalid phone number!")
        self.__phone_number = value

