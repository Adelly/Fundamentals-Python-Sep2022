first_number = int(input())
second_number = int(input())
operator = input()
result = 0
number_type = ""
is_divided_by_zero = False
if operator == "+":
    result = first_number + second_number
elif operator == "-":
    result = first_number - second_number
elif operator == "*":
    result = first_number * second_number
elif operator == "/":
    if second_number == 0:
        is_divided_by_zero = True
    else:
        result = first_number / second_number
elif operator == "%":
    if second_number == 0:
        is_divided_by_zero = True
    else:
        result = first_number % second_number
if result % 2 == 0:
    number_type = "even"
else:
    number_type = "odd"
if is_divided_by_zero:
    print(f"Cannot divide {first_number} by zero")
elif operator == "+" or operator == "-" or operator == "*":
    print(f"{first_number} {operator} {second_number} = {result} - {number_type}")
elif operator == "/":
    print(f"{first_number} / {second_number} = {result:.2f}")
elif operator == "%":
    print(f"{first_number} % {second_number} = {result}")
