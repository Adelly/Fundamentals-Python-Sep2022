easter_bread_count = int(input())
best_result_name = ""
best_points = 0
for easter_breads in range(1, easter_bread_count + 1):
    baker_points = 0
    baker_name = input()
    command = input()
    while command != "Stop":
        points = int(command)
        baker_points += points
        command = input()
    print(f"{baker_name} has {baker_points} points.")
    if baker_points > best_points:
        best_points = baker_points
        best_result_name = baker_name
        print(f"{baker_name} is the new number 1!")
print(f"{best_result_name} won competition with {best_points} points!")
