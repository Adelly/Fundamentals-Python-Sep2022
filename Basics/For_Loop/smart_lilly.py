age = int(input())
washing_machine_price = float(input())
toy_price = int(input())
toys_count = 0
money = 0
money_total = 0
for years in range(1, age + 1):
    if years % 2 == 0:
        money += 10
        money_total += money
        money_total -= 1
    else:
        toys_count += 1
money_from_toys = toy_price * toys_count
total_money = money_from_toys + money_total
if total_money >= washing_machine_price:
    remaining = total_money - washing_machine_price
    print(f"Yes! {remaining:.2f}")
else:
    difference = abs(total_money - washing_machine_price)
    print(f"No! {difference:.2f}")
