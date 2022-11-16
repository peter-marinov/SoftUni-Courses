# number_of_rooms = int(input())
# is_chair_needed = False
# for room in range(1, number_of_rooms + 1):
#     current_room = input().split()
#     if int(current_room[1]) > len(current_room):
#         chairs_needed = int(current_room[1]) - len(current_room)
#         print(f'{chairs_needed} more chairs needed in room {room}')
#         is_chair_needed = True
#     else:
#         if
def check_chairs(number_of_rooms):
    total_free_chairs = 0
    needed_chairs = 0

    for number_of_room in range(1, number_of_rooms + 1):
        free_chairs, visitors = input().split()
        difference = len(free_chairs) - int(visitors)
        # print(difference)
        if difference >= 0:
            total_free_chairs += difference
        else:
            needed_chairs += abs(difference)
            print(f'{abs(difference)} more chairs needed in room {number_of_room}')

    return total_free_chairs, needed_chairs


number_of_rooms = int(input())
total_free_chairs, needed_chairs = check_chairs(number_of_rooms)
if total_free_chairs >= needed_chairs:
    print(f"Game On, {total_free_chairs} free chairs left")
