import json

def restore_lend_books(borrow_books):
    with open("all_lends.json",'r') as fp:
        borrow_books = json.load(fp)
    return borrow_books