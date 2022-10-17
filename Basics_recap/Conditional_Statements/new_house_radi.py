type_of_flowers=input()
count_of_flowers=int(input())
budget=int(input())
total_price=0
rose_price=5
dahlia_price=3.8
tulips_price=2.8
narcissus_price=3
gladiolus_price=2.5
if type_of_flowers=="Roses":
    if count_of_flowers>80:
        total_price=rose_price*count_of_flowers*0.9
    else:
        total_price=rose_price*count_of_flowers
elif type_of_flowers=="Dahlias":
    if count_of_flowers>90:
        total_price=dahlia_price*count_of_flowers*0.85
    else:
        total_price=dahlia_price*count_of_flowers
elif type_of_flowers=="Tulips":
    if count_of_flowers>80:
        total_price=tulips_price*count_of_flowers*0.85
    else:
        total_price=tulips_price*count_of_flowers
elif type_of_flowers=="Narcissus":
    if count_of_flowers<120:
        total_price=narcissus_price*count_of_flowers*1.15
    else:
        total_price=narcissus_price*count_of_flowers
elif type_of_flowers=="Gladiolus":
    if count_of_flowers<80:
        total_price=gladiolus_price*count_of_flowers*1.2
    else:
        total_price=gladiolus_price*count_of_flowers
difference=abs(budget-total_price)
if budget>=total_price:
    print(f"Hey, you have a great garden with {count_of_flowers} {type_of_flowers} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")