budget = int(input())
command = input()
is_budget_enough = True
while command != "End":
    product_price = int(command)
    budget -= product_price
    if budget < 0:
        print(f"You went in overdraft!")
        is_budget_enough = False
        break
    command = input()
if is_budget_enough:
    print(f"You bought everything needed.")
