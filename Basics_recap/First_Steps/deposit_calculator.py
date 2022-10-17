deposit = float(input())
deposit_period = int(input())
annual_interest_rate = float(input()) / 100
total_interest_rate = deposit * annual_interest_rate
final_amount = deposit + deposit_period * ((deposit*annual_interest_rate) / 12)
print(final_amount)