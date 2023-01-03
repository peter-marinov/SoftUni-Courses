from project.player import Player
from project.supply.supply import Supply


class Controller:
    def __init__(self):
        self.players: list = []
        self.supplies: list = []

    def __check_if_players_exist_by_name(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return True

    def __get_players_by_name(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return player

    def __take_last_supply(self, supply_type):
        for supply in self.supplies[::-1]:
            if type(supply).__name__ == supply_type:
                idx = self.supplies.index(supply)
                return self.supplies.pop(idx)
        if supply_type == "Food":
            raise Exception("There are no food supplies left!")
        if supply_type == "Drink":
            raise Exception("There are no drink supplies left!")

    def add_player(self, *args: Player):
        added_players_names = []
        for player in args:
            if not self.__check_if_players_exist_by_name(player.name):
                added_players_names.append(player.name)
                self.players.append(player)

        return f"Successfully added: {', '.join(added_players_names)}"

    def add_supply(self, *args: Supply):
        for supply in args:
            self.supplies.append(supply)

    def sustain(self, player_name: str, sustenance_type: str):
        current_player = self.__get_players_by_name(player_name)
        if not current_player.need_sustenance:
            return f"{current_player.name} have enough stamina."
        current_supply = self.__take_last_supply(sustenance_type)
        if current_supply:
            if current_player.stamina + current_supply.energy > 100:
                current_player.stamina = 100
            else:
                # if player_name == 'Lilly':
                #     for supply in self.supplies:
                #         print(supply.details())
                current_player.stamina += current_supply.energy

            return f"{player_name} sustained successfully with {current_supply.name}."

    @staticmethod
    def __can_fight(*args):
        result = []
        for player in args:
            if player.stamina == 0:
                result.append(f"Player {player.name} does not have enough stamina.")
        if result:
            return '\n'.join(result)

    @staticmethod
    def __attack(first_player, second_player):
        second_player.stamina -= first_player.stamina / 2
        if first_player.stamina - (second_player.stamina / 2) < 0:
            first_player.stamina = 0
        else:
            first_player.stamina -= second_player.stamina / 2

        if first_player.stamina > second_player.stamina:
            return f"Winner: {first_player.name}"

        return f"Winner: {second_player.name}"

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = self.__get_players_by_name(first_player_name)
        second_player = self.__get_players_by_name(second_player_name)

        result = self.__can_fight(first_player, second_player)
        if result:
            return result

        if first_player.stamina < second_player.stamina:
            return self.__attack(first_player, second_player)
        else:
            return self.__attack(second_player, first_player)

    def next_day(self):
        for player in self.players:
            if player.stamina - (player.age * 2) < 0:
                player.stamina = 0
            else:
                player.stamina -= player.age * 2
            # print(f'Before: {player.stamina}')
            self.sustain(player.name, "Food")
            # print(f'After food: {player.stamina}')
            self.sustain(player.name, "Drink")
            # print(f'After drink: {player.stamina}')

    def __str__(self):
        info = []
        for player in self.players:
            info.append(player.__str__())
        for supply in self.supplies:
            info.append(supply.details())
        result = "\n".join(info)
        return result


