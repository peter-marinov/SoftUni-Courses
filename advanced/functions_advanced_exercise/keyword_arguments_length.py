def kwargs_length(**args):
    return len(args)

dictionary = {'name': 'Peter', 'age': 25}

print(kwargs_length(**dictionary))