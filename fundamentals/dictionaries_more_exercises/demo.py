import operator

test_dict = {"one": 1, "two": 2, "three": 3}

test_dict = sorted(test_dict.items(), key=operator.itemgetter(1))`
print(test_dict)