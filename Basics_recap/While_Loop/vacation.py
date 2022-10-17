money_needed = float(input())
money_available = float(input())
days_counter = 0
spend_counter = 0
is_money_enough = False
while money_needed > money_available:
    action = input()
    sum = float(input())
    days_counter += 1
    if action == "spend":
        money_available -= sum
        if money_available < 0:
            money_available = 0
        spend_counter += 1
        if spend_counter == 5:
            break
    elif action == "save":
        money_available += sum
        spend_counter = 0
        if money_available >= money_needed:
            is_money_enough = True
            break
if is_money_enough:
    print(f"You saved the money for {days_counter} days.")
else:
    print(f"You can't save the money.")
    print(f"{days_counter}"

