high = int(input())

target = high - 30
error_count = 0
jumps_count = 0
jump_is_successful = False
while True:
    jump_try = int(input())
    jumps_count += 1
    if jump_try > high:
        jump_is_successful = True
        break
    elif jump_try > target:
        if target >= high:
            break
        target += 5
        error_count = 0
    else:
        error_count += 1
        if error_count == 3:
            break



if jump_is_successful:
    print(f"Tihomir succeeded, he jumped over {target}cm after {jumps_count} jumps.")
else:
    print(f"Tihomir failed at {target}cm after {jumps_count} jumps.")
