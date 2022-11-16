numbers = int(input())

for i in range(numbers):
    code = int(input())
    if code == 88:
        print("Hello")
    elif code == 86:
        print("How are you?")
    elif code > 88:
        print("Bye.")
    else:
        print("GREAT!")

