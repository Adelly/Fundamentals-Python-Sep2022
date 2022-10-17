numbers_count = int(input())
odd_sum = 0
even_sum = 0
for position in range(1, numbers_count + 1):
    current_number = int(input())
    if position % 2 == 0: #even
        even_sum += current_number
    else: #odd
        odd_sum += current_number
if even_sum == odd_sum:
    print("Yes")
    print(f"Sum = {even_sum}")
else:
    difference = abs(odd_sum - even_sum)
    print("No")
    print(f"Diff = {difference}")