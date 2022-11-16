budget = int(input())

money_spent = 0

# while money_spent < budget:
# is_below_budget = True
# while is_below_budget:
while True:
    key_word = input()
    if key_word == 'End':
        print('You bought everything needed.')
        # is_below_budget = False
        break
    price = int(key_word)
    money_spent += price
    if money_spent > budget:
        print('You went in overdraft!')
        break
    # print(money_spent)

# if money_spent < budget:
#     print('You bought everything needed.')
# else:
#     print('You went in overdraft!')