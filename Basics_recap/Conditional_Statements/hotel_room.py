month = input()
nights = int(input())
studio_price = 0
apartment_price = 0
if month == "May" or month == "October":
    if nights <= 7:
        studio_price = 50 * nights
        apartment_price = 65 * nights
    elif nights > 14:
        studio_price = (50 * nights) * 0.70
        apartment_price = (65 * nights) * 0.90
    else:
        studio_price = (50 * nights) * 0.95
        apartment_price = 65 * nights
elif month == "June" or month == "September":
    if nights > 14:
        studio_price = (75.20 * nights) * 0.80
        apartment_price = (68.70 * nights) * 0.90
    else:
        studio_price = 75.20 * nights
        apartment_price = 68.70 * nights
elif month == "July" or month == "August":
    if nights > 14:
        studio_price = 76 * nights
        apartment_price = (77 * nights) * 0.90
    else:
        studio_price = 76 * nights
        apartment_price = 77 * nights
print(f"Apartment: {apartment_price:.2f} lv.")
print(f"Studio: {studio_price:.2f} lv.")
