class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True  # Book is available by default


class Patron:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []  # List to store borrowed books


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)  # Add book to library

    def register_patron(self, patron):
        self.patrons.append(patron)  # Register a new patron

    def borrow_book(self, patron, book):
        if book.available:
            book.available = False
            patron.borrowed_books.append(book)  # Assign book to patron
            print(f"{patron.name} borrowed '{book.title}'.")
        else:
            print(f"'{book.title}' is not available.")

    def return_book(self, patron, book):
        if book in patron.borrowed_books:
            book.available = True
            patron.borrowed_books.remove(book)
            print(f"{patron.name} returned '{book.title}'.")
        else:
            print(f"{patron.name} did not borrow '{book.title}'.")


# Example usage
library = Library()

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("1984", "George Orwell")

library.add_book(book1)
library.add_book(book2)

patron = Patron("Alice")
library.register_patron(patron)

library.borrow_book(patron, book1)
library.return_book(patron, book1)