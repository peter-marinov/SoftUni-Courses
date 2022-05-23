searched_book = input()
checked_books_cnt = 0
book_is_found = False
next_book = input()
# while searched_book != next_book:
#     if next_book == "No More Books":
#         break

while next_book != "No More Books":
    if next_book == searched_book:
        book_is_found = True
        break

    checked_books_cnt += 1
    next_book = input()


if not book_is_found:
    print("The book you search is not here!")
    print(f"You checked {checked_books_cnt} books.")
else:
    print(f"You checked {checked_books_cnt} books and found it.")