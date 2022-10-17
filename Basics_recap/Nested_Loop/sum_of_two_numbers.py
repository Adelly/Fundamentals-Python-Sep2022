start = int(input())
finish = int(input())
magic_number = int(input())
combination_found = False
combination_counter = 0
for first_number in range(start, finish + 1):
    for second_number in range(start, finish + 1):
        combination_counter += 1
        if first_number + second_number == magic_number:
            combination_found = True
            break
    if combination_found:
        break
if combination_found:
    print(f"Combination N:{combination_counter} ({first_number} + {second_number} = {magic_number})")
else:
    print(f"{combination_counter} combinations - neither equals {magic_number}")

