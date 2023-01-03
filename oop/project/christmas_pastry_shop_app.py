from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    def __init__(self):
        self.booths: list = []  # list that will contain all booths (objects) that are created
        self.delicacies: list = []  # list that will contain all delicacies (objects) that are created
        self.income: float = 0.0  # total income

    def __check_if_delicacy_exists(self, delicacy_name):
        for delicacy in self.delicacies:
            if delicacy.name == delicacy_name:
                return True

    def __check_if_booth_exists(self, booth_number):
        for booth in self.booths:
            if booth.booth_number == booth_number:
                return True

    def __find_first_available_booth(self, number_of_people):
        for booth in self.booths:
            if not booth.is_reserved and booth.capacity >= number_of_people:
                return booth
        return None

    def __get_booth(self, booth_number):
        for booth in self.booths:
            if booth.booth_number == booth_number:
                return booth

    def __get_delicacy(self, delicacy_name):
        for delicacy in self.delicacies:
            if delicacy.name == delicacy_name:
                return delicacy

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        delicacy_mapper = {'Gingerbread': Gingerbread, 'Stolen': Stolen}

        if self.__check_if_delicacy_exists(name):
            raise Exception(f"{name} already exists!")

        if type_delicacy not in delicacy_mapper.keys():
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        self.delicacies.append(delicacy_mapper[type_delicacy](name, price))
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        booth_mapper = {'Open Booth': OpenBooth, 'Private Booth': PrivateBooth}

        if self.__check_if_booth_exists(booth_number):
            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in booth_mapper.keys():
            raise Exception(f"{type_booth} is not a valid booth!")

        self.booths.append(booth_mapper[type_booth](booth_number, capacity))
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        current_booth = self.__find_first_available_booth(number_of_people)
        if current_booth is None:
            raise Exception(f"No available booth for {number_of_people} people!")

        current_booth.reserve(number_of_people)
        return f"Booth {current_booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        if not self.__check_if_booth_exists(booth_number):
            raise Exception(f"Could not find booth {booth_number}!")

        if not self.__check_if_delicacy_exists(delicacy_name):
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        current_booth = self.__get_booth(booth_number)
        current_delicacy = self.__get_delicacy(delicacy_name)
        current_booth.delicacy_orders.append(current_delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        current_booth = self.__get_booth(booth_number)
        current_bill = current_booth.price_for_reservation
        for delicacy in current_booth.delicacy_orders:
            current_bill += delicacy.price

        self.income += current_bill
        current_booth.price_for_reservation = 0
        current_booth.delicacy_orders = []
        current_booth.is_reserved = False

        output = f"Booth {booth_number}:\nBill: {current_bill:.2f}lv."
        return output

    def get_income(self):
        return f"Income: {self.income:.2f}lv."
