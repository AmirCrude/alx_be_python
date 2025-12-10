class Book:
    """Base class representing a book."""
    
    def __init__(self, title, author):
        """Initialize book with title and author."""
        self.title = title
        self.author = author
    
    def __str__(self):
        """String representation for Book class."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Derived class representing an electronic book."""
    
    def __init__(self, title, author, file_size):
        """Initialize EBook with title, author, and file size."""
        super().__init__(title, author)
        self.file_size = file_size
    
    def __str__(self):
        """String representation for EBook class."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Derived class representing a printed book."""
    
    def __init__(self, title, author, page_count):
        """Initialize PrintBook with title, author, and page count."""
        super().__init__(title, author)
        self.page_count = page_count
    
    def __str__(self):
        """String representation for PrintBook class."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """Library class demonstrating composition by managing books."""
    
    def __init__(self):
        """Initialize library with empty list of books."""
        self.books = []
    
    def add_book(self, book):
        """Add a book (Book, EBook, or PrintBook) to the library."""
        if isinstance(book, (Book, EBook, PrintBook)):
            self.books.append(book)
        else:
            print("Error: Can only add Book objects to the library")
    
    def list_books(self):
        """Print details of all books in the library."""
        for book in self.books:
            print(book)