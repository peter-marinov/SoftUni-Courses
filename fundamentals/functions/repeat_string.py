# def repeat_string(string, count):
#     new_string = string * count
#     return new_string
#
# string_input = input()
# count_input = int(input())
#
# print(repeat_string(string_input,count_input))


string_input = input()
count_input = int(input())

repeat_string = lambda string, count: string * count

print(repeat_string(string_input,count_input))
