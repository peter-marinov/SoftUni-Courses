from functools import wraps


def uppercase(func_ref):
    @wraps(func_ref)
    def wrapper():
        func_result = func_ref()
        return func_result.upper()

    return wrapper


@uppercase
def say_hi():
    return 'hello world'

@uppercase
def say_goodbye():
    return 'goodbye world'



print(say_hi())
print(say_goodbye())