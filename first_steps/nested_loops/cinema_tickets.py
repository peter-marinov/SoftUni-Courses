command = input()

students_tickets = 0
standard_tickets = 0
kids_tickets = 0

while command != "Finish":
    # free_places = 100
    current_taken_paces = 0
    free_places = int(input())
    for place in range(0, free_places):
        ticket_type = input()
        if ticket_type == "End":
            break

        if ticket_type == "student":
            students_tickets += 1
            current_taken_paces += 1
        elif ticket_type == "standard":
            standard_tickets += 1
            current_taken_paces += 1
        else: # kids tickets
            kids_tickets += 1
            current_taken_paces += 1

    capacity =  current_taken_paces / free_places * 100
    print(f"{command} - {capacity:.2f}% full.")
    command = input()

total_tickets = students_tickets + standard_tickets + kids_tickets
procentage_students_tickets = students_tickets / total_tickets * 100
procentage_standard_tickets = standard_tickets / total_tickets * 100
procentage_kids_tickets = kids_tickets / total_tickets * 100

print(f"Total tickets: {total_tickets}")
print(f"{procentage_students_tickets:.2f}% student tickets.")
print(f"{procentage_standard_tickets:.2f}% standard tickets.")
print(f"{procentage_kids_tickets:.2f}% kids tickets.")