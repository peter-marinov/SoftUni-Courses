empty_dict = {}

while True:
    key, value = input().split()
    empty_dict[key] += value
    print(empty_dict)