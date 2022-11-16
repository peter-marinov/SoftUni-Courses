def palindrome_filter(word):
    if word == word[::-1]:
        return word

words = input().split()

palindrome_word = input()

palindrome_list = [word for word in words if palindrome_filter(word)]
print(palindrome_list)
print(f'Found palindrome {palindrome_list.count(palindrome_word)} times')

