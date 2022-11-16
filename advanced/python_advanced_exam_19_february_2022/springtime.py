def start_spring(**kwargs):
    spring_dict = {}
    sorted_dict = {}
    for key, value in kwargs.items():
        if value not in spring_dict.keys():
            spring_dict[value] = []
        if key not in spring_dict[value]:
            spring_dict[value].append(key)

    sorted_dict = dict(sorted(spring_dict.items(), key=lambda x: (-len(x[1]), x[0])))
    result = ''

    for key, values in sorted_dict.items():
        result += f'{key}:\n'
        for value in sorted(values):
            result += f'-{value}\n'
    return result


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))

example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",}
print(start_spring(**example_objects))


example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))