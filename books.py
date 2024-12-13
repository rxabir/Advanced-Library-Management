import add_books
import return_book
import view_all_books
import update_books
from restore_books_file import restore_all_books
from restore_lend_book import restore_lend_books
import delete_book
import lend_book

all_books = []
borrow_books = []

while True:
    print("Welcome to Library Management System")
    print("0. Exit")
    print("1. Add books")
    print("2. View All Books")
    print("3. Update books")
    print("4. Remove books")
    print("5. Lend books")

    all_books = restore_all_books(all_books)
    borrow_books = restore_lend_books(borrow_books)

    menu = input("Select any number: ")

    if menu == "0":
        print("Thanks for using Library Management System ")
        break
    elif menu == "1":
        all_books = add_books.add_books(all_books)
    elif menu == "2":
        view_all_books.view_all_books(all_books)
    elif menu == "3":
        update_books.update_books(all_books)
    elif menu == "4":
        delete_book.delete_book(all_books)
    elif menu == "5":
        print("1. Borrow book")
        print("2. Return book")

        menu2 = input("Select any number: ")

        if menu2 == "1":
            lend_book.borrow_book(borrow_books,all_books)
        elif menu2 == "2":
            return_book.return_book(borrow_books,all_books)
        else:
            print("Choose a valid number.")

    else:
        print("Choose a valid number.")