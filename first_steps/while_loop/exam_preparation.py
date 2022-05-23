number_of_bad_degree = int(input())

has_failed = True
failed_times = 0
solved_problems = 0
last_problem = ""
grades_sum = 0

while failed_times < number_of_bad_degree:
    problem_name = input()
    if problem_name == "Enough":
        has_failed = False
        break
    score = int(input())
    if score <= 4:
        failed_times += 1
    solved_problems += 1
    grades_sum += score
    last_problem = problem_name


if not has_failed:
    average_grade = grades_sum / solved_problems
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {solved_problems}")
    print(f"Last problem: {last_problem}")
else:
    print(f"You need a break, {failed_times} poor grades.")