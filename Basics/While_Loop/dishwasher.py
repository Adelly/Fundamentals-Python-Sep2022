bottles = int(input())
detergent = bottles * 750
command = input()
dishes = 0
pots = 0
counter = 0
is_detergent_over = False
while command != "End":
    current_command = int(command)
    counter += 1
    if counter == 3:
        pots += current_command
        detergent -= current_command * 15
        counter = 0
    else:
        dishes += current_command
        detergent -= current_command * 5
    if detergent <= 0:
        is_detergent_over = True
        break
    command = input()
if is_detergent_over:
    insufficient = abs(detergent)
    print(f"Not enough detergent, {insufficient} ml. more necessary!")
else:
    print(f"Detergent was enough!")
    print(f"{dishes} dishes and {pots} pots were washed.")
    print(f"Leftover detergent {detergent} ml.")