'''
first_sequence = set(input().split())
second_sequence = set(input().split())

lines = int(input())

for _ in range(lines):
    command = input().split()
    action = command[0]
    if action == "Add":
        numbers_to_add = set(command[2:])
        selector = command[1]
        if selector == "First":
            first_sequence = first_sequence.union(numbers_to_add)
        else:
            second_sequence = second_sequence.union(numbers_to_add)
    elif action == "Remove":
        numbers_to_remove = set(command[2:])
        selector = command[1]
        for num in numbers_to_remove:
            if selector == "First" and num in first_sequence:
                first_sequence.remove(num)
            elif selector == "Second" and num in second_sequence:
                second_sequence.remove(num)
    elif action == "Check":
        if first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence):
            print("True")
        else:
            print("False")

print(', '.join(sorted(first_sequence)))
print(', '.join(sorted(second_sequence)))
'''

# The issue was the I was sorting str values instead of the int!!!

first_set, second_set = {*input().split()}, {*input().split()}
# first_set = set(input().split())
# second_set = set(input().split())

N = int(input())

for _ in range(N):
    command = input()
    if 'Add First' in command:
        numbers = command.split()[2:]
        first_set = first_set.union(numbers)
    elif 'Add Second' in command:
        numbers = command.split()[2:]
        second_set = second_set.union(numbers)
    elif 'Remove First' in command:
        numbers = command.split()[2:]
        for number in numbers:
            if number in first_set:
                first_set.remove(number)
    elif 'Remove Second' in command:
        numbers = command.split()[2:]
        for number in numbers:
            if number in second_set:
                second_set.remove(number)
    else:
        print('True' if first_set.issubset(second_set) or second_set.issubset(first_set) else 'False')

print(', '.join(map(str, (sorted(map(int, first_set))))))
print(', '.join(map(str, (sorted(map(int, second_set))))))
