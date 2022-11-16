# version = [int(number) for number in input().split('.')]
#
#
# version[-1] += 1
# for current_index in range((len(version)) - 1, -1, -1):
#     if version[current_index] > 9:
#         version[current_index] = 0
#         # if current_index - 1 >= 0:
#         version[current_index] += 1
#
# print('.'.join(str(number) for number in version))

version = input()
version = version.replace('.', '')
version = int(version) + 1
version_str = str(version)
version_str = version_str[0] + version_str[1:2].replace('', '.') + version_str[2]
print(version_str)