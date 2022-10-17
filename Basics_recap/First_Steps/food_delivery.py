chicken_menu_count = int(input())
fish_menu_count = int(input())
vegan_menu_count = int(input())
chicken_price = chicken_menu_count * 10.35
fish_price = fish_menu_count * 12.40
vegan_price = vegan_menu_count * 8.15
dessert_price = (chicken_price + fish_price + vegan_price) * 0.20
delivery_price = 2.50
total_cost = chicken_price + fish_price + vegan_price + dessert_price + delivery_price
print(total_cost)

