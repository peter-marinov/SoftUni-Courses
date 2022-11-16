def get_line(i, n):
    spaces_count = n - 1 - i
    starts_count = i + 1
    return ' ' * spaces_count + ('* ' * starts_count).strip()


def print_line(n):
    print(get_line(n - 1, n - 1))


def print_rhombus(n):
    for i in range(n):
        print(get_line(i, n))
    for i in range(n - 2, -1, -1):
        print(get_line(i, n))

print_rhombus(int(input()))

print_rhombus(1)
print_rhombus(2)
print_rhombus(3)
print_rhombus(4)
print_line(4)