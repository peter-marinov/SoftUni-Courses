target_steps = 10000
steps_done = 0
# is_steps_done = True

while target_steps >= steps_done:
    steps_input = input()
    if steps_input == "Going home":
        steps_input = input()
        steps_done += int(steps_input)
        break

    steps_done += int(steps_input)

difference = abs(target_steps - steps_done)
if target_steps <= steps_done:
    print(f"Goal reached! Good job!")
    print(f"{difference} steps over the goal!")

else:
    print(f"{difference} more steps to reach goal.")

