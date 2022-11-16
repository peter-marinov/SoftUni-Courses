'''
numbers = input().split('|')

matrix = [numbers[i].strip().split() for i in range(len(numbers))]

for row in range(len(matrix) -1, -1, -1):
    for item in matrix[row]:
        print(item, end=' ')

'''

line = input().split('|')

sub_lists = []
for sub_sting in line[::-1]:
    sub_sting.extend(sub_sting.split())

print(*sub_lists)