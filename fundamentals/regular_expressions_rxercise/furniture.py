import re

money_spend = 0
bought_furniture = []
pattern = r'>{2}([a-zA-Z]+)<{2}(\d+\.?\d*)!(\d+)'
while True:
    command = input()
    if command == "Purchase":
        break

    match = re.search(pattern, command)
    if match:
        furniture, price, queue = match.groups()
        bought_furniture.append(furniture)
        money_spend += float(price) * int(queue)

print("Bought furniture:")
# print('\n'.join(bought_furniture))
for item in bought_furniture:
    print(item)
print(f"Total money spend: {money_spend:.2f}")


