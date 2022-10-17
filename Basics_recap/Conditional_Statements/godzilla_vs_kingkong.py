movie_budget = float(input())
statists_count = int(input())
outfit_price_per_statist = float(input())
decor = movie_budget * 0.10
outfit_total_price = statists_count * outfit_price_per_statist
if statists_count > 150:
    outfit_total_price = outfit_total_price - (outfit_total_price * 0.10)
if outfit_total_price + decor > movie_budget:
    print(f"Not enough money!")
    print(f"Wingard needs {(outfit_total_price + decor) - movie_budget:.2f} leva more.")
else:
    print(f"Action!")
    print(f"Wingard starts filming with {movie_budget - (outfit_total_price + decor):.2f} leva left.")


