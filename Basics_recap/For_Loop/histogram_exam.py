numbers_count = int(input())
p1_count = 0
p2_count = 0
p3_count = 0
p4_count = 0
p5_count = 0
for numbers in range(1, numbers_count + 1):
    current_number = int(input())
    if current_number < 200:
        p1_count += 1
    elif 200 <= current_number < 400:
        p2_count += 1
    elif 400 <= current_number < 600:
        p3_count += 1
    elif 600 <= current_number < 800:
        p4_count += 1
    else:
        p5_count += 1
count_all = p1_count + p2_count + p3_count + p4_count + p5_count
p1_percent = (p1_count / count_all) * 100
p2_percent = (p2_count / count_all) * 100
p3_percent = (p3_count / count_all) * 100
p4_percent = (p4_count / count_all) * 100
p5_percent = (p5_count / count_all) * 100
print(f"{p1_percent:.2f}%")
print(f"{p2_percent:.2f}%")
print(f"{p3_percent:.2f}%")
print(f"{p4_percent:.2f}%")
print(f"{p5_percent:.2f}%")