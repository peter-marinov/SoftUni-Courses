import re

# txt = "The rain in Spain"

# x = re.search("^The.*Spain$", txt)
# x = re.findall("ai", txt)
# print(x)

# text = 'MARIO is python developer at a BioPharmacy, his age is 32'

# result = re.findall(r'Mario', text, re.IGNORECASE)
# result = re.search(r'''(^\w{5}# match 5 letters and
#                         .+(\d{2}$)# match 2 dogot number at the end''',
#                    text, re.X)
# print(result)


# data = ['software', 'developer']
#
# text = 'software is a set of instructions'
#
# for pattern in data:
#     if re.search(pattern, text):
#         print('Found match')
#     else:
#         print('Not match')

data = ['software', 'developer']

text = 'The rain in Spain'

print(re.split('\s', text))