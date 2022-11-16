# def palindrome(*args):
#     if args[0] == args[0][::-1]:
#         return f'{args[0]} is a palindrome'
#     else:
#         return f'{args[0]} is not a palindrome'

def palindrome(word: str, idx: int):
    if idx == len(word) // 2:
        return f'{word} is a palindrome'

    first, last = word[idx], word[-1 - idx]
    if first != last:
        return f'{word} is not a palindrome'

    idx += 1
    return palindrome(word, idx)

print(palindrome("abcba", 0))
print(palindrome("peter", 0))