exam_start_hour = int(input())
exam_time_window = int(input())
hour_of_arrival = int(input())
mins_of_arrival = int(input())

time_of_exam = exam_start_hour * 60 + exam_time_window
time_of_arrival = hour_of_arrival * 60 + mins_of_arrival

# print(time_of_exam)
# print(time_of_arrival)

if time_of_arrival > time_of_exam:
    print("Late")
elif time_of_exam - 30 <= time_of_arrival <= time_of_exam:
    print("On time")
else:
    print("Early")

difference = abs(time_of_arrival - time_of_exam)
diff_hours = difference // 60
diff_mins = difference % 60

if time_of_exam - 60 < time_of_arrival < time_of_exam:
    print(f"{diff_mins} minutes before the start")
elif time_of_arrival <= time_of_exam - 60:
    print(f"{diff_hours}:{diff_mins:02d} hours before the start")
elif time_of_exam < time_of_arrival < time_of_exam + 60:
    print(f"{diff_mins} minutes after the start")
elif time_of_arrival >= time_of_exam + 60:
    print(f"{diff_hours}:{diff_mins:02d} hours after the start")