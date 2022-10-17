budget = float(input())
video_cards = int(input())
processors = int(input())
ram = int(input())
total_amount = video_cards * 250 + (((video_cards * 250) * 0.35) * processors) + (((video_cards * 250) * 0.10) * ram)
if video_cards > processors:
    total_amount = total_amount - total_amount * 0.15
if budget >= total_amount:
    print(f"You have {budget - total_amount:.2f} leva left!")
else:
    print(f"Not enough money! You need {total_amount - budget:.2f} leva more!")

