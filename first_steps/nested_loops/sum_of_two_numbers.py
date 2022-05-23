start = int(input())
end = int(input())
magic_num = int(input())

combination = 0
flag = False
for i in range(start, end + 1):
    for j in range(start, end + 1):
        combination += 1
        sum = i + j
        if sum == magic_num:
            print(f"Combination N:{combination} ({i} + {j} = {sum})")
            flag = True
            break
    if flag:
        break

if flag == False:
    print(f"{combination} combinations - neither equals {magic_num}")
# print(f"Combination N:{пореден номер} ({първото число} + {второ число} = {магическото число})")
#