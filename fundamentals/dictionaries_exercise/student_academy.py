academy_dict = {}

number_of_students = int(input())

for _ in range(number_of_students):
    student_name = input()
    student_grade = float(input())

    if student_name not in academy_dict:
        academy_dict[student_name] = []
    academy_dict[student_name].append(student_grade)

for student in academy_dict.keys():
    student_average_grade = sum(academy_dict[student]) / len(academy_dict[student])
    if student_average_grade >= 4.50:
        print(f"{student} -> {student_average_grade:.2f}")