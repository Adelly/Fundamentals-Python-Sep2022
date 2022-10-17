days_stay = int(input())
room_type = input()
rating = input()
price = 0
days_stay = days_stay - 1
if room_type == "apartment":
    if days_stay < 10:
        price = (25 * days_stay) * 0.70
    elif 10 <= days_stay <= 15:
        price = (25 * days_stay) * 0.65
    else:
        price = (25 * days_stay) * 0.50
elif room_type == "president apartment":
    if days_stay < 10:
        price = (35 * days_stay) * 0.90
    elif 10 <= days_stay <= 15:
        price = (35 * days_stay) * 0.85
    else:
        price = (35 * days_stay) * 0.80
elif room_type == "room for one person":
    price = 18 * days_stay
if rating == "positive":
    price = (price * 0.25) + price
else:
    price = price * 0.90
print(f"{price:.2f}")