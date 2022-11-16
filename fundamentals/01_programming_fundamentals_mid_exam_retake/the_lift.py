number_of_waiting_people = int(input())
wagon_status = list(map(int, input().split()))

for index, current_wagon_capacity in enumerate(wagon_status):
    if current_wagon_capacity < 4:
        people_can_go = 4 - current_wagon_capacity
        # print(people_can_go)
        # print(number_of_waiting_people)
        if number_of_waiting_people < people_can_go:
            people_can_go = number_of_waiting_people
        number_of_waiting_people -= people_can_go
        wagon_status[index] += people_can_go

if True in [empty_space < 4 for empty_space in wagon_status]:
    is_empty_space = True
else:
    is_empty_space = False
# wagon_current_status =
# print(wagon_current_status)
# print(number_of_waiting_people)

if number_of_waiting_people == 0 and is_empty_space:
    print(f"The lift has empty spots!")
    print(" ".join([str(wagon) for wagon in wagon_status]))
    #
elif number_of_waiting_people > 0 and not is_empty_space:
    print(f"There isn't enough space! {number_of_waiting_people} people in a queue!")
    print(" ".join([str(wagon) for wagon in wagon_status]))
else:
    print(" ".join([str(wagon) for wagon in wagon_status]))