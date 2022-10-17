actors_budget = float(input())
command = input()
budget_remaining = actors_budget
is_money_over = False
while command != "ACTION":
    actor = command
    length = len(actor)
    if length > 15:
        salary = 0.20 * budget_remaining
    else:
        salary = float(input())
    budget_remaining -= salary
    if budget_remaining < 0:
        is_money_over = True
        break
    command = input()
budget_remaining = abs(budget_remaining)
if is_money_over:
    print(f"We need {budget_remaining:.2f} leva for our actors.")
else:
    print(f"We are left with {budget_remaining:.2f} leva.")



