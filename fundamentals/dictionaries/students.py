def print_students(std_dict, std_course):
    print('\n'.join(std_dict[std_course]))

students_dict = {}

while True:
    command = input()
    if ':' not in command:
        command = ' '.join(command.split('_'))
        print_students(students_dict, command)
        break

    name, id, course = command.split(':')
    if course in students_dict:
        students_dict[course].append(f'{name} - {id}')
    else:
        students_dict[course] = [f'{name} - {id}']


