import random
from colorama import Fore


class InvalidLevelError(Exception):
    pass


try:
    level = int(input(Fore.BLUE + "Select level: "))

except ValueError:
    raise InvalidLevelError("The level you selected isn't valid")

if level <= 0:
    raise InvalidLevelError("The level you selected isn't valid")

computer_number = random.randint(1, 10 * level)
play = True

while play:
    try:
        player_number = int(input(Fore.WHITE + "Guess the number: "))
    except ValueError:
        print(Fore.RED + "Enter a number!")
        continue

    if player_number == computer_number:
        print("You guessed it!")
        play = True if input("Do you want to play again? [y/n] ") == "y" else False
        if play:
            computer_number = random.randint(1, 10 * level)
    elif player_number < computer_number:
        print("Higher")
    else:
        print("Lower")