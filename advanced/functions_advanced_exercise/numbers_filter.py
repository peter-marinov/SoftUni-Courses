def even_odd_filter(**kwargs):
    if 'odd' in kwargs.keys():
        kwargs['odd'] = [i for i in kwargs['odd'] if i % 2 != 0]
    if 'even' in kwargs.keys():
        kwargs['even'] = [i for i in kwargs['even'] if i % 2 == 0]

    sorted_dict = dict(sorted(kwargs.items(), key=lambda x: -len(x[1])))
    return sorted_dict


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))