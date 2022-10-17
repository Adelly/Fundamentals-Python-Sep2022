record_seconds = float(input())
distance_meters = float(input())
one_meter_distance_seconds = float(input())
total_time = distance_meters * one_meter_distance_seconds
delay = distance_meters // 15 * 12.5
total_time = total_time + delay
if total_time < record_seconds:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {total_time - record_seconds:.2f} seconds slower.")


