movie = input()
order = input()
ticket_count = int(input())
price = 0
if movie == "John Wick":
    if order == "Drink":
        price = 12
    elif order == "Popcorn":
        price = 15
    elif order == "Menu":
        price = 19
elif movie == "Star Wars":
    if order == "Drink":
        price = 18
    elif order == "Popcorn":
        price = 25
    elif order == "Menu":
        price = 30
    if ticket_count >= 4:
        price *= 0.70
elif movie == "Jumanji":
    if order == "Drink":
        price = 9
    elif order == "Popcorn":
        price = 11
    elif order == "Menu":
        price = 14
    if ticket_count == 2:
        price *= 0.85
final_amount = price * ticket_count
print(f"Your bill is {final_amount:.2f} leva.")