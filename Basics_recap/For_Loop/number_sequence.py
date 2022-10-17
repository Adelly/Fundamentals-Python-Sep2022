import sys
numbers_count = int(input())
max_number = - sys.maxsize #задава се с обратното число, най-малкото, за да сме сигурни че ще е по-голямо
min_number = sys.maxsize #давам му най-високата възможна стойност

for numbers in range(numbers_count):
    current_number = int(input())
    if current_number > max_number:
        max_number = current_number
    if current_number < min_number:
        min_number = current_number
#if numbers count = 0
#if max_number != max_number, тогава print max number, else не
print(f"Max number: {max_number}")
print(f"Min number: {min_number}")

