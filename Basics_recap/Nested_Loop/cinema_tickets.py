command = input()
student_tickets = 0
standard_tickets = 0
kids_tickets = 0
while command != "Finish":
    movie = command
    seats_available = int(input())
    input_line = input()
    seats_sold = 0
    while input_line != "End":
        ticket_type = input_line
        seats_sold += 1
        if ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "kid":
            kids_tickets += 1
        if seats_sold >= seats_available:
            break
        input_line = input()
    capacity_used = seats_sold / seats_available * 100
    print(f"{movie} - {capacity_used:.2f}% full.")
    command = input()
sum_of_all_tickets = student_tickets + standard_tickets + kids_tickets
student_percentage = student_tickets / sum_of_all_tickets * 100
standard_percentage = standard_tickets / sum_of_all_tickets * 100
kids_percentage = kids_tickets / sum_of_all_tickets * 100
print(f"Total tickets: {sum_of_all_tickets}")
print(f"{student_percentage:.2f}% student tickets.")
print(f"{standard_percentage:.2f}% standard tickets.")
print(f"{kids_percentage:.2f}% kids tickets.")
