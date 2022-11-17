def custom_range_1(n):
    value = 1
    while value < n:
        yield value
        value += 1


def custom_range_2(n):
    values = list(range(1, n))
    for value in values:
        yield value

for x in custom_range_1(5):
    print(x)

for x in custom_range_2(5):
    print(x)