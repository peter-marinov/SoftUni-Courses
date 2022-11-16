courses_dict_dict = {}

while True:
    command = input().split(" : ")
    if command[0] == "end":
        break

    course, student = command
    if course not in courses_dict_dict.keys():
        courses_dict_dict[course] = []
    courses_dict_dict[course].append(student)

for current_course in courses_dict_dict.keys():
    print(f"{current_course}: {len(courses_dict_dict[current_course])}")
    [print(f"-- {student_name}") for student_name in courses_dict_dict[current_course]]
