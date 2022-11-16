import re

number_of_inputs = int(input())

for _ in range(number_of_inputs):
    message = input()
    pattern = r'^([$%])([A-Z][a-z]{2,})\1\:\s\[(\d+)\]\|\[(\d+)\]\|\[(\d+)\]\|$'
    result = re.findall(pattern, message)
    # print(result)
    if result:
        decrypted_msg = chr(int(result[0][2])) + chr(int(result[0][3])) + chr(int(result[0][4]))
        print(f'{result[0][1]}: {decrypted_msg}')
    else:
        print('Valid message not found!')
