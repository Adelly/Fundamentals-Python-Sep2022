luggage_price_over_20kg = float(input())
weight = float(input())
days_to_go = int(input())
luggage_count = int(input())
luggage_price = luggage_price_over_20kg
if weight < 10:
    luggage_price *= 0.20
    if days_to_go > 30:
        luggage_price *= 1.10
    elif 7 <= days_to_go <= 30:
        luggage_price *= 1.15
    else:
        luggage_price *= 1.40
elif 10 <= weight <= 20:
    luggage_price *= 0.50
    if days_to_go > 30:
        luggage_price *= 1.10
    elif 7 <= days_to_go <= 30:
        luggage_price *= 1.15
    else:
        luggage_price *= 1.40
else:
    luggage_price = luggage_price_over_20kg
    if days_to_go > 30:
        luggage_price *= 1.10
    elif 7 <= days_to_go <= 30:
        luggage_price *= 1.15
    else:
        luggage_price *= 1.40
total_price = luggage_count * luggage_price
print(f"The total price of bags is: {total_price:.2f} lv.")