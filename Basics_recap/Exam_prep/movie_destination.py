movie_budget = float(input())
destination = input()
season = input()
days = int(input())
shooting_price_per_day = 0
if season == "Winter":
    if destination == "Dubai":
        shooting_price_per_day = 45000 * 0.70
    elif destination == "Sofia":
        shooting_price_per_day = 17000 * 1.25
    elif destination == "London":
        shooting_price_per_day = 24000
elif season == "Summer":
    if destination == "Dubai":
        shooting_price_per_day = 40000 * 0.70
    elif destination == "Sofia":
        shooting_price_per_day = 12500 * 1.25
    elif destination == "London":
        shooting_price_per_day = 20250
total_cost = shooting_price_per_day * days
price_difference = abs(movie_budget - total_cost)
if total_cost <= movie_budget:
    print(f"The budget for the movie is enough! We have {price_difference:.2f} leva left!")
else:
    print(f"The director needs {price_difference:.2f} leva more!")