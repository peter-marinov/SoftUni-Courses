from functools import wraps


def logged(func_ref):

    @wraps(func_ref)
    def wrapper(*args):
        result = func_ref(*args)
        output = (f'you called {func_ref.__name__}{args}\n'
                  f'it returned {result}')
        return output

    return wrapper

@logged
def func(*args):
    return 3 + len(args)
print(func(4, 4, 4))