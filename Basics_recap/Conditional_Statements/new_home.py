flowers = input()
flowers_count = int(input())
budget = int(input())
price = 0
if flowers == "Roses":
    if flowers_count > 80:
        price = (5 * flowers_count) - (5 * flowers_count) * 0.10
    else:
        price = 5 * flowers_count
elif flowers == "Dahlias":
    if flowers_count > 90:
        price = (3.80 * flowers_count) - (3.80 * flowers_count) * 0.15
    else:
        price = 3.80 * flowers_count
elif flowers == "Tulips":
    if flowers_count > 80:
        price = (2.80 * flowers_count) - (2.80 * flowers_count) * 0.15
    else:
        price = 2.80 * flowers_count
elif flowers == "Narcissus":
    if flowers_count < 120:
        price = (3 * flowers_count) + (3 * flowers_count) * 0.15
    else:
        price = 3 * flowers_count
elif flowers == "Gladiolus":
    if flowers_count < 80:
        price = (2.50 * flowers_count) + (2.50 * flowers_count) * 0.20
    else:
        price = 2.50 * flowers_count
if budget >= price:
    print(f"Hey, you have a great garden with {flowers_count} {flowers} and {budget - price:.2f} leva left.")
else:
    print(f"Not enough money, you need {price - budget:.2f} leva more.")
