capacity = int(input())
command = input()
capacity_full = 0
discount = 0
while command != "Movie time!":
    people_entering = int(command)
    capacity_full += people_entering
    if people_entering % 3 == 0:
        discount += 5
    if capacity_full >= capacity:
        break
    command = input()
income = 5 * capacity_full - discount
capacity_free = capacity - capacity_full

    print("The cinema is full.")
else:
    print(f"There are {capacity_free} seats left in the cinema.")
print(f"Cinema income - {income} lv.")
