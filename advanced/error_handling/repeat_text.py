# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError as error:
#         print("Oops!  That was no valid number.   Try again...")
#         print(error)
#     finally:
#         print("This is always here")


try:
    text = input()
    times = int(input())
    output = text * times
    print(output)
except ValueError:
    print("Variable times must be an integer")
