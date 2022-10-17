import sys
numbers_count = int(input())
numbers_sum = 0
max_number = -sys.maxsize
for numbers in range(1, numbers_count + 1):
    current_number = int(input())
    numbers_sum += current_number
    if current_number > max_number:
        max_number = current_number
sum_of_the_rest = numbers_sum - max_number
if sum_of_the_rest == max_number:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    difference = abs(sum_of_the_rest - max_number)
    print("No")
    print(f"Diff = {difference}")
