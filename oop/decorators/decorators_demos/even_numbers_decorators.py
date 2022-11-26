class func_even_numbers:
    def __init__(self, func_ref):
        self.func_ref = func_ref

    def __call__(self, *args, **kwargs):
        result = self.func_ref(*args, **kwargs)
        return [x for x in result if x % 2 == 0]


@func_even_numbers
def get_numbers(numbers):
    return numbers
print(get_numbers([1, 2, 3, 4, 5]))
