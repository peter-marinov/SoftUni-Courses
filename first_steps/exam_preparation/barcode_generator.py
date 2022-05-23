start_range = int(input())
end_range = int(input())

# print(start_range % 10)
# print(start_range // 1000)

start_first_number = start_range // 1000 % 10
start_second_number = start_range // 100 % 10
start_third_number = start_range // 10 % 10
start_forth_number = start_range % 10

end_first_number = end_range // 1000 % 10
end_second_number = end_range // 100 % 10
end_third_number = end_range // 10 % 10
end_forth_number = end_range % 10

# print(end_first_number)
# print(end_second_number)
# print(end_third_number)
# print(end_forth_number)

for first in range(start_first_number, end_first_number + 1):
    if first % 2 == 0:
        continue
    for second in range(start_second_number, end_second_number + 1):
        if second % 2 == 0:
            continue
        for third in range(start_third_number, end_third_number + 1):
            if third % 2 == 0:
                continue
            for forth in range(start_forth_number, end_forth_number + 1):
                if forth % 2 == 0:
                    continue
                print(f"{first}{second}{third}{forth}", end=" ")