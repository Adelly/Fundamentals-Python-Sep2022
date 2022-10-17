movie_name = input()
days = int(input())
tickets = int(input())
ticket_price = float(input())
cinema_revenue_percentage = int(input())
tickets_sold = days * tickets * ticket_price
cinema_revenue = tickets_sold * cinema_revenue_percentage / 100
movie_revenue = tickets_sold - cinema_revenue
print(f"The profit from the movie {movie_name} is {movie_revenue:.2f} lv.")