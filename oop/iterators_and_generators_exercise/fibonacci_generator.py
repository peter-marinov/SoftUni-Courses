def fibonacci():
    first_number = 0
    second_number = 1
    yield first_number
    yield second_number

    while True:
        result = first_number + second_number
        yield result
        first_number, second_number = second_number, result

    # previous_number = -1
    # current_number = 0
    # while True:
    #     yield current_number
    #     if current_number == 0:
    #         previous_number = 0
    #         current_number = 1
    #     else:
    #         current_number_remember = current_number
    #         current_number = current_number + previous_number
    #         previous_number = current_number_remember

generator = fibonacci()
for i in range(5):
    print(next(generator))