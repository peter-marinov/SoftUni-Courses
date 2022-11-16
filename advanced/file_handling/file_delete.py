from os import remove
file_path = './my_first_file.txt'

try:
    remove(file_path)
except FileNotFoundError:
    print('File already deleted!')
