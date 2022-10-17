daily_pocket_money = float(input())
daily_income = float(input())
expenses = float(input())
gift_price = float(input())
days_left = 5
money_available = ((daily_pocket_money + daily_income) * days_left) - expenses
if money_available >= gift_price:
    print(f"Profit: {money_available:.2f} BGN, the gift has been purchased.")
else:
    gap = gift_price - money_available
    print(f"Insufficient money: {gap:.2f} BGN.")

