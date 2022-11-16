from classes_and_objects_exercise.guild_system import Player
from classes_and_objects_exercise.guild_system.project.guild import Guild

player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())