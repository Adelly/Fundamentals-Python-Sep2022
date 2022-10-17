from math import floor
tv_show = input()
seasons = int(input())
episodes = int(input())
length = float(input())
ads = length * 0.20
season_finale_extra_time = seasons * 10
total_time = (length + ads) * seasons * episodes + season_finale_extra_time
print(f"Total time needed to watch the {tv_show} series is {floor(total_time)} minutes.")
#instead of floor we can use int