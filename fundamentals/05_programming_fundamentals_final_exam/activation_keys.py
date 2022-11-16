def contains(raw_activation_key, substring):
    if substring in raw_activation_key:
        return f'{raw_activation_key} contains {substring}'
    return 'Substring not found!'


def flip(raw_activation_key, mode, start_index, end_index):
    if mode == 'Upper':
        raw_activation_key = raw_activation_key[:start_index] + \
                             raw_activation_key[start_index:end_index].upper() + \
                             raw_activation_key[end_index:]
    elif mode == 'Lower':
        raw_activation_key = raw_activation_key[:start_index] + \
                             raw_activation_key[start_index:end_index].lower() + \
                             raw_activation_key[end_index:]
    print(raw_activation_key)
    return raw_activation_key


def slice(raw_activation_key, start_index, end_index):
    raw_activation_key = raw_activation_key.replace(raw_activation_key[start_index:end_index], '')
    # print(raw_activation_key[start_index:end_index])
    print(raw_activation_key)
    return raw_activation_key

raw_activation_key = input()

while True:
    command = input().split('>>>')

    if command[0] == 'Generate':
        print(f"Your activation key is: {raw_activation_key}")
        break

    action = command[0]
    if action == 'Contains':
        substring = command[1]
        print(contains(raw_activation_key, substring))
    elif action == 'Flip':
        mode, start_index, end_index = command[1], int(command[2]), int(command[3])
        raw_activation_key = flip(raw_activation_key, mode, start_index, end_index)
    elif action == 'Slice':
        start_index, end_index = int(command[1]), int(command[2])
        raw_activation_key = slice(raw_activation_key, start_index, end_index)