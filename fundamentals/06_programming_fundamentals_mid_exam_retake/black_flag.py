days_of_pirating = int(input())
plunder_for_a_day = int(input())
expected_plunder = float(input())

current_number_of_plunders = 0

if days_of_pirating >= 1:
    for day in range(1, days_of_pirating + 1):
        current_number_of_plunders += plunder_for_a_day
        if day % 3 == 0:
            current_number_of_plunders += plunder_for_a_day * 0.5
        if day % 5 == 0:
            current_number_of_plunders *= 0.7

if current_number_of_plunders >= expected_plunder:
    print(f"Ahoy! {current_number_of_plunders:.2f} plunder gained.")
else:
    percentage_of_gain_plunders = (current_number_of_plunders / expected_plunder) * 100
    print(f"Collected only {percentage_of_gain_plunders:.2f}% of the plunder.")