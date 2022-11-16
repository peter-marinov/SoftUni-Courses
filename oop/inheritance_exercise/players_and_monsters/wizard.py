from inheritance_exercise.players_and_monsters.hero import Hero


class Wizard(Hero):
    def __init__(self, username, level):
        super().__init__(username, level)