bad_grades = int(input())
task_name = input()
last_task = ""
bad_grades_count = 0
grades_sum = 0
task_count = 0
while task_name != "Enough":
    last_task = task_name
    current_grade = int(input())
    if current_grade <= 4:
        bad_grades_count += 1
    grades_sum += current_grade
    task_count += 1
    if bad_grades_count >= bad_grades:
        break
    task_name = input()
if bad_grades_count >= bad_grades:
    print(f"You need a break, {bad_grades_count} poor grades.")
else:
    average_score = grades_sum / task_count
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {task_count}")
    print(f"Last problem: {last_task}")
