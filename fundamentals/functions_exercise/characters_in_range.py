# def ascii_strings_between(first_str, last_str):
#     for symbol in range(ord(first_str) + 1, ord(last_str)):
#         print(f'{chr(symbol)}', end=' ')
#
# first_string = input()
# last_string = input()
# ascii_strings_between(first_string, last_string)

def ascii_strings_between(first_str, last_str):
    symbols_list = []
    for symbol in range(ord(first_str) + 1, ord(last_str)):
        symbols_list.append(chr(symbol))
    return symbols_list

first_string = input()
last_string = input()
result = ascii_strings_between(first_string, last_string)
print(' '.join(result))