# farming_dict = {'shards': 0,
#                 'fragments': 0,
#                 'motes': 0}
#
# while True:
#     command = input().split(' ')
#     print(farming_dict)
#     if command == "stop":
#         print(farming_dict)
#         break
#     for index in range(0, len(command), 2):
#         value = int(command[index])
#         key = command[index + 1]
#         if key.lower() in farming_dict:
#             farming_dict[key.lower()] += value
#         else:
#             farming_dict[key] = value

########################

items = {"shards": 0, "fragments": 0, "motes": 0}
obtained = False
command = input().split()
while not obtained:
    for index in range(0, len(command), 2):
        value = int(command[index])
        key = command[index + 1].lower()
        if key not in items.keys(): #in useless_items
                items[key] = 0
        items[key] += value
        if items["shards"] >= 250:
            print("Shadowmourne obtained!")
            items["shards"] -= 250
            obtained = True
        elif items["fragments"] >= 250:
            print("Valanyr obtained!")
            items["fragments"] -= 250
            obtained = True
        elif items["motes"] >= 250:
            print("Dragonwrath obtained!")
            items["motes"] -= 250
            obtained = True
        if obtained:
            break
    if obtained:
        break
    command = input().split()
for material,quantity in items.items():
    print(f"{material}: {quantity}")











