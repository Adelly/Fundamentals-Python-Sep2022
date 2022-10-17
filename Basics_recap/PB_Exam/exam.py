students_count = int(input())
group_one = 0       #grade_above_5
group_two = 0       # grade_4_to_5
group_three = 0     # grade_3_to_4
group_four = 0      # grade_below_3
grades_sum = 0
for student in range(1, students_count + 1):
    grade = float(input())
    if grade >= 5:
        group_one += 1
        grades_sum += grade
    elif 4 <= grade <= 4.99:
        group_two += 1
        grades_sum += grade
    elif 3 <= grade <= 3.99:
        group_three += 1
        grades_sum += grade
    elif 2 <= grade <= 2.99:
        group_four += 1
        grades_sum += grade
percentage_group_one = group_one /students_count * 100
percentage_group_two = group_two /students_count * 100
percentage_group_three = group_three /students_count * 100
percentage_group_four = group_four /students_count * 100
average_grade = grades_sum / students_count
print(f"Top students: {percentage_group_one:.2f}%")
print(f"Between 4.00 and 4.99: {percentage_group_two:.2f}%")
print(f"Between 3.00 and 3.99: {percentage_group_three:.2f}%")
print(f"Fail: {percentage_group_four:.2f}%")
print(f"Average: {average_grade:.2f}")