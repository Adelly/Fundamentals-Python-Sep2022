budget = float(input())
flour_price_kg = float(input())
bread_counter = 0
colored_eggs_counter = 0
eggs_price = flour_price_kg * 0.75
milk_price = flour_price_kg * 1.25 / 4
one_bread_price = flour_price_kg + eggs_price + milk_price
while budget >= one_bread_price:
    budget -= one_bread_price
    bread_counter += 1
    colored_eggs_counter += 3
    if bread_counter % 3 == 0:
        colored_eggs_counter -= bread_counter - 2
print(f"You made {bread_counter} loaves of Easter bread! Now you have {colored_eggs_counter} eggs and {budget:.2f}BGN left.")

