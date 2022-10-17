numbers_count = int(input())
left_sum = 0
right_sum = 0
for numbers in range(2 * numbers_count):
    current_number = int(input())
    if numbers < numbers_count: #left sum
        left_sum += current_number
    else: #right sum
        right_sum += current_number
if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    difference = abs(left_sum - right_sum)
    print(f"No, diff = {difference}")


# #може и с 2 фор цикъла
# # for numbers in range (count of numbers):
# current_number = int(input())
# left sum += current_number
#same for the right sum