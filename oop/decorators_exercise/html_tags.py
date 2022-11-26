def tags(tag):
    def decorator(func_ref):
        def wrapper(*args):
            output = func_ref(*args)
            return f'<{tag}>{output}</{tag}>'

        return wrapper
    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)
print(join_strings("Hello", " you!"))


@tags('h1')
def to_upper(text):
    return text.upper()
print(to_upper('hello'))