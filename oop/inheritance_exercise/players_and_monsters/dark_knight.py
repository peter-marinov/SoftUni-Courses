from inheritance_exercise.players_and_monsters.knight import Knight


class DarkKnight(Knight):
    def __init__(self, username, level):
        super().__init__(username, level)
