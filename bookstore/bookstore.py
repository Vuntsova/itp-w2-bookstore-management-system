def create_bookstore(name):
    bookstore = {
        "name": name,
        'authors' : [],
        'books': []
        
    }
    return bookstore
print(create_bookstore("rmotr's bookstore"), " 1")

def get_bookstore_name(bookstore):
#     print(bookstore['name'], " 2")
    return bookstore['name']
get_bookstore_name(create_bookstore('fm'))

def add_author(bookstore, name, nationality):
    author = {
        "name": name, 
        "nationality":nationality,
        
    }
    bookstore['authors'].append(author)
    return author


def get_author_by_name(bookstore, name):
    for author in bookstore['authors']:
        if author['name'] == name:
            return author
# print(get_author_by_name(create_bookstore("rmotr's bookstore"), 'James Joyce'), "get_author_by_name")


def add_book(bookstore, title, isbn, author):
    book = { 
        'title':title, 
        'isbn':isbn, 
        'author':author
    }
    
    bookstore['books'].append(book )
    return book
    
    
    
#     for a in bookstore['authors']:
#         if a['name'] == author:
#             a.setdefault('title', title)
#             a.setdefault('isbn', isbn)
#             return a
print()
print()
print()
print(add_book(create_bookstore("rmotr's bookstore"), 'El Aleph', 'XXX-4', 'Jorge Luis Borges'))
    


def get_book_by_title(bookstore, title):
    for book in bookstore['books']:
        if book['title'] == title:
            return book


def get_books_by_author(bookstore, author):
    books = []
    for book in bookstore['books']:
        if book['author'] == author:
            books.append(book)
        
    return books
    
