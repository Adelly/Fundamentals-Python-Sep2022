landscaping_area_m = float(input())
landscaping_price_per_m = 7.61
landscaping_total_price = landscaping_area_m * landscaping_price_per_m
discount = 0.18 * landscaping_total_price
final_price = landscaping_total_price - discount
print(f"The final price is: {final_price} lv.")
print(f"The discount is: {discount} lv.")


