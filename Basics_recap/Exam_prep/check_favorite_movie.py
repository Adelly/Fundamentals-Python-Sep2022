command = input()
counter = 0
best_movie = ""
best_movie_points = 0
while command != "STOP":
    movie = command
    counter += 1
    if counter > 7:
        print("The limit is reached.")
        break
    for letter in range(1, len(movie) + 1):
        if letter.isupper():
            upper_letters += 1
        else:
            lower_letters += 1


    command = input()
print(f"The best movie for you is {best_movie} with {symbol} ASCII sum.")


# ASCII value:
# c = "M"
# print(ord(c))