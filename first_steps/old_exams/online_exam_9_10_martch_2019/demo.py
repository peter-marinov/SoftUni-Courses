target_high = int(input())

jumps_count = 0
current_target_high = target_high - 30
fail_counter = 0
target_is_not_achieved = False
while not target_is_not_achieved:
    current_jump_high = int(input())
    jumps_count += 1

    if current_jump_high <= current_target_high:
        fail_counter += 1
        if fail_counter == 3:
            target_is_not_achieved = True
            # break
    else:
        if current_target_high >= target_high:
            # target_is_achieved = True
            break
        current_target_high += 5
        fail_counter = 0

if not target_is_not_achieved:
    print(f"Tihomir succeeded, he jumped over {current_target_high}cm after {jumps_count} jumps.")
else:
    print(f"Tihomir failed at {current_target_high}cm after {jumps_count} jumps.")