length = int(input())
width = int(input())
pieces = length * width
command = input()
is_cake_enough = True
while command != "STOP":
    current_command = int(command)
    pieces -= current_command
    if pieces <= 0:
        is_cake_enough = False
        break
    command = input()
if is_cake_enough:
    print(f"{pieces} pieces are left.")
else:
    insufficient = abs(pieces)
    print(f"No more cake left! You need {insufficient} pieces more.")
