class Book:
    """A class representing a book with magic methods."""
    
    def __init__(self, title, author, year):
        """Constructor to initialize book attributes."""
        self.title = title
        self.author = author
        self.year = year
    
    def __del__(self):
        """Destructor to print message when object is deleted."""
        print(f"Deleting {self.title}")
    
    def __str__(self):
        """User-friendly string representation of the book."""
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        """Official representation that can recreate the object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"