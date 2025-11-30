# library_management.py

class Book:
    """A class representing a book in the library."""
    
    def __init__(self, title, author):
        """Initialize a book with title, author, and set it as available."""
        self.title = title
        self.author = author
        self._is_checked_out = False
    
    def check_out(self):
        """Check out the book if it is available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    
    def return_book(self):
        """Return the book to the library."""
        self._is_checked_out = False
    
    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out
    
    def __str__(self):
        """Return string representation of the book."""
        return f"{self.title} by {self.author}"


class Library:
    """A class representing a library that manages a collection of books."""
    
    def __init__(self):
        """Initialize the library with an empty collection of books."""
        self._books = []
    
    def add_book(self, book):
        """Add a book to the library collection."""
        self._books.append(book)
    
    def check_out_book(self, title):
        """
        Check out a book by title.
        Returns True if successful, False if book not found or already checked out.
        """
        for book in self._books:
            if book.title == title:
                return book.check_out()
        return False
    
    def return_book(self, title):
        """Return a book to the library by title."""
        for book in self._books:
            if book.title == title:
                book.return_book()
                return True
        return False
    
    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No books available.")