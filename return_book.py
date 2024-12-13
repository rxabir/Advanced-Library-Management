from lend_book import save_all_lends
from save_all_books import save_all_books
def return_book(borrow_books,all_books):
    if borrow_books != []:
        a = input("Enter the name of the borrower: ")
        for person in borrow_books:
            if person['name'] == a:
                q = person['book']
                for book in all_books:
                    if book['title'] == q:
                        book['quantity'] += 1
                        save_all_books(all_books)
                        borrow_books.remove(person)
                        save_all_lends(borrow_books)
                        print("Book returned Successfully.")
                        break
                break
        else:
            print("Borrower not found.")
    else:
        print("No one has borrowed any books")