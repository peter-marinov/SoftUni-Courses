control_mins = int(input())
control_sec = int(input())
trace_length = float(input())
time_for_100_m = int(input())

control_total_time = control_mins * 60 + control_sec
delay_time = (trace_length / 120) * 2.5
martin_time = (trace_length / 100) * time_for_100_m - delay_time

needed_time = abs(control_total_time - martin_time)
if martin_time <= control_total_time:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {martin_time:.3f}.")
else:
    print(f"No, Marin failed! He was {needed_time:.3f} second slower.")