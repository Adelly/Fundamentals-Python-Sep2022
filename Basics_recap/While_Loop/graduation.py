# name = input()
# current_class = 1
# bad_grades = 0
# grades_sum = 0
# is_excluded = False
# while current_class <= 12:
#     current_grade = float(input())
#     if current_grade < 4:
#         bad_grades += 1
#         # grades_sum += current_grade ? in case we only have 1 grade < 4 why we are not adding to the total sum?
#         if bad_grades == 2:
#             is_excluded = True
#             break
#     else:
#         current_class += 1
#         grades_sum += current_grade
# if is_excluded:
#     print(f"{name} has been excluded at {current_class} grade")
# else:
#     average_grade = grades_sum / 12
#     print(f"{name} graduated. Average grade: {average_grade:.2f}")


name = input()
current_class = 1
bad_grades = 0
grades_sum = 0
is_excluded = False
while current_class <= 12:
    current_grade = float(input())
    if current_grade < 4:
        bad_grades += 1
        # grades_sum += current_grade ? in case we only have 1 grade < 4 why we are not adding to the total sum?
        if bad_grades == 2:
            is_excluded = True
            break
        continue
    current_class += 1
    grades_sum += current_grade
if is_excluded:
    print(f"{name} has been excluded at {current_class} grade")
else:
    average_grade = grades_sum / 12
    print(f"{name} graduated. Average grade: {average_grade:.2f}")
