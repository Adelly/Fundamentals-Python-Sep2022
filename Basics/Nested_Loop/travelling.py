destination = input()
while destination != "End":
    money_needed = float(input())
    money_available = 0
    while money_available < money_needed:
        current_money = float(input())
        money_available += current_money
    print(f"Going to {destination}!")
    destination = input()