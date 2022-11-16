def receiving_exams_passwords(exams_passwords_dict):
    while True:
        command = input().split(':')
        if command[0] == 'end of contests':
            break
        contest, password = command
        exams_passwords_dict[contest] = password
    return exams_passwords_dict


def add_contest(exams_passwords_dict, students_dict):
    while True:
        command = input().split('=>')
        if command[0] == 'end of submissions':
            break
        contest, password, username, points = command[0], command[1], command[2], int(command[3])
        if contest in exams_passwords_dict.keys() and password == exams_passwords_dict[contest]:
            if username not in students_dict.keys():
                students_dict[username] = {}
            if contest not in students_dict[username].keys():
                students_dict[username][contest] = points
            else:
                if students_dict[username][contest] < points:
                    students_dict[username][contest] = points
    return students_dict


def students_sorted(students_dict):
    # print(students_dict)
    students_ranking_dict = {}
    sorted_dict = {}
    for student in students_dict.keys():
        total_score = 0
        sorted_dict[student] = dict(sorted(students_dict[student].items(), key=lambda item: item[1], reverse=True))
        for contest in students_dict[student].keys():
            total_score += students_dict[student][contest]
        students_ranking_dict[student] = total_score

    # print(sorted_dict)
    # print(students_ranking_dict)
    best_user = list(students_ranking_dict.keys())[0]
    print(f"Best candidate is {best_user} with total {students_ranking_dict[best_user]} points.")
    print('Ranking:')
    for user in students_ranking_dict.keys():
        if user != best_user:
            print(f'{user}')
            for contest in sorted_dict[user]:
                print(f"#  {contest} -> {sorted_dict[user][contest]}")
    print(f'{best_user}')
    for contest in sorted_dict[best_user]:
        print(f"#  {contest} -> {sorted_dict[best_user][contest]}")






def ranking():
    exams_passwords_dict = {}
    students_dict = {}

    exams_passwords_dict = receiving_exams_passwords(exams_passwords_dict)
    students_dict = add_contest(exams_passwords_dict, students_dict)

    students_sorted(students_dict)


ranking()
