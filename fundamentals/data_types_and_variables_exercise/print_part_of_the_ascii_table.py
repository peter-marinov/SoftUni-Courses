start_point = int(input())
end_point = int(input())

for character in range(start_point, end_point + 1):
    print(f'{chr(character)}', end=' ')