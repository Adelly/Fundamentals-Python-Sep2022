width = int(input())
length = int(input())
height = int(input())
space_available = width * length * height
command = input()
is_space_over = False
while command != "Done":
    current_command = int(command)
    space_available -= current_command
    if space_available <= 0:
        is_space_over = True
        break
    command = input()
if is_space_over:
    insufficient = abs(space_available)
    print(f"No more free space! You need {insufficient} Cubic meters more.")
else:
    print(f"{space_available} Cubic meters left.")

