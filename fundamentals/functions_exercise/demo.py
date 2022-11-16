def length_is_valid(some_string):
    if 6 <= len(some_string) <= 10:
        return True
    print("Password must be between 6 and 10 characters")
    return False


def symbols_are_valid(some_string):
    if some_string.isalnum():
        return True
    print("Password must consist only of letters and digits")
    return False


def have_at_least_two_digits(some_string):
    digit_counter = 0
    for character in some_string:
        if character.isdigit():
            digit_counter += 1
    if digit_counter >= 2:
        return True
    print("Password must have at least 2 digits")
    return False


some_password = input()
validated = [length_is_valid(some_password), symbols_are_valid(some_password), have_at_least_two_digits(some_password)]
# print(validated)
# if False not in validated:
if all(validated):
    print("Password is valid")