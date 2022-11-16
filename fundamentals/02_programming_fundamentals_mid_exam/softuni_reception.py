from math import ceil

first_employee_students = int(input())
second_employee_students = int(input())
third_employee_students = int(input())
number_of_students = int(input())

needed_time = 0
number_of_students_per_hour = first_employee_students + second_employee_students + third_employee_students
# if number_of_students > 0:
#     needed_time = ceil(number_of_students / number_of_students_per_hour)
#     # every fourth hour all employees have a 1 hour break
#     break_hours = needed_time // 4
#     print(break_hours)
#     needed_time += break_hours

while number_of_students > 0:
    number_of_students -= number_of_students_per_hour
    needed_time += 1
    if needed_time % 4 == 0:
        needed_time +=1

print(f"Time needed: {needed_time}h.")