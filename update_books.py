from view_all_books import view_all_books
from save_all_books import save_all_books
from _datetime import datetime

def update_books(all_books):
    view_all_books(all_books)
    a = input("Enter the book title to update: ")

    for book in all_books:
        if book["title"] == a:
            book['title'] = input("Enter New Book Title: ")
            book['author'] = input("Enter New Author Name: ")
            while True:
                try:
                    book['year'] = int(input("Enter New Publishing Year Number: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")
            while True:
                try:
                    book['price'] = int(input("Enter New Book Price: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")
            while True:
                try:
                    book['quantity'] = int(input("Enter New Quantity Number: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")

            book['book_last_updated_at'] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

            save_all_books(all_books)
            print("Book has been successfully updated")
            return all_books


    print("Book not found.")

