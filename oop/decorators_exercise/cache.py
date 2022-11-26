def cache(func_ref):
    def wrapper(number):
        cache_key = number
        if cache_key not in wrapper.log:
            wrapper.log[cache_key] = func_ref(number)

        return wrapper.log[cache_key]

    wrapper.log = {}

    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci(3)
print(fibonacci.log)