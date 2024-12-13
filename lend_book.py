import json
from datetime import datetime
from save_all_books import save_all_books


def borrow_book(borrow_books, all_books):
    name = input("Enter Borrower's name: ")
    phone = input("Enter Borrower's phone: ")
    while True:
        book = input("Enter the book title: ")
        book_found = book_checks(all_books, book)

        if book_found:
            while True:
                try:
                    due = input("Enter Return Due date (DD-MM-YYYY): ")
                    date = datetime.strptime(due, "%d-%m-%Y").date()
                    break
                except ValueError:
                    print("Invalid date format! Please enter a date in 'DD-MM-YYYY' format.")

            borrower = {
                "name": name,
                "phone": phone,
                "book": book,
                "due": due
            }
            borrow_books.append(borrower)
            save_all_lends(borrow_books)
            print("Book lending successful.")
            break



def save_all_lends(borrow_books):
    with open("all_lends.json","w") as fp:
        json.dump(borrow_books, fp, indent=4)


def book_checks(all_books,book):
    for mybook in all_books:
        if mybook["title"] == book:
            if mybook['quantity'] > 0:
                mybook['quantity'] -= 1
                save_all_books(all_books)
                return True
            else:
                print("There are not enough books available to lend.")
                return False
    print("Book not found. Please try again.")
    return False

