nylon_m = int(input())
paint_litres = int(input())
thinner = int(input())
worker_hours = int(input())
nylon_price = (nylon_m + 2) * 1.50
paint_price = (paint_litres + paint_litres * 0.10) * 14.50
thinner_price = thinner * 5.00
bags_price = 0.40
material_expenses = nylon_price + paint_price + thinner_price + bags_price
worker_expenses = (material_expenses * 0.30) * worker_hours
total_expenses = material_expenses + worker_expenses
print(total_expenses)



