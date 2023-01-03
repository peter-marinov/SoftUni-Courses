from abc import abstractmethod

from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def __check_if_horse_exists(self, horse_name):
        for horse in self.horses:
            if horse.name == horse_name:
                return True

    @staticmethod
    def __create_new_horse(horse_type, horse_name, horse_speed):
        if horse_type == "Appaloosa":
            return Appaloosa(horse_name, horse_speed)

        return Thoroughbred(horse_name, horse_speed)

    def __check_if_jockey_exists(self, jockey_name):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                return True

    @staticmethod
    def __create_new_jockey(jockey_name, jockey_age):
        return Jockey(jockey_name, jockey_age)

    def __check_if_race_exists(self, race_name):
        for horse_race in self.horse_races:
            if horse_race.race_type == race_name:
                return True

    @staticmethod
    def __create_new_race(race_type):
        return HorseRace(race_type)

    def __get_jockey_by_name(self, jockey_name):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                return jockey

    def __get_race_by_type(self, race_type):
        for horse_race in self.horse_races:
            if horse_race.race_type == race_type:
                return horse_race

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if self.__check_if_horse_exists(horse_name):
            raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type in ["Appaloosa", "Thoroughbred"]:
            new_horse = self.__create_new_horse(horse_type, horse_name, horse_speed)
            self.horses.append(new_horse)

            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if self.__check_if_jockey_exists(jockey_name):
            raise Exception(f"Jockey {jockey_name} has been already added!")

        new_jockey = self.__create_new_jockey(jockey_name, age)
        self.jockeys.append(new_jockey)

        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if self.__check_if_race_exists(race_type):
            raise Exception(f"Race {race_type} has been already created!")

        new_race = self.__create_new_race(race_type)
        self.horse_races.append(new_race)

        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        # if not self.__check_if_jockey_exists(jockey_name):
        #     raise Exception(f"Jockey {jockey_name} could not be found!")
        #
        # current_horse = None
        # current_jockey = None
        # for horse in self.horses[::-1]:
        #     if type(horse).__name__ == horse_type:
        #         if horse.is_taken is False:
        #             current_horse = horse
        #             break
        # else:
        #     raise Exception(f"Horse breed {horse_type} could not be found!")
        #
        # current_jockey = self.__get_jockey_by_name(jockey_name)
        # if current_jockey.horse:
        #     return f"Jockey {jockey_name} already has a horse."
        #
        # current_jockey.horse = current_horse
        # current_jockey.is_taken = True
        #
        # return f"Jockey {jockey_name} will ride the horse {current_horse.name}."

        try:
            jockey = next(filter(lambda j: j.name == jockey_name, self.jockeys))
        except StopIteration:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        try:
            horse = list(filter(lambda h: h.__class__.__name__ == horse_type and not h.is_taken, self.horses))[-1]
        except IndexError:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."

        jockey.horse = horse
        horse.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        if not self.__check_if_race_exists(race_type):
            raise Exception(f"Race {race_type} could not be found!")

        if not self.__check_if_jockey_exists(jockey_name):
            raise Exception(f"Jockey {jockey_name} could not be found!")

        current_jockey = self.__get_jockey_by_name(jockey_name)
        if not current_jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        current_race_type = self.__get_race_by_type(race_type)
        if current_jockey in current_race_type.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        current_race_type.jockeys.append(current_jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        if not self.__check_if_race_exists(race_type):
            raise Exception(f"Race {race_type} could not be found!")

        current_race = self.__get_race_by_type(race_type)
        if len(current_race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        current_max_speed = 0
        winner = None
        for jockey in current_race.jockeys:
            if jockey.horse.speed > current_max_speed:
                current_max_speed = jockey.horse.speed
                winner = jockey

        return f"The winner of the {race_type} race, with a speed of {current_max_speed}km/h is " \
               f"{winner.name}! Winner's horse: {winner.horse.name}."







