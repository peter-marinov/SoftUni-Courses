def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def pow(a, b):
    return a ** b


def calculate_expression(a, b, op):
    if op == '+':
        return add(a, b)
    elif op == '-':
        return sub(a, b)
    elif op == '/':
        return div(a, b)
    elif op == '*':
        return mul(a, b)
    elif op == '^':
        return pow(a, b)
    else:
        raise ValueError('Not supported operation')

