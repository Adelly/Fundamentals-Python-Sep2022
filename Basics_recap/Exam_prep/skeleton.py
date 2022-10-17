minutes_control = int(input())
seconds_control = int(input())
length_m = float(input())
seconds_for_100_m = int(input())
control_in_seconds = minutes_control * 60 + seconds_control
time_reduced_in_sec = length_m / 120 * 2.5
competitor_time = length_m / 100 * seconds_for_100_m - time_reduced_in_sec
if competitor_time <= control_in_seconds:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {competitor_time:.3f}.")
else:
    difference = competitor_time - control_in_seconds
    print(f"No, Marin failed! He was {difference:.3f} second slower.")