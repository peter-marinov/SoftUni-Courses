coffee_cnt = 0
lowercase_list = ['coding', 'dog', 'cat', 'movie']
uppercase_list = ['CODING', 'DOG', 'CAT', 'MOVIE']
while True:
    command = input()
    if command == "END":
        break

    if command in lowercase_list:
        coffee_cnt += 1
    elif command in uppercase_list:
        coffee_cnt += 2

if coffee_cnt > 5:
    print("You need extra sleep")
else:
    print(coffee_cnt)