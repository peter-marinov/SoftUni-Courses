def words_sorting(*words):
    words_dict = {word: sum([ord(i) for i in word]) for word in words}

    numbers_sum = sum([words_dict[key] for key in words_dict.keys()])
    result = ''
    sorted_dict = {}
    if numbers_sum % 2 == 0:
        sorted_dict = dict(sorted(words_dict.items(), key=lambda x: x[0]))
    else:
        sorted_dict = dict(sorted(words_dict.items(), key=lambda x: -x[1]))

    for key, value in sorted_dict.items():
        result += f'{key} - {value}\n'
    return result

print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))

print(
    words_sorting(
        'cacophony',
        'accolade'
  ))

