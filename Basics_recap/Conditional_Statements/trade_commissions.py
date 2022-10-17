city = input()
sales = float(input())
commission = 0
if city == "Sofia":
    if 0 <= sales <= 500:
        commission = 0.05
    if 500 < sales <= 1000:
        commission = 0.07
    if 1000 < sales <= 10000:
        commission = 0.08
    if sales > 10000:
        commission = 0.12
if city == "Varna":
    if 0 <= sales <= 500:
        commission = 0.045
    if 500 < sales <= 1000:
        commission = 0.075
    if 1000 < sales <= 10000:
        commission = 0.10
    if sales > 10000:
        commission = 0.13
if city == "Plovdiv":
    if 0 <= sales <= 500:
        commission = 0.055
    if 500 < sales <= 1000:
        commission = 0.08
    if 1000 < sales <= 10000:
        commission = 0.12
    if sales > 10000:
        commission = 0.145
if commission == 0:
    print("error")
else:
    print(f"{sales * commission:.2f}")