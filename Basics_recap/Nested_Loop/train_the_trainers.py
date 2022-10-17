jury_count = int(input())
command = input()
all_grades_sum = 0
grades_count = 0
while command != "Finish":
    presentation_name = command
    grades_sum = 0
    for grades in range(1, jury_count + 1):
        grade = float(input())
        grades_count += 1
        grades_sum += grade
        all_grades_sum += grade
    average_grade_current = grades_sum / jury_count
    print(f"{presentation_name} - {average_grade_current:.2f}.")
    command = input()
all_grades_average = all_grades_sum / grades_count
print(f"Student's final assessment is {all_grades_average:.2f}.")