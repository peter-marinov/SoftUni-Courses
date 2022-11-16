# def say_hello(*args):
#     print(f"Hello, {', '.join(args)}")
#
# say_hello('peter', 'gosho', 'ivan

# def info(**kwargs):
#     print(kwargs)
#
# info(first_name='pesho', second_name="georgiev")

people = {
    'ivan': 14,
    'gosho': 19,
    'mimi': 14,
    'ani': 14
}

# 1. Age in ascending order.
# 2. Name length in descending order.
# 3. Name in ascending order

result = sorted(people.items(), key=lambda x: (x[1], -len(x[0]), x[0]))
print(result)