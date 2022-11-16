string = ''

while string != "End":
    string = input()
    if string == "End":
        break
    if string != "SoftUni":
        # for letter in string:
        for letter in range(len(string)):
            # print(letter)
            print(2*string[letter], end="")
        print('', end='\n')