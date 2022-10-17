command = input()
best_player = ""
best_player_goals = 0
while command != "END":
    player_name = command
    goals = int(input())
    if goals > best_player_goals:
        best_player_goals = goals
        best_player = player_name
        if goals >= 10:
            break
    command = input()
print(f"{best_player} is the best player!")
if goals >= 3:
    print(f"He has scored {best_player_goals} goals and made a hat-trick !!!")
else:
        print(f"He has scored {best_player_goals} goals.")


# easter_bread_count = int(input())
# best_result_name = ""
# best_points = 0
# for easter_breads in range(1, easter_bread_count + 1):
#     baker_points = 0
#     baker_name = input()
#     command = input()
#     while command != "Stop":
#         points = int(command)
#         baker_points += points
#         command = input()
#     print(f"{baker_name} has {baker_points} points.")
#     if baker_points > best_points:
#         best_points = baker_points
#         best_result_name = baker_name
#         print(f"{baker_name} is the new number 1!")
# print(f"{best_result_name} won competition with {best_points} points!")