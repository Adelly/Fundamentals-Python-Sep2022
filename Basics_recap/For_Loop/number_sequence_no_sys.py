numbers_count = int(input())
current_number = int(input())
max_number = current_number
min_number = current_number
# защото 1вото въведено число е най-малко и най-голямо
# този вариант на кода няма да е много верен ако въведем 0 за numbers count
for numbers in range(numbers_count - 1):
    current_number = int(input())
    if current_number > max_number:
        max_number = current_number
    if current_number < min_number:
        min_number = current_number
print(f"Max number: {max_number}")
print(f"Min number: {min_number}")