from math import ceil

number_of_students = int(input())
total_number_of_lectures = int(input())
additional_bonus = int(input())
students_bonus_list = []
students_lectures_list = []

for student in range(number_of_students):
    student_attendances = int(input())
    total_bonus = student_attendances / total_number_of_lectures * (5 + additional_bonus)
    students_bonus_list.append(total_bonus)
    students_lectures_list.append(student_attendances)

if students_bonus_list:
    student_highest_score_index = students_bonus_list.index(max(students_bonus_list))

    print(f"Max Bonus: {ceil(students_bonus_list[student_highest_score_index])}.")
    print(f"The student has attended {students_lectures_list[student_highest_score_index]} lectures.")
else:
    print(f"Max Bonus: 0.")
    print(f"The student has attended 0 lectures.")