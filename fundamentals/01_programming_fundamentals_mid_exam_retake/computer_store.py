parts_price = 0
taxes = 0
total_price = 0

while True:
    command = input()
    if command == "special":
        taxes = parts_price * 0.2
        total_price = (parts_price + taxes) * 0.9
        break
    elif command == "regular":
        taxes = parts_price * 0.2
        total_price = parts_price + taxes
        break
    else:
        if float(command) <= 0:
            print("Invalid price!")
            continue
        parts_price += float(command)

if parts_price == 0:
    print("Invalid order!")
else:
    print(f"Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {parts_price:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_price:.2f}$")