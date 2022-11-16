from inheritance_exercise.players_and_monsters.wizard import Wizard


class DarkWizard(Wizard):
    def __init__(self, username, level):
        super().__init__(username, level)