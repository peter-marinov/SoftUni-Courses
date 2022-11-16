import random

number_to_be_guessed_a = random.randint(0, 9)
number_to_be_guessed_b = random.randint(0, 9)
number_to_be_guessed_c = random.randint(0, 9)
number_to_be_guessed_d = random.randint(0, 9)

number_to_be_guessed = str(number_to_be_guessed_a)+str(number_to_be_guessed_b)+str(number_to_be_guessed_c)+str(number_to_be_guessed_d)
# Hardcode value for debug
# number_to_be_guessed = "0728"
# print(number_to_be_guessed)

number_to_be_guessed_as_int = int(number_to_be_guessed)
number_is_not_guessed = True
number_of_guesses = 0

while number_is_not_guessed:
    player_guess = input('Въведете вашето предположение: ')
    cows = 0
    bulls = 0
    # Checks if the input string is a number and it is in the range from 0000 to 9999 and if the string has 4 bits
    if str.isdigit(player_guess):
        player_guess_as_int = int(player_guess)
        if player_guess_as_int < 0 or player_guess_as_int > 9999:
            print('Въведеното число е извън диапазона от 0000 до 9999.')
            continue
        if len(player_guess) != 4:
            print('Въведеното число е извън диапазона от 0000 до 9999.')
            continue
        number_of_guesses += 1
        # Check if the random number is equal to the input one
        if player_guess_as_int == number_to_be_guessed_as_int:
            print(f'Честито! С {number_of_guesses} коректни опита успяхте да познаете числото {number_to_be_guessed}!')
            number_is_not_guessed = False
            # break
        else:
            flag_index = "0000" # Each bit will reflect to if there is bull on each index
            # Checking if there is any bulls
            for number in range(len(number_to_be_guessed)):
                if number_to_be_guessed[number] == player_guess[number]:
                    # print(number_to_be_guessed[number], player_guess[number])
                    bulls += 1
                    flag_index = flag_index[:number] + "1" + flag_index[number+1:]
            # Checks the rest positions, which have no bulls
            for  index in range(len(number_to_be_guessed)):
                if flag_index[index] == "0":
                    for item in range(len(number_to_be_guessed)):
                        if number_to_be_guessed[index] == player_guess[item] and flag_index[item] == "0":
                            # print(number_to_be_guessed[index], player_guess[item], flag_index[item])
                            cows += 1
                            break
            print(f"Не успяхте да познаете числото. Имате {bulls} бика и {cows} крави.")
    else:
        print('Въведеното предложение не е число.')
