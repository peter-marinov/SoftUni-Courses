needed_money = float(input())
money_in_hand = float(input())
spending_counter = 0
total_days = 0
spending_too_many_days = False

while money_in_hand < needed_money:
    action = input()
    current_sum = float(input())
    total_days += 1
    if action == "save":
        spending_counter = 0
        money_in_hand += current_sum
    else: # spend
        spending_counter += 1
        if spending_counter == 5:
            spending_too_many_days = True
            break

        money_in_hand -= current_sum
        if money_in_hand < 0:
            money_in_hand = 0


if spending_too_many_days:
    print("You can't save the money.")
    print(f"{total_days}")
else:
    print(f"You saved the money for {total_days} days.")