command = input()
is_Voldemort = False
while command != "Welcome!":
    house = ""
    if command == "Voldemort":
        is_Voldemort = True
        break
    elif len(command) < 5:
        house = "Gryffindor"
    elif len(command) == 5:
        house = "Slytherin"
    elif len(command) == 6:
        house = "Ravenclaw"
    else:
        house = "Hufflepuff"
    print(f"{command} goes to {house}.")
    command = input()
if is_Voldemort:
    print(f"You must not speak of that name!")
else:
    print("Welcome to Hogwarts.")