string = input()
while string != "End":
    if string == "SoftUni":
        continue
    for char in string:
        print(char * 2, end="")
    print()
    string = input()
