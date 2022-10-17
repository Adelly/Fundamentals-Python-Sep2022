first_number = int(input())
second_number = int(input())
for number in range(first_number, second_number + 1):
    current_number = str(number)
    even = 0
    odd = 0
    for index, digit in enumerate(current_number):
        if index % 2 == 0:
            even += int(digit)
        else:
            odd += int(digit)
    if even == odd:
        print(number, end=" ")
