spell = input()

while True:
    command = input().split()
    if command[0] == 'Abracadabra':
        # print(spell)
        break

    action = command[0]
    if action == 'Abjuration':
        for index in range(len(spell)):
            if spell[index].isalpha():
                spell = spell.replace(spell[index], spell[index].upper(), 1)
        print(spell)
    elif action == 'Necromancy':
        for index in range(len(spell)):
            if spell[index].isalpha():
                spell = spell.replace(spell[index], spell[index].lower(), 1)
        print(spell)
    elif action == 'Illusion':
        index, letter = int(command[1]), command[2]
        if 0 <= index < len(spell):
            spell = spell.replace(spell[index], letter, 1)
            print('Done!')
        else:
            print('The spell was too weak.')
    elif action == 'Divination':
        first_substring, second_substring = command[1:]
        if first_substring in spell:
            spell = spell.replace(first_substring, second_substring)
            print(spell)
    elif action == 'Alteration':
        substring = command[1]
        if substring in spell:
            spell = spell.replace(substring, '')
            print(spell)
    else:
        print('The spell did not work!')