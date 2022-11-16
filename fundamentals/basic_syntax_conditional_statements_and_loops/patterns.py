number_of_starts = int(input())

for star in range(1, number_of_starts + 1):
    print(star * '*')

for star in range(number_of_starts-1, 0, - 1):
    print(star * '*')