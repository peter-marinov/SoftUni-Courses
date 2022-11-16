from collections import deque

seats_list = input().split(', ')
first_sequence_deque = deque(map(int, input().split(', ')))
second_sequence_stack = list(map(int, input().split(', ')))

taken_seats = []

rotations = 0

while len(taken_seats) < 3 and rotations < 10:
    found_seat = False
    if len(first_sequence_deque) == 0 or len(second_sequence_stack) == 0:
        break
    searched_seat_letter = chr(first_sequence_deque[0] + second_sequence_stack[-1])
    fist_searched_seat = str(first_sequence_deque[0]) + searched_seat_letter
    second_searched_seat = str(second_sequence_stack[-1]) + searched_seat_letter
    for seat in seats_list:
        if seat in [fist_searched_seat, second_searched_seat]:
            if seat not in taken_seats:
                taken_seats.append(seat)
            first_sequence_deque.popleft()
            second_sequence_stack.pop()
            found_seat = True
            break

    if not found_seat:
        first_sequence_deque.append(first_sequence_deque.popleft())
        second_sequence_stack.insert(0, second_sequence_stack.pop())

    rotations += 1


print(f"Seat matches: {', '.join(taken_seats)}")
print(f"Rotations count: {rotations}")
# print(searched_seat)
# print(seats_list)
# print(first_sequence_deque[1])
# print(second_sequence_stack)
