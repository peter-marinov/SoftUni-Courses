number = int(input())

nothing_is_found = True
sum = 0
power = 0
for a in range(1, 9):
    for b in range(9, a, -1):
        for c in range(0, 9):
            for d in range(9, c, -1):
                sum = a + b + c + d
                power = a * b * c * d
                # if a == 1 and b == 9 and c == 1 and d == 8:
                    # print(power)
                    # print(sum)
                    # print(power//sum)
                    # print(number % 3)
                if sum == power and number % 10 == 5:
                    print(f"{a}{b}{c}{d}")
                    nothing_is_found = False
                    exit()
                if power // sum == 3 and number % 3 == 0:
                    print(f"{d}{c}{b}{a}")
                    nothing_is_found = False
                    exit()

if nothing_is_found == True:
    print(f"Nothing found")

                # if a == 1 and b == 9 and c == 1 and d == 8:
                #     sum = a + b + c + d
                #     print(sum)
                #     power = a * b * c * d
                #     print(power)
                # if sum == power and number % 10 == 5:
                #     print(f"{a}{b}{c}{d}")

                # print(f"{a}{b}{c}{d}")