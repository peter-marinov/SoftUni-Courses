def check_contact(memory_dict, number_of_searches):
    for _ in range(number_of_searches):
        searched_name = input()
        if searched_name in memory_dict:
            print(f'{searched_name} -> {memory_dict[searched_name]}')
        else:
            print(f"Contact {searched_name} does not exist.")

phonebook_dict = {}

while True:
    command = input().split('-')
    if command[0].isdigit():
        check_contact(phonebook_dict, int(command[0]))
        break
    name, number = command[0], command[1]

    # if name in phonebook_dict:
    phonebook_dict[name] = number
    # print(phonebook_dict)