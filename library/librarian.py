

# Function add 
def add_book(library, title, author, isbn):
    if isbn in library:
        print("The book already exists")
    else:
        library[isbn] = {
            'title': title,
            'author': author,
            'isbn': isbn,
            'available': True
        }
        print(f"Book added: {title}")

# Function remove 
def remove_book(library, isbn):
    if isbn in library:
        del library[isbn]
        print(f"Book with ISBN {isbn} removed")
    else:
        print("Book not found")



# Functioncheck 
def check_out_book(library, isbn):
    if isbn not in library:
        print("Book not found")
    elif not library[isbn]['available']:
        print("The book is already checked out")
    else:
        library[isbn]['available'] = False
        print(f"Book checked out: {library[isbn]['title']}")




# Function return
def return_book(library, isbn):
    if isbn in library:
        library[isbn]['available'] = True
        print(f"Book returned: {library[isbn]['title']}")
    else:
        print("Book not found")

# Function display
def display_books(library):
    print("\nLibrary Books:")
    for book in library.values():
        status = "Available" if book['available'] else "Checked Out"
        print(f"{book['title']} by {book['author']} (ISBN: {book['isbn']}) - {status}")
    print()
