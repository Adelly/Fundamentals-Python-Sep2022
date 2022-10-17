time_limit = int(input())
scenes = int(input())
scene_length = int(input())
preparation_time = time_limit * 0.15
time_needed = scenes * scene_length + preparation_time
time_gap = abs(time_limit - time_needed)
if time_needed <= time_limit:
    print(f"You managed to finish the movie on time! You have {round(time_gap)} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {round(time_gap)} minutes.")
