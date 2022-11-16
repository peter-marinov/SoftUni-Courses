number=int(input())
new_list=[]
i=0

while 0<number:

    i+=1
    shell=2*i**2

    if number >= shell:  # проверка дали има място за максималния капацитет
        new_list.append(shell)
        number -= shell
    else:                # ако няма попълваме колкото е останало
        new_list.append(number)
        number = 0

print(new_list)