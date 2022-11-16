def search_for_substring(first_list, second_list):
    match_list = []
    for key_word in first_list:
        for word in second_list:
            if key_word in word:
                if key_word not in match_list:
                    match_list.append(key_word)
    return match_list

first_list = input().split(', ')
second_list = input().split(', ')

print(search_for_substring(first_list, second_list))