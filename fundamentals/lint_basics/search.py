numbers = int(input())
word = input()
string_list = []
filtered_string_list = []
for _ in range(numbers):
    current_string = input()
    string_list.append(current_string)

for item in string_list:
    if word in item:
        filtered_string_list.append(item)

print(string_list)
print(filtered_string_list)
