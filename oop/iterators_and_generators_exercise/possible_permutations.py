from itertools import permutations

def possible_permutations(elements):
    for result in permutations(elements):
        yield list(result)


[print(n) for n in possible_permutations([1, 2, 3])]