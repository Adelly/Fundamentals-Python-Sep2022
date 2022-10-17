trekking_groups = int(input())
people_count_total = 0
musala_group = 0
montblanc_group = 0
kilimanjaro_group = 0
k2_group = 0
everest_group = 0
for each_group in range(1, trekking_groups + 1):
    people_count = int(input())
    people_count_total += people_count
    if people_count <= 5:
        peak = "Musala"
        musala_group += people_count
    elif 6 <= people_count <= 12:
        peak = "Montblanc"
        montblanc_group += people_count
    elif 13 <= people_count <= 25:
        peak = "Kilimanjaro"
        kilimanjaro_group += people_count
    elif 26 <= people_count <= 40:
        peak = "K2"
        k2_group += people_count
    elif people_count >= 41:
        peak = "Everest"
        everest_group += people_count
musala_percent = musala_group/ people_count_total * 100
montblanc_percent = montblanc_group / people_count_total * 100
kilimanjaro_percent = kilimanjaro_group / people_count_total * 100
k2_percent = k2_group / people_count_total * 100
everest_percent = everest_group / people_count_total * 100
print(f"{musala_percent:.2f}%")
print(f"{montblanc_percent:.2f}%")
print(f"{kilimanjaro_percent:.2f}%")
print(f"{k2_percent:.2f}%")
print(f"{everest_percent:.2f}%")