file_path = './numbers.txt'

file = open(file_path, 'r')
# result = 0
# for line in file:
#     result += int(line.strip())
#
#
# print(result)

print(sum([int(x.strip()) for x in file]))