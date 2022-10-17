#:1 hours - range (0, 23 + 1)
#:2 minutes - range (0, 59 + 1)
for hour in range(24):
    for minutes in range(60):
        print(f"{hour:02d}:{minutes:02d}")


