number_of_groups = int(input())

musala = 0
monblan = 0
kilimandjaro = 0
k2 = 0
everest = 0
number_of_people = 0

for i in range(1, number_of_groups + 1):
    people_in_group = int(input())
    number_of_people += people_in_group
    if people_in_group <= 5:
        musala += people_in_group
    elif people_in_group <= 12:
        monblan += people_in_group
    elif people_in_group <= 25:
        kilimandjaro += people_in_group
    elif people_in_group <= 40:
        k2 += people_in_group
    else:
        everest += people_in_group
# print(musala)
# print(monblan)
# print(kilimandjaro)
# print(k2)
# print(everest)
# print(number_of_people)
musala_procent = musala / number_of_people * 100
monblan_procent = monblan / number_of_people * 100
kilimandjaro_procent = kilimandjaro / number_of_people * 100
k2_procent = k2 / number_of_people * 100
everest_procent = everest / number_of_people * 100

print(f"{musala_procent:.2f}%")
print(f"{monblan_procent:.2f}%")
print(f"{kilimandjaro_procent:.2f}%")
print(f"{k2_procent:.2f}%")
print(f"{everest_procent:.2f}%")

