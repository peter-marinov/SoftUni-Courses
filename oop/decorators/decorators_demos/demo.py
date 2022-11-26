# def parse_number(number_as_str):
#     return int(number_as_str)
#
# def my_func(element, parse_func):
#     return parse_func(element)
#
# el = '23'
#
# print(my_func(el, parse_number))


def hello_func(name):
    def say_hi():
        return f'I am saying hi to {name}'

    return say_hi

greeting_func = hello_func('pesho')
print(hello_func('pesho')())
print(greeting_func())