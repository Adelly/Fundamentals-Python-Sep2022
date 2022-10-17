book_needed = input()
current_book = input()
books_checked = 0
is_book_found = False
while current_book != "No More Books":
    if current_book == book_needed:
        is_book_found = True
        break
    else:
        books_checked += 1
        current_book = input()
if is_book_found:
    print(f"You checked {books_checked} books and found it.")
else:
    print(f"The book you search is not here!")
    print(f"You checked {books_checked} books.")
