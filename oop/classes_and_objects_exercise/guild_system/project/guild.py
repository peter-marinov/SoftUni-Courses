class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player):
        if player.guild != self.name and player.guild != 'Unaffiliated':
            return f"Player {player.name} is in another guild."

        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."

        player.guild = self.name
        self.players.append(player)
        return f"Welcome player {player.name} to the guild {player.guild}"

    def kick_player(self, player_name: str):
        for player in self.players:
            if player.name == player_name:
                player.guild = 'Unaffiliated'
                self.players.remove(player)
                return f"Player {player_name} has been removed from the guild."

        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        output_string = f'Guild: {self.name}\n'
        for player in self.players:
            output_string += player.player_info() + '\n'

        return output_string.strip()