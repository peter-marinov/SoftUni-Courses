user_names = input().split(', ')
valid_user_names = []

for user in user_names:
    valid_user = False
    if 3 <= len(user) <= 16:
        if ',' in user:
            continue
        for symbol in user:
            # print(symbol)
            if not (symbol.isalpha() or symbol.isdigit() or symbol == "-" or symbol == "_"):
                # print(symbol)
                valid_user = False
                break
            else:
                valid_user = True
        if valid_user:
            valid_user_names.append(user)

[print(f'{current_user}') for current_user in valid_user_names]