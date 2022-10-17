from math import floor
tournaments_count = int(input())
starting_points = int(input())
total_points = starting_points
tournaments_won = 0
for tournaments in range(1, tournaments_count + 1):
    stage = str(input())
    if stage == "W":
        total_points += 2000
        tournaments_won += 1
    elif stage == "F":
        total_points += 1200
    elif stage == "SF":
        total_points += 720
average_points_per_tournament = (total_points - starting_points) / tournaments_count
percentage_wins = tournaments_won / tournaments_count * 100
print(f"Final points: {floor(total_points)}")
print(f"Average points: {floor(average_points_per_tournament)}")
print(f"{percentage_wins:.2f}%")
