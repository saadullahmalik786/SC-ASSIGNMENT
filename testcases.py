import unittest
from library_management_system import LibraryManagementSystem, Book

class TestLibraryManagementSystem(unittest.TestCase):
    def test_add_book(self):
        lms = LibraryManagementSystem()
        book = Book(1, "The Great Gatsby", "F. Scott Fitzgerald", "Fiction")
        lms.add_book(book)
        self.assertEqual(len(lms.books), 1)
        self.assertEqual(lms.books[0].title, "The Great Gatsby")

    def test_search_book(self):
        lms = LibraryManagementSystem()
        book = Book(2, "1984", "George Orwell", "Dystopian")
        lms.add_book(book)
        self.assertEqual(lms.books[0].title, "1984")

    def test_delete_book(self):
        lms = LibraryManagementSystem()
        book = Book(3, "To Kill a Mockingbird", "Harper Lee", "Classic")
        lms.add_book(book)
        lms.delete_book(3)
        self.assertEqual(len(lms.books), 0)

if __name__ == "__main__":
    unittest.main()
