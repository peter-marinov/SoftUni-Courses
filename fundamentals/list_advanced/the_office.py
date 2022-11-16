employees_happiness = list(map(int, input().split()))
add_happiness = int(input())
employees_happiness = [employee * add_happiness for employee in employees_happiness]
average_happiness = sum(employees_happiness) / len(employees_happiness)
# print(average_happiness)
# print(employees_happiness)
number_happy_employees = len([person_happiness for person_happiness in employees_happiness if person_happiness > average_happiness])
# print(number_happy_employees)

if number_happy_employees >= len(employees_happiness)/2:
    print(f"Score: {number_happy_employees}/{len(employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {number_happy_employees}/{len(employees_happiness)}. Employees are not happy!")
