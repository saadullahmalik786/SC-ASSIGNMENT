# library_management_system.py

class Book:
    def __init__(self, book_id, title, author, genre):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre

    def display_book(self):
        return f"Book ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Genre: {self.genre}"


class LibraryManagementSystem:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully.")

    def view_books(self):
        if not self.books:
            print("No books available.")
        else:
            for book in self.books:
                print(book.display_book())

    def search_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                print(book.display_book())
                return
        print("Book not found.")

    def delete_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                print("Book removed successfully.")
                return
        print("Book not found.")


if __name__ == "__main__":
    lms = LibraryManagementSystem()

    while True:
        print("\n1. Add Book\n2. View Books\n3. Search Book\n4. Delete Book\n5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            book_id = int(input("Enter Book ID: "))
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            genre = input("Enter Genre: ")
            book = Book(book_id, title, author, genre)
            lms.add_book(book)

        elif choice == 2:
            lms.view_books()

        elif choice == 3:
            book_id = int(input("Enter Book ID: "))
            lms.search_book(book_id)

        elif choice == 4:
            book_id = int(input("Enter Book ID: "))
            lms.delete_book(book_id)

        elif choice == 5:
            print("Exiting Program.")
            break

        else:
            print("Invalid choice. Please try again.")