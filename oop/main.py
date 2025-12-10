from book_class import Book

def main():
    # Create an instance of Book
    book1 = Book("1984", "George Orwell", 1949)
    
    # Print the book using __str__
    print(book1)
    
    # Print the book using __repr__
    print(repr(book1))
    
    # Delete the book instance
    del book1

if __name__ == "__main__":
    main()