def check_if_palindrome(list):
    for number in list:
        if number == number[::-1]:
            print(True)
        else:
            print(False)

numbers_list = list(input().split(', '))
check_if_palindrome(numbers_list)

