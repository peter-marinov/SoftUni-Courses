# a = dict(name='Gosho', age=15)
# b = dict(smart='low', salam='leki')
# c = {**a, **b}
# print(c)

# letters = ['a', 'b', 'c', 'd']
# nums = [1, 2, 3, 4]
# result = dict(zip(letters, nums))
# print(result)

# squares = {1: 'one', 2: 'two', 3: 'three'}
#
# for el in squares.keys():
#     print(el)
#
# for el in squares.items():
#     print(el)
#
# for el in squares.values():
#     print(el)
#
# for key, value in squares.items():
#     print(key, value)


# my_dict = {'one': 1, 'two': 2, 'three': 3}
# print('one' in my_dict)
# print(1 in my_dict.values())

# help(dict)

# my_dict = {'one': 1, 'two': 2, 'three': 3}
# my_dict.clear()
# print(my_dict)

# my_dict = {'one': 1, 'two': 2, 'three': 3}
# new_dict = my_dict.copy()
# print(new_dict)

# my_dict = {'one': 1, 'two': 2, 'three': 3}
# new_dict = my_dict.copy()
# print(my_dict.pop('one'))
# print(my_dict.popitem())
# print(my_dict)

# numbers = {'one': 1, 'two': 2, 'three': 3}
# del numbers['one']
# print(numbers)

# numbers = {'one': 1, 'two': 2, 'three': 3}
# print(numbers.get('one'))

# numbers = {'one': 1, 'two': 2, 'three': 3}
# print(numbers.setdefault(4))
# print(numbers)

# numbers_1 = {1: 'one', 2: 'two', 3: 'three'}
# numbers_2 = {4: 'four', 5: 'five'}
# numbers_1.update(numbers_2)
# print(numbers_1)

# example_dict = {'nums': {1: 'one', 2: 'two'},
#                 'letters': {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D'}}
#
# print(example_dict['nums'][1])

# example_dict = {'nums': {1: 'one', 2: 'two'},
#                 'letters': {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D'}}
#
# example_dict['chars'] = {'plus': '+', 'minus': '-'}
# 
# print(example_dict)

example_dict = {'a': 10, 'b': 20, 'c': 30}
comprehension_dict = {key * 2: value * 2 for key, value in example_dict.items()}
print(comprehension_dict)