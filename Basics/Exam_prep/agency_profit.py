airline = input()
adult_tickets = int(input())
child_tickets = int(input())
adult_price = float(input())
service_fee = float(input())
child_price = adult_price * 0.30
service_fee_total = (adult_tickets + child_tickets) * service_fee
final_amount = (adult_tickets * adult_price) + (child_tickets * child_price) + service_fee_total
revenue = final_amount * 0.20
print(f"The profit of your agency from {airline} tickets is {revenue:.2f} lv.")