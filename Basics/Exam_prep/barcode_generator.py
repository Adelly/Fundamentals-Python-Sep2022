# number = int(input())
# for number_one in range(1, 10): #1111 - 9999 - всяко едно число е отделен цикъл
#     for number_two in range(1, 10):
#         for number_three in range(1, 10):
#             for number_four in range(1, 10):
#                 is_valid = number % number_one == 0 and number % number_two == 0 and number % number_three == 0 and \
#                     number % number_four == 0
#                 if is_valid:
#                     print(f"{number_one}{number_two}{number_three}{number_four}", end = " ")


first_number = int(input())
last_number = int(input())
first_number_str = str(first_number)
last_number_str = str(last_number)

for number_1 in range(int(first_number_str[0]), int(last_number_str[0]) + 1):
    for number_2 in range(int(first_number_str[1]), int(last_number_str[1]) + 1):
        for number_3 in range(int(first_number_str[2]), int(last_number_str[2]) + 1):
            for number_4 in range(int(first_number_str[3]), int(last_number_str[3]) + 1):
                if number_1 % 2 != 0 and number_2 % 2 != 0 and number_3 % 2 != 0 and number_4 % 2 != 0:
                    print(f"{number_1}{number_2}{number_3}{number_4}", end=' ')




# last_digit = start % 10
# start //= 10


