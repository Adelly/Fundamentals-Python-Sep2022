length_cm = int(input())
width_cm = int(input())
height_cm = int(input())
percentage = float(input())
fish_tank_volume_cm = length_cm * width_cm * height_cm
fish_tank_volume_litres = fish_tank_volume_cm / 1000
space_occupied = fish_tank_volume_litres * 0.17
space_free = fish_tank_volume_litres - space_occupied
print(space_free)