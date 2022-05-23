jury = int(input())
presentation = input()
presentation_count = 0
total_grade_sum = 0
while presentation != "Finish":
    presentation_count += 1

    average = 0
    grade_sum = 0
    for j in range(0, jury):
        grade = float(input())
        grade_sum += grade
        total_grade_sum += grade
    average = grade_sum / jury
    print(f"{presentation} - {average:.2f}.")
    presentation = input()

total_average = total_grade_sum / (presentation_count * jury)
print(f"Student's final assessment is {total_average:.2f}.")
