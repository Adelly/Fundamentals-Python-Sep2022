tabs = int(input())
salary = int(input())
fine = 0
for tab in range(1, tabs + 1):
    current_tab = str(input())
    if current_tab == "Facebook":
        fine += 150
    elif current_tab == "Instagram":
        fine += 100
    elif current_tab == "Reddit":
        fine += 50
if salary > fine:
    remaining = salary - fine
    print(remaining)
else:
    print(f"You have lost your salary.")


