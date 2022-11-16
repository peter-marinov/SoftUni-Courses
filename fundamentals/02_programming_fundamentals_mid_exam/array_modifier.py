numbers = list(map(int, input().split()))

command = input()

while command != "end":
    command = command.split()
    if command[0] == "swap":
        numbers[int(command[1])], numbers[int(command[2])] = numbers[int(command[2])], numbers[int(command[1])]
    elif command[0] == "multiply":
        numbers[int(command[1])] = numbers[int(command[1])] * numbers[int(command[2])]
    elif command[0] == "decrease":
        numbers = [int(num) - 1 for num in numbers]
    command = input()

print(", ".join([str(num) for num in numbers]))