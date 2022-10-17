numbers_count = int(input())  #колко числа ще ни въвеждат от конзолата
numbers_sum = 0
for numbers in range(numbers_count): #numbers_count ще стартира от 0; алтернатива - for numbers in range(1, numbers_count + 1)
    current_number = int(input())
    numbers_sum += current_number
print(numbers_sum)