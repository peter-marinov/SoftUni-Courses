from functools import wraps


def vowel_filter(func_ref):
    vowels = 'aoeiyu'

    @wraps(func_ref)
    def wrapper():
        result = func_ref()
        return [x for x in result if x.lower() in vowels]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())