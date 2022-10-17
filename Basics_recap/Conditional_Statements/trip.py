budget = float(input())
season = input()
destination = ""
expenses = 0
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        expenses = budget * 0.70
    elif season == "winter":
        expenses = budget * 0.30
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        expenses = budget * 0.60
    elif season == "winter":
        expenses = budget * 0.20
elif budget > 1000:
    destination = "Europe"
    expenses = budget * 0.10
if season == "winter" or destination == "Europe":
    vacation_place = "Hotel"
else:
    vacation_place = "Camp"
money_spent = abs(budget - expenses)
print(f"Somewhere in {destination}")
print(f"{vacation_place} - {money_spent:.2f}")
