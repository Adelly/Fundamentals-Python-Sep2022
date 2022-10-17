trip_amount = float(input())
puzzle_count = int(input())
dolls_count = int(input())
teddy_bear_count = int(input())
minions_count = int(input())
trucks_count = int(input())
ordered_toys_count = puzzle_count + dolls_count + teddy_bear_count + minions_count + trucks_count
ordered_toys_amount = (2.60 * puzzle_count) + (3.00 * dolls_count) + (4.10 * teddy_bear_count) + (8.20 * minions_count) + (2.00 * trucks_count)
# revenue = 0
if ordered_toys_count >= 50:
    ordered_toys_amount = ordered_toys_amount - ordered_toys_amount * 0.25
    revenue = ordered_toys_amount - ordered_toys_amount * 0.10
else:
    revenue = ordered_toys_amount - ordered_toys_amount * 0.10
if trip_amount <= revenue:
    print(f" Yes! {revenue - trip_amount:.2f} lv left.")
else:
    print(f"Not enough money! {trip_amount - revenue:.2f} lv needed.")





