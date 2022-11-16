from inheritance_exercise.players_and_monsters.dark_wizard import DarkWizard


class SoulMaster(DarkWizard):
    def __init__(self, username, level):
        super().__init__(username, level)