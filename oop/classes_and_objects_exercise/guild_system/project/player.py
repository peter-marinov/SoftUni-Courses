class Player:
    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = 'Unaffiliated'

    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills:
            return "Skill already added"
        new_skill = {skill_name: mana_cost}
        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        output_string = f'Name: {self.name}\n'
        output_string += f'Guild: {self.guild}\n'
        output_string += f'HP: {self.hp}\n'
        output_string += f'MP: {self.mp}\n'
        for key, value in self.skills.items():
            output_string += f'==={key} - {value}\n'

        return output_string.strip()



