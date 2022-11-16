from collections import deque
seats = input().split(", ")
first_numbers = deque(map(int, input().split(", ")))
second_numbers = deque(map(int, input().split(", ")))

rotations = 0
taken_seats = []

while True:
    if rotations == 10:
        break
    if len(taken_seats) == 3:
        break
    first_number = first_numbers.popleft()
    second_number = second_numbers.pop()
    sum_of_both_numbers = first_number + second_number
    ascii_char = chr(sum_of_both_numbers)
    first_concat = str(first_number) + ascii_char
    second_concat = str(second_number) + ascii_char
    for seat in [first_concat, second_concat]:
        if seat in taken_seats:
            break
        if seat in seats:
            seats.remove(seat)
            taken_seats.append(seat)
            break
    else:
        first_numbers.append(first_number)
        second_numbers.appendleft(second_number)
    rotations += 1

print(f"Seat matches: {', '.join(taken_seats)}")
print(f"Rotations count: {rotations}")
