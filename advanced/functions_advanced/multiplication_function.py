def multiply(*args):
    result = 1
    # result = [result * int(x) for x in args]
    for el in args:
        result *= int(el)
    return result

print(multiply(1, 4, 5))