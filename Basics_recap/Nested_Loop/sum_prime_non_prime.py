command = input()
prime_sum = 0
non_prime_sum = 0
while command != "stop":
    current_command = int(command)
    if current_command < 0:
        print(f"Number is negative.")
        command = input()
        continue
    count = 0
    for number in range(1, current_command + 1):
        if current_command % number == 0:
            count += 1
    if count == 2:
        prime_sum += current_command
    else:
        non_prime_sum += current_command
    command = input()
print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")