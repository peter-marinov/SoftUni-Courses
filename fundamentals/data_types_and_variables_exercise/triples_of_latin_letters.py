number_of_letters = int(input())

for first_letter in range(number_of_letters):
    for second_letter in range(number_of_letters):
        for third_letter in range(number_of_letters):
            current_string = chr(97+first_letter) + chr(97+second_letter) + chr(97+third_letter)
            print(current_string)