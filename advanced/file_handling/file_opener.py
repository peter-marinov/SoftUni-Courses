file_path = 'text.txt'

try:
    file = open(file_path, 'r')
    print('File found')
    # print(file.read())
    for _ in range(3):
        print(file.read(4))
except FileNotFoundError:
    print('File not found')