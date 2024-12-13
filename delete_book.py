from save_all_books import save_all_books
def delete_book(all_books):
    if all_books != []:
        a = input("Enter the book title to delete: ")
        for book in all_books:
            if book['title'] == a:
                all_books.remove(book)
                save_all_books(all_books)
                print("Book Deleted Successfully.")
                return all_books
        print("Book not found.")
    else:
        print("Library is empty.")

