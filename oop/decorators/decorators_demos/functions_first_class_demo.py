def print_list(ll):
    pass

def increment_list_values(ll):
    return [x + 1 for x in ll]

def apply_func_for_list_values(ll, func):
    return [func(x) for x in ll]

ll = []
print_list(ll)

print(
    apply_func_for_list_values([1, 2, 3], lambda x: x + 2)
)


def f(x):
    def f_internal(y):
        return x + y

    return f_internal

f1 = f(2)
print(f1)
print(f1(3))
print(f1(4))
print(f1(2))