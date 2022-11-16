import re

line = input()

pattern = '\d+'
numbers_list = []
while True:
    if line:
        match = re.findall(pattern, line)
        if match:
            numbers_list += match
    else:
        break
    line = input()

print(' '.join(numbers_list))