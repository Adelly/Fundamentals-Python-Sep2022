budget = int(input())
season = input()
fisherman_count = int(input())
price_for_rent = 0
if season == "Spring":
    if fisherman_count <= 6:
        price_for_rent = 3000 * 0.90
    elif 7 < fisherman_count <= 11:
        price_for_rent = 3000 * 0.85
    else:
        price_for_rent = 3000 * 0.75
if season == "Summer" or season == "Autumn":
    if fisherman_count <= 6:
        price_for_rent = 4200 * 0.90
    elif 7 < fisherman_count <= 11:
        price_for_rent = 4200 * 0.85
    else:
        price_for_rent = 4200 * 0.75
if season == "Winter":
    if fisherman_count <= 6:
        price_for_rent = 2600 * 0.90
    elif 7 < fisherman_count <= 11:
        price_for_rent = 2600 * 0.85
    else:
        price_for_rent = 2600 * 0.75
if fisherman_count % 2 == 0:
    if season != "Autumn":
        price_for_rent = price_for_rent * 0.95
difference = abs(budget - price_for_rent)
if budget >= price_for_rent:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")

