student_name = input()

year = 1
sum = 0
fail_cnt = 0
while year <= 12:
    if fail_cnt > 1:
        break

    grade = float(input())
    if grade < 4:
        fail_cnt += 1
        continue

    sum += grade
    year += 1

if fail_cnt > 1:
    print(f"{student_name} has been excluded at {year} grade")
else:
    average_grade = sum / 12
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")

# bad_degree = 0
# score_num = 0
#
# while bad_degree > 1:
#     score = float(input())
#     # if score < 4:
#     #     bad_degree += 1
#     score_num += 1


# {име на ученика} graduated. Average grade: {средната оценка от цялото обучение}
# В случай, че ученикът е изключен от училище, да се отпечата:
# {име на ученика} has been excluded at {класа, в който е бил изключен} grade