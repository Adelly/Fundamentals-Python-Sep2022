joinery_count = int(input())
joinery_type = input()
delivery_type = input()
price = 0
if joinery_type == "90X130":
    price = 110 * joinery_count
    if 30 < joinery_count <= 60:
        price *= 0.95
    elif joinery_count > 60:
        price *= 0.92
elif joinery_type == "100X150":
    price = 140 * joinery_count
    if 40 < joinery_count <= 80:
        price *= 0.94
    elif joinery_count > 80:
        price *= 0.90
elif joinery_type == "130X180":
    price = 190 * joinery_count
    if 20 < joinery_count <= 50:
        price *= 0.93
    elif joinery_count > 50:
        price *= 0.88
elif joinery_type == "200X300":
    price = 250 * joinery_count
    if 25 < joinery_count <= 50:
        price *= 0.91
    elif joinery_count > 50:
        price *= 0.86
if delivery_type == "With delivery":
    price += 60
if joinery_count > 99:
    price *= 0.96
if joinery_count < 10:
    print(f"Invalid order")
else:
    print(f"{price:.2f} BGN")


