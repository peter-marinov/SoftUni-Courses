def multiply(n):
    def decorator(func_ref):
        def wrapper(*args):
            result = func_ref(*args)
            return result * n

        return wrapper

    return decorator


@multiply(3)
def add_ten(number):
    return number + 10

print(add_ten(3))