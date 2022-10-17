number = int(input())
for number_one in range(1, 10): #1111 - 9999 - всяко едно число е отделен цикъл
    for number_two in range(1, 10):
        for number_three in range(1, 10):
            for number_four in range(1, 10):
                is_valid = number % number_one == 0 and number % number_two == 0 and number % number_three == 0 and \
                    number % number_four == 0
                if is_valid:
                    print(f"{number_one}{number_two}{number_three}{number_four}", end = " ")
