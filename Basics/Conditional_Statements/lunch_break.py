from math import ceil

series = str(input())
episode_length = int(input())
lunch_break = int(input())
lunch_time = lunch_break * 1/8
break_time = lunch_break * 1/4
time_needed = break_time + lunch_time + episode_length
if time_needed <= lunch_break:
    print(f"You have enough time to watch {series} and left with {ceil(lunch_break - time_needed):.0f} minutes free time.")
else:
    print(f"You don't have enough time to watch {series}, you need {ceil(time_needed - lunch_break):.0f} more minutes.")