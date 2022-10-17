floors_count = int(input())
rooms = int(input())
floor = ""
for current_floor in range(floors_count, 0, -1):
    for current_room in range(rooms):
        if current_floor == floors_count:
            floor = "L"
        elif current_floor % 2 == 0:
            floor = "O"
        else:
            floor = "A"
        print(f"{floor}{current_floor}{current_room}", end = " ")
    print()