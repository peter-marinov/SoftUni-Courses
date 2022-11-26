def type_check(selected_type):
    def decorator(func_ref):
        def wrapper(*args):
            if not isinstance(*args, selected_type):
                return 'Bad Type'

            result = func_ref(*args)
            return result

        return wrapper

    return decorator


@type_check(int)
def times2(num):
    return num*2
print(times2(2))
print(times2('Not A Number'))


@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))