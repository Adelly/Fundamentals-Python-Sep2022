initial_hours = int(input())
initial_minutes = int(input())
total_time = initial_hours * 60 + initial_minutes + 15
hours = total_time // 60
minutes = total_time % 60
if hours > 23: #добавяйки го е добре да проверим дали не сме си счупили логиката при другите сценарии
    hours = 0
if minutes < 10:
    print(f"{hours}:0{minutes}")
else:
    print(f"{hours}:{minutes}")
