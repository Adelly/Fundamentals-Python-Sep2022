CPU_price = float(input()) * 1.57
video_card_price = float(input()) * 1.57
RAM_price = float(input()) * 1.57
RAM_count = int(input())
discount = float(input())
CPU_final_price = CPU_price - (CPU_price * discount)
video_card_final_price = video_card_price - (video_card_price * discount)
total_amount = CPU_final_price + video_card_final_price + RAM_price * RAM_count
print(f"Money needed - {total_amount:.2f} leva.")
