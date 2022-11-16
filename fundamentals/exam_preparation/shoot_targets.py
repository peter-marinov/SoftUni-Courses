targets_to_shoot = list(map(int, input().split(" ")))
print(targets_to_shoot)
shoots_count = 0

while True:
    command = input()

    if command == 'End':
        print(f"Shot targets: {shoots_count} -> {' '.join([str(num) for num in targets_to_shoot])}")
        # print(f"Shot targets: {shoots_count} ->")
        break

    index_shoot = int(command)
    if 0 <= index_shoot <= len(targets_to_shoot):
        for target_index in range(len(targets_to_shoot)):
            if index_shoot == target_index and targets_to_shoot[target_index] != -1:
                for target_reduce_increase_index in range(len(targets_to_shoot)):
                    if targets_to_shoot[target_reduce_increase_index] > targets_to_shoot[target_index]:
                        print(targets_to_shoot[target_reduce_increase_index], targets_to_shoot[target_index])
                        targets_to_shoot[target_reduce_increase_index] -= targets_to_shoot[target_index]
                    else:
                        targets_to_shoot[target_reduce_increase_index] += targets_to_shoot[target_index]
                shoots_count += 1
                targets_to_shoot[target_index] = -1
                print(targets_to_shoot)

                break


