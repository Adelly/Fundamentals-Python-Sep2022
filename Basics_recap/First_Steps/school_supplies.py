pen_bundle = 5.80
marker_bundle = 7.20
detergent = 1.20 #litre
count_pen_bundle = int(input())
count_marker_bundle = int(input())
litres_detergent = int(input())
discount = int(input()) / 100
total_amount_needed = count_pen_bundle * pen_bundle + count_marker_bundle * marker_bundle + litres_detergent * detergent
final_amount = total_amount_needed - (total_amount_needed * discount)
print(final_amount)