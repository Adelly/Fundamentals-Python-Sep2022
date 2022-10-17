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