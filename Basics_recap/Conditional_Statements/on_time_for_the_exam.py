exam_hour = int(input())
exam_minutes = int(input())
hour_of_arrival = int(input())
minute_of_arrival = int(input())
exam_time = (exam_hour * 60) + exam_minutes
arrival_time = (hour_of_arrival * 60) + minute_of_arrival
difference = abs(exam_time - arrival_time)
#to get hour:min separately
hour = difference // 60
minutes = difference % 60
if arrival_time > exam_time:
    print("Late")
    if difference < 60:
        print(f"{difference} minutes after the start")
    else:
        if minutes < 10:
            print(f"{hour}:0{minutes} hours after the start")
        else:
            print(f"{hour}:{minutes} hours after the start")
elif arrival_time == exam_time or difference <= 30:
    print("On time")
    if 1 <= difference <= 30:
        print(f"{difference} minutes before the start")
else:
    print("Early")
    if difference < 60:
        print(f"{difference} minutes before the start")
    else:
        if minutes < 10:
            print(f"{hour}:0{minutes} hours before the start")
        else:
            print(f"{hour}:{minutes} hours before the start")