input_line = input()

sum = 0

while input_line != "NoMoreMoney":
    money = float(input_line)
    if money < 0:
        print(f"Invalid operation!")
        break
    sum += money
    print(f"Increase: {money:.2f}")

    input_line = input()

print(f"Total: {sum:.2f}")
