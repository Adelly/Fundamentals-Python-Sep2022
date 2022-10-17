budget = float(input())
number_of_series = int(input())
price = 0
for series in range(1, number_of_series + 1):
    series_name = input()
    series_price = float(input())
    if series_name == "Thrones":
        price += 0.50 * series_price
    elif series_name == "Lucifer":
        price += 0.60 * series_price
    elif series_name == "Protector":
        price += 0.70 * series_price
    elif series_name == "TotalDrama":
        price += 0.80 * series_price
    elif series_name == "Area":
        price += 0.90 * series_price
    else:
        price += series_price
gap = abs(budget - price)
if budget >= price:
    print(f"You bought all the series and left with {gap:.2f} lv.")
else:
    print(f"You need {gap:.2f} lv. more to buy the series!")