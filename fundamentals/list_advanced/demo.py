# import timeit
#
# def even_numbers_with_compression():
#     return [num for num in [1, 2, 3, 4, 5, 6]]
#
# def even_numbers_with_loop():
#     even_nums = []
#
#     for num in [1, 2, 3, 4, 5, 6]:
#         if num % 2 == 0:
#             even_nums

# print([x for x in range(5) if x % 2 == 0])
# print(list(range(11)))
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = [num for num in nums if num % 2 ==0 if num > 5 if num !=10]
# print(result)

matrix = [[x for x in range(3)] for y in range(3)]
print(matrix)