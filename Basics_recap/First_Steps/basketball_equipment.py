annual_fee_basketball = int(input())
basketball_shoes = annual_fee_basketball - (annual_fee_basketball * 0.40)
basketball_set = basketball_shoes - (basketball_shoes * 0.20)
basketball_ball = basketball_set * 0.25
basketball_accessories = basketball_ball * 0.20
total_expenses_basketball = annual_fee_basketball + basketball_shoes + basketball_set + basketball_ball + basketball_accessories
print(total_expenses_basketball)