from os import path

try:
    file = open('demo.txt')

    print(file)
    print(path.abspath('.'))
except FileNotFoundError:
    print(f'File does not exist')