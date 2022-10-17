actor = input()
points_from_the_academy = float(input())
jury_count = int(input())
final_evaluation = points_from_the_academy
for jury in range(1, jury_count + 1):
    jury_name = input()
    jury_points = float(input())
    name_points = len(jury_name)
    final_evaluation += (jury_points * name_points) / 2
    if final_evaluation >= 1250.5:
        break
if final_evaluation > 1250.5:
    print(f"Congratulations, {actor} got a nominee for leading role with {final_evaluation:.1f}! ")
else:
    difference = 1250.5 - final_evaluation
    print(f"Sorry, {actor} you need {difference:.1f} more!")