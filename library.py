# Class to represent a Book object
class Book:
    def __init__(self, title, author, isbn, publication_year):
        # Instance attributes for each book
        self.title = title #Instance attribute
        self.author = author #Instance attribute
        self.isbn = isbn #Instance attribute
        self.publication_year = publication_year #Instance attribute

    def __str__(self):
        # String representation when printing a book object
        return f"{self.title} by {self.author} '{self.publication_year}' '{self.isbn}'"

    def to_csv_string(self):
        # Converts book details into a single line with comma seperated values
        return f"{self.title},{self.author},{self.isbn},{self.publication_year}"

# Class to represent a Library that stores multiple books
class Library:
    def __init__(self):
        # List to store Book objects
        self.books = []

    def add_book(self, title, author, isbn, year):
        # Adds a new book to the library
        for book in self.books:
            if book.isbn == isbn:
                # Prevent adding duped ISBN
                print("ISBN already exists in the library.")
                return False
            elif book.isbn != isbn:
                # If ISBN is unique, it will be added
                new_book = Book(title, author, isbn, year)
                self.books.append(new_book)
                print(f"{title} is added")
                return True

    def display_book(self):
        # Displays all books entered in the library
        if not self.books:
            print("The library is empty.")
        else:
            print("Current library:")
            for book in self.books:
                print("\n")
                print(book) # Uses __str__ method of book


    def search_book(self, query):
        # Searches for a book in titles
        for book in self.books:
            if book.title.lower() == query:
                print("\n")
                print(f"{query}, Book exists.")
                return True
        print("\n")
        print(f"{query}, Book does not yet exist.")
        return False

    def save_to_file(self, filename):
        # Saves all book data to a file in csv format
        try:
            with open(filename, 'w') as file:
                for book in self.books:
                    file.write(book.to_csv_string() + '\n')
            print(f"Books saved successfully to '{filename}'!")
        except IOError:
            # Handles file-writing errors
            print(f"Error: Could not save to file '{filename}'.")

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                self.books = []  # Clear current list before loading
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) != 4:
                        # Skip invalid lines
                        print(f"Error: skipping invalid data in file: '{line.strip()}'")
                        continue
                    title, author, isbn_str, year_str = parts
                    try:
                        # Convert ISBN and Year to integers
                        isbn = int(isbn_str)
                        year = int(year_str)
                        book = Book(title, author, isbn, year)
                        self.books.append(book)
                    except ValueError:
                        # Prints out a message when ISBN/year are not valid integers
                        print(f"Error: invalid ISBN or year in line: '{line.strip()}'")
            print(f"Library loaded successfully! Loaded {len(self.books)} books.")
        except FileNotFoundError:
            # Prints out a message if the file was not found
            print(f"Error: The library file '{filename}' was not found. Starting with an empty library..")

# Main program function
def main():
    library = Library()
    filename = "library.csv"
    print("--- Library Management System ---")
    library.load_from_file(filename)

    while True:
        # Menu options
        print("\n" + "=" * 30)
        print("Please choose an option:")
        print("1. Add a book")
        print("2. Display library")
        print("3. Save to file")
        print("4. Load from file")
        print("5. Search book")
        print("6. Exit")
        print("=" * 30)
        while True:
                choice = input("> ")
                if choice in ('1', '2', '3', '4', '5', '6'):
                    break
                else:
                    print("Invalid choice. Please enter a number from 1 to 6.")
        if choice == '1':
            try:
                title = input("Enter a book title: ")
                author = input("Enter author name: ")
                isbn = int(input("Enter isbn (numbers only): "))
                publication_year = int(input("Enter publication year: "))
                library.add_book(title, author, isbn, publication_year)
            except ValueError:
                print("Invalid input. Please enter numbers for ISBN and publication year.")
        elif choice == '2':
            library.display_book()
        elif choice == '3':
            library.save_to_file(filename)
        elif choice == '4':
            library.load_from_file(filename)
        elif choice == '5':
            LocateBook = input("Enter a book name :").lower()
            library.search_book(LocateBook)
        elif choice == '6':
            print("Exiting program. Goodbye!")
            return False
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")
            return True

if __name__ == "__main__":
    main()
