from collections import deque


def find_match(flowers_dict, flower, letter):
    if letter in flowers_dict[flower]:
        flowers_dict[flower][letter] = True
        # if letter not in letter_collection:
        #     letter_collection.append(letter)

    return flowers_dict


vowels_deque = deque(input().split())
consonants_stack = list(input().split())

words_dict = {
    'rose': {},
    'tulip': {},
    'lotus': {},
    'daffodil': {}
}

# vowels_collection = []
# consonants_collection = []
word_found = False

for key in words_dict.keys():
    words_dict[key] = {letter: False for letter in key}


while vowels_deque and consonants_stack:
    # Todo exit when a word is found
    first_vowels = vowels_deque.popleft()
    last_consonants = consonants_stack.pop()
    for key in words_dict.keys():
        words_dict = find_match(words_dict, key, first_vowels)
        words_dict = find_match(words_dict, key, last_consonants)

        if all(value is True for value in words_dict[key].values()):
            print(f'Word found: {key}')
            word_found = True
            break

    if word_found:
        break

if not word_found:
    print('Cannot find any word!')

if vowels_deque:
    print(f"Vowels left: {' '.join(vowels_deque)}")
if consonants_stack:
    print(f"Consonants left: {' '.join(consonants_stack)}")
