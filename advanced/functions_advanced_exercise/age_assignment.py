def age_assignment(*args, **kwargs):
    names_dict = {}
    for name in args:
        names_dict[name] = kwargs[name[0]]

    sorted_dict = dict(sorted(names_dict.items(), key=lambda x: x[0]))

    result = ''
    for key, value in sorted_dict.items():
        result += f"{key} is {value} years old." + '\n'
    return result


print(age_assignment("Peter", "George", G=26, P=19))

print(age_assignment("Amy", "Bill", "Willy", W=36,A=22, B=61))