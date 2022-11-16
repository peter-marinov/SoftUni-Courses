import re

number_of_barcodes = int(input())

pattern = r'@#+([A-Z][a-zA-Z0-9]{4,}[A-Z])@#+'

for _ in range(number_of_barcodes):
    barcode = input()
    result = re.findall(pattern, barcode)
    if result:
        group = ''
        for character in result[0]:
            if character.isdigit():
                group += character
        # if there is no number found the barcode is 00
        if len(group) == 0:
            group = '00'
        print(f'Product group: {group}')
    else:
        print('Invalid barcode')
