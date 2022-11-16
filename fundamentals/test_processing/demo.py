# a = "Test Example"
# print(a[-1])
# print(a[-2:])
# print(a[-7:])
# print(a[slice(0, 5)])

# a = " example "
# print(a.upper())
# print(a.strip())
# print(a.lstrip())
# print(a.rstrip())

# a = "This is text example example example example"
# print(a.replace('text', 'SoftUni'))
# print(a.replace('example', ''))
# print(a.replace('example', '', 1))
# print(a.replace('example', '', 2))

def multiline_input(text):
    print(text)
    multiline_input = ''

    while True:
        string = input()
        if string != '':
            multiline_input += string + "\n"
        else:
            break
    return multiline_input

print(multiline_input('Please enter your input: '))

