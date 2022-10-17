number = int(input())
for first_multiplier in range(1, int(str(number)[0]) + 1):
    for second_multiplier in range(1, int(str(number)[1]) + 1):
        for third_multiplier in range(1, int(str(number)[2]) + 1):
            result = first_multiplier * second_multiplier * third_multiplier
        print(f"{first_multiplier} * {second_multiplier} * {third_multiplier} = {result}")



