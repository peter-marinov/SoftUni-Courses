exam_results_dict = {}
language_attempts_dict = {}

while True:
    command = input().split("-")
    if command[0] == "exam finished":
        break
    elif len(command) == 2: # banned student
        student = command[0]
        # print(exam_results_dict)
        del exam_results_dict[student]
    else:
        student, language, score = command[0], command[1], int(command[2])
        if student not in exam_results_dict.keys():
            exam_results_dict[student] = {}
            exam_results_dict[student][language] = [0, 0]
        else:
            if language not in exam_results_dict[student].keys():
                exam_results_dict[student][language] = [0, 0]
        # adding submissions
        exam_results_dict[student][language][0] += 1
        if exam_results_dict[student][language][1] < score:
            exam_results_dict[student][language][1] = score

        if language not in language_attempts_dict.keys():
            language_attempts_dict[language] = 0
        language_attempts_dict[language] += 1

# print(exam_results_dict)
# print(language_attempts_dict)
print("Results:")
for user in exam_results_dict.keys():
    for programming_result in exam_results_dict[user].values():
        print(f"{user} | {programming_result[1]}")
print("Submissions:")
for programing_language in language_attempts_dict:
    print(f"{programing_language} - {language_attempts_dict[programing_language]}")