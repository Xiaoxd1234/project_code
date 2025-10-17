import unittest
import book
from custom_errors import *

"""
You should write test cases for all the classes defined in book module
"""

class TestBook(unittest.TestCase):

    def setUp(self):
        """Set up test fixtures before each test method."""
        # Clear books list before each test
        book.Book.books.clear()

    def test_valid_physical_book(self):
        """
        1.1 Valid physical book.
        Test the init method of the Book class with valid input fields for physical book
        """
        test_book = book.Book("P001", "physical", 5, "Python Programming", "John Smith", 2023, ["programming", "python"])
        self.assertEqual(test_book.book_ID, "P001")
        self.assertEqual(test_book.book_type, "physical")
        self.assertEqual(test_book.total_copy, 5)
        self.assertEqual(test_book.title, "Python Programming")
        self.assertEqual(test_book.author, "John Smith")
        self.assertEqual(test_book.year, 2023)
        self.assertEqual(test_book.keywords, ["programming", "python"])
        self.assertIn(test_book, book.Book.books)

    def test_valid_online_book(self):
        """
        1.2 Valid online book.
        Test the init method of the Book class with valid input fields for online book
        """
        test_book = book.Book("O001", "online", 0, "Data Science", "Jane Doe", 2022, "data:science:analytics")
        self.assertEqual(test_book.book_ID, "O001")
        self.assertEqual(test_book.book_type, "online")
        self.assertEqual(test_book.total_copy, 0)
        self.assertEqual(test_book.title, "Data Science")
        self.assertEqual(test_book.author, "Jane Doe")
        self.assertEqual(test_book.year, 2022)
        self.assertEqual(test_book.keywords, ["data", "science", "analytics"])
        self.assertIn(test_book, book.Book.books)

    def test_valid_book(self):
        """
        1.1 Valid book.
        Test the init method of the Book class with valid input fields
        """
        # your test goes here
        pass

    def test_load_books_from_csv_file_not_found(self):
        """
        8.1 Load books from CSV - file not found.
        Test that FileNotFoundError is raised when CSV file doesn't exist
        """
        book.Book.books.clear()
        with self.assertRaises(FileNotFoundError):
            book.Book.load_books_from_csv("nonexistent_file.csv")

    def test_load_books_from_csv_missing_required_field(self):
        """
        8.2 Load books from CSV - missing required field.
        Test that MissingRequiredFieldError is raised when required field is missing
        """
        import tempfile
        import os
        
        book.Book.books.clear()
        
        # Create a temporary CSV file with missing required field
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as f:
            f.write("book_ID,book_type,title,author,year\n")  # Missing total_copy field
            f.write("P001,physical,Python Programming,John Smith,2023\n")
            temp_file = f.name
        
        try:
            with self.assertRaises(MissingRequiredFieldError):
                book.Book.load_books_from_csv(temp_file)
        finally:
            os.unlink(temp_file)

    def test_load_books_from_csv_empty_required_field(self):
        """
        8.3 Load books from CSV - empty required field.
        Test that MissingRequiredFieldError is raised when required field is empty
        """
        import tempfile
        import os
        
        book.Book.books.clear()
        
        # Create a temporary CSV file with empty required field
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as f:
            f.write("book_ID,book_type,title,author,year,total_copy\n")
            f.write("P001,physical,,John Smith,2023,5\n")  # Empty title field
            temp_file = f.name
        
        try:
            with self.assertRaises(MissingRequiredFieldError):
                book.Book.load_books_from_csv(temp_file)
        finally:
            os.unlink(temp_file)

    def test_load_books_from_csv_invalid_book_creation(self):
        """
        8.4 Load books from CSV - invalid book creation.
        Test that CustomError is raised when book creation fails
        """
        import tempfile
        import os
        
        book.Book.books.clear()
        
        # Create a temporary CSV file with invalid data
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as f:
            f.write("book_ID,book_type,title,author,year,total_copy\n")
            f.write("P001,invalid_type,Python Programming,John Smith,2023,5\n")  # Invalid book_type
            temp_file = f.name
        
        try:
            with self.assertRaises(CustomError):
                book.Book.load_books_from_csv(temp_file)
        finally:
            os.unlink(temp_file)

    def test_load_books_from_csv_valid_data(self):
        """
        8.5 Load books from CSV - valid data.
        Test successful loading of valid CSV data
        """
        import tempfile
        import os
        
        book.Book.books.clear()
        
        # Create a temporary CSV file with valid data
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as f:
            f.write("book_ID,book_type,title,author,year,total_copy\n")
            f.write("P001,physical,Python Programming,John Smith,2023,5\n")
            f.write("O001,online,Digital Guide,Jane Doe,2024,1\n")
            temp_file = f.name
        
        try:
            book.Book.load_books_from_csv(temp_file)
            self.assertEqual(len(book.Book.books), 2)
            
            # Check that books were created correctly
            physical_book = book.Book.find_book_by_id("P001")
            self.assertIsNotNone(physical_book)
            self.assertEqual(physical_book.title, "Python Programming")
            self.assertEqual(physical_book.book_type, "physical")
            self.assertEqual(physical_book.total_copy, 5)
            
            online_book = book.Book.find_book_by_id("O001")
            self.assertIsNotNone(online_book)
            self.assertEqual(online_book.title, "Digital Guide")
            self.assertEqual(online_book.book_type, "online")
            self.assertEqual(online_book.total_copy, 1)
            
        finally:
            os.unlink(temp_file)

    def test_load_books_from_csv_with_keywords(self):
        """
        8.6 Load books from CSV - with keywords.
        Test loading CSV data that includes keywords
        """
        import tempfile
        import os
        
        book.Book.books.clear()
        
        # Create a temporary CSV file with keywords
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as f:
            f.write("book_ID,book_type,title,author,year,total_copy,keywords\n")
            f.write("P001,physical,Python Programming,John Smith,2023,5,python;programming;beginner\n")
            temp_file = f.name
        
        try:
            book.Book.load_books_from_csv(temp_file)
            self.assertEqual(len(book.Book.books), 1)
            
            test_book = book.Book.find_book_by_id("P001")
            expected_keywords = ["python", "programming", "beginner"]
            self.assertEqual(sorted(test_book.keywords), sorted(expected_keywords))
            
        finally:
            os.unlink(temp_file)

    def test_load_books_from_csv_auto_generate_keywords(self):
        """
        8.7 Load books from CSV - auto generate keywords.
        Test that keywords are auto-generated from title when not provided
        """
        import tempfile
        import os
        
        book.Book.books.clear()
        
        # Create a temporary CSV file without keywords column
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as f:
            f.write("book_ID,book_type,title,author,year,total_copy\n")
            f.write("P001,physical,Advanced Python Programming,John Smith,2023,5\n")
            temp_file = f.name
        
        try:
            book.Book.load_books_from_csv(temp_file)
            self.assertEqual(len(book.Book.books), 1)
            
            test_book = book.Book.find_book_by_id("P001")
            # Keywords should be auto-generated from title
            self.assertIn("advanced", test_book.keywords)
            self.assertIn("python", test_book.keywords)
            self.assertIn("programming", test_book.keywords)
            
        finally:
            os.unlink(temp_file)

    def test_load_books_from_csv_invalid_year(self):
        """
        8.8 Load books from CSV - invalid year.
        Test that CustomError is raised when year is invalid
        """
        import tempfile
        import os
        
        book.Book.books.clear()
        
        # Create a temporary CSV file with invalid year
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as f:
            f.write("book_ID,book_type,title,author,year,total_copy\n")
            f.write("P001,physical,Python Programming,John Smith,invalid_year,5\n")
            temp_file = f.name
        
        try:
            with self.assertRaises(CustomError):
                book.Book.load_books_from_csv(temp_file)
        finally:
            os.unlink(temp_file)

    def test_load_books_from_csv_invalid_total_copy(self):
        """
        8.9 Load books from CSV - invalid total copy.
        Test that CustomError is raised when total_copy is invalid
        """
        import tempfile
        import os
        
        book.Book.books.clear()
        
        # Create a temporary CSV file with invalid total_copy
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as f:
            f.write("book_ID,book_type,title,author,year,total_copy\n")
            f.write("P001,physical,Python Programming,John Smith,2023,invalid_copy\n")
            temp_file = f.name
        
        try:
            with self.assertRaises(CustomError):
                book.Book.load_books_from_csv(temp_file)
        finally:
            os.unlink(temp_file)

if __name__ == "__main__":
    unittest.main()
