from design_patterns.command.add_command import AddCommand

nums = [1, 2, 3, 4, 5]



command, *others = input().split()
if command == 'sum':
    print(sum(nums))
elif command == 'add':
    cmd = AddCommand(nums)
    cmd.execute(*others)
    nums.append(int(others[0]))
elif command == 'remove':
    num_to_remove = int(others[0])
    nums.remove(num_to_remove)