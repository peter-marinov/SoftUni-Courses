from abc import abstractmethod

from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def __check_if_car_exists_by_model(self, model_name):
        for car in self.cars:
            if car.model == model_name:
                return True

    def __check_if_car_model_is_available(self, model_name):
        for car in self.cars[::-1]:
            if not car.is_taken:
                return car
        return False

    def __get_car_by_model(self, model_name):
        for car in self.cars:
            if car.model == model_name:
                return car

    def __check_if_driver_exists_by_name(self, driver_name):
        for driver in self.drivers:
            if driver.name == driver_name:
                return True

    def __get_driver_by_name(self, driver_name):
        for driver in self.drivers:
            if driver.name == driver_name:
                return driver

    def __check_if_race_exists_by_name(self, race_name):
        for race in self.races:
            if race.name == race_name:
                return True

    def __get_race_by_name(self, race_name):
        for race in self.races:
            if race.name == race_name:
                return race

    @staticmethod
    def __sort_winners(race: Race):
        winners = {}
        for driver in race.drivers:
            winners[driver.name] = driver.car.speed_limit

        winners = dict(sorted(winners.items(), key=lambda x: -x[1]))
        while len(winners) > 3:
            winners.popitem()

        return winners

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type in ["MuscleCar", "SportsCar"]:
            if self.__check_if_car_exists_by_model(model):
                raise Exception(f"Car {model} is already created!")
            else:
                if car_type == "MuscleCar":
                    new_car = MuscleCar(model, speed_limit)
                else:
                    new_car = SportsCar(model, speed_limit)
                self.cars.append(new_car)
                return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        if self.__check_if_driver_exists_by_name(driver_name):
            raise Exception(f"Driver {driver_name} is already created!")

        new_driver = Driver(driver_name)
        self.drivers.append(new_driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        if self.__check_if_race_exists_by_name(race_name):
            raise Exception(f"Race {race_name} is already created!")

        new_race = Race(race_name)
        self.races.append(new_race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        if not self.__check_if_driver_exists_by_name(driver_name):
            raise Exception(f"Driver {driver_name} could not be found!")

        searched_car = self.__check_if_car_model_is_available(car_type)
        if not searched_car:
            raise Exception(f"Car {car_type} could not be found!")

        searched_driver = self.__get_driver_by_name(driver_name)
        if searched_driver.car is not None:
            old_car = self.__get_car_by_model(searched_driver.car.model)
            old_car.is_taken = False
            searched_car.is_taken = True
            searched_driver.car = searched_car
            return f"Driver {searched_driver.name} changed his car from {old_car.model} to {searched_car.model}."

        searched_car.is_taken = True
        searched_driver.car = searched_car
        return f"Driver {searched_driver.name} chose the car {searched_car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        if not self.__check_if_race_exists_by_name(race_name):
            raise Exception(f"Race {race_name} could not be found!")

        if not self.__check_if_driver_exists_by_name(driver_name):
            raise Exception(f"Driver {driver_name} could not be found!")

        driver = self.__get_driver_by_name(driver_name)
        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        race = self.__get_race_by_name(race_name)

        for race_driver in race.drivers:
            if race_driver.name == driver.name:
                return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        if not self.__check_if_race_exists_by_name(race_name):
            raise Exception(f"Race {race_name} could not be found!")

        race = self.__get_race_by_name(race_name)
        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        winners = self.__sort_winners(race)
        output_str = []
        for driver_name, top_speed in winners.items():
            winner_driver = self.__get_driver_by_name(driver_name)
            winner_driver.number_of_wins += 1
            output_str.append(f"Driver {driver_name} wins the {race_name} race with a speed of {top_speed}.")

        return '\n'.join(output_str)









