people_in_fitness = int(input())

back_cnt = 0
chest_cnt = 0
legs_cnt = 0
abs_cnt = 0
protein_shake_cnt = 0
protein_bar_cnt = 0

for person in range(1, people_in_fitness + 1):
    type_of_train = input()
    if type_of_train == "Back":
        back_cnt += 1
    elif type_of_train == "Chest":
        chest_cnt += 1
    elif type_of_train == "Legs":
        legs_cnt += 1
    elif type_of_train == "Abs":
        abs_cnt += 1
    elif type_of_train == "Protein shake":
        protein_shake_cnt += 1
    elif type_of_train == "Protein bar":
        protein_bar_cnt += 1

percent_training_people = (back_cnt + chest_cnt + legs_cnt + abs_cnt) / people_in_fitness * 100
percent_protein_people = (protein_bar_cnt + protein_shake_cnt) / people_in_fitness * 100
print(f"{back_cnt} - back")
print(f"{chest_cnt} - chest")
print(f"{legs_cnt} - legs")
print(f"{abs_cnt} - abs")
print(f"{protein_shake_cnt} - protein shake")
print(f"{protein_bar_cnt} - protein bar")
print(f"{percent_training_people:.2f}% - work out")
print(f"{percent_protein_people:.2f}% - protein")