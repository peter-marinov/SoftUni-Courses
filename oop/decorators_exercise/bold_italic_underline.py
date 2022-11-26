from functools import wraps


def make_bold(func_ref):
    @wraps(func_ref)
    def wrapper(*args):
        result = func_ref(*args)
        return f'<b>{result}</b>'

    return wrapper


def make_italic(func_ref):
    @wraps(func_ref)
    def wrapper(*args):
        result = func_ref(*args)
        return f'<i>{result}</i>'

    return wrapper


def make_underline(func_ref):
    @wraps(func_ref)
    def wrapper(*args):
        result = func_ref(*args)
        return f'<u>{result}</u>'

    return wrapper


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"

print(greet("Peter"))