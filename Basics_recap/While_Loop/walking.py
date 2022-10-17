command = input()
total_steps = 0
while command != "Going home":
    steps = int(command)
    total_steps += steps
    if total_steps >= 10000:
        break
    command = input()
if command == "Going home":
    steps_home = int(input())
    total_steps += steps_home
difference = abs(10000 - total_steps)
if total_steps >= 10000:
    print(f"Goal reached! Good job!")
    print(f"{difference} steps over the goal!")
else:
    print(f"{difference} more steps to reach goal.")
