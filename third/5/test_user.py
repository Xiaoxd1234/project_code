import unittest
import user
from custom_errors import *

"""
You should write test cases for all the classes defined in user module
"""
class TestUser(unittest.TestCase):

    def setUp(self):
        """Set up test fixtures before each test method."""
        # Clear users list before each test
        user.User.users.clear()

    def test_valid_student_user(self):
        """
        1.1 Valid student user.
        Test the init method of the student user class with valid input fields
        """
        student = user.Student("s001", "John Doe", "password123", "IT")
        self.assertEqual(student.user_ID, "s001")
        self.assertEqual(student.name, "John Doe")
        self.assertEqual(student.password, "password123")
        self.assertEqual(student.role, "Student")
        self.assertEqual(student.department, "IT")
        self.assertEqual(len(student.loans), 0)
        self.assertIn(student, user.User.users)

    def test_valid_staff_user(self):
        """
        1.2 Valid staff user.
        Test the init method of the staff user class with valid input fields
        """
        staff = user.Staff("e001", "Jane Smith", "password456", "Library")
        self.assertEqual(staff.user_ID, "e001")
        self.assertEqual(staff.name, "Jane Smith")
        self.assertEqual(staff.password, "password456")
        self.assertEqual(staff.role, "Staff")
        self.assertEqual(staff.department, "Library")
        self.assertEqual(len(staff.loans), 0)
        self.assertIn(staff, user.User.users)

    def test_valid_others_user(self):
        """
        1.3 Valid others user.
        Test the init method of the others user class with valid input fields
        """
        others = user.Others("o001", "Bob Wilson", "password789")
        self.assertEqual(others.user_ID, "o001")
        self.assertEqual(others.name, "Bob Wilson")
        self.assertEqual(others.password, "password789")
        self.assertEqual(others.role, "Others")
        self.assertEqual(others.department, "")
        self.assertEqual(len(others.loans), 0)
        self.assertIn(others, user.User.users)

    def test_invalid_user_creation(self):
        """
        2. Invalid user creation - comprehensive test for all invalid inputs.
        Test that various invalid inputs raise CustomValueError
        """
        # Invalid user IDs
        with self.assertRaises(CustomValueError):
            user.Student("", "John Doe", "password123", "IT")  # Empty string
        with self.assertRaises(CustomValueError):
            user.Student(None, "John Doe", "password123", "IT")  # None value
        with self.assertRaises(CustomValueError):
            user.Student(123, "John Doe", "password123", "IT")  # Non-string type
        
        # Invalid names
        with self.assertRaises(CustomValueError):
            user.Student("s001", "", "password123", "IT")  # Empty name
        with self.assertRaises(CustomValueError):
            user.Student("s001", "John123", "password123", "IT")  # Contains numbers
        with self.assertRaises(CustomValueError):
            user.Student("s001", "John@Doe", "password123", "IT")  # Special characters
        
        # Invalid password
        with self.assertRaises(CustomValueError):
            user.Student("s001", "John Doe", "", "IT")  # Empty password
        
        # Invalid departments
        with self.assertRaises(CustomValueError):
            user.Student("s001", "John Doe", "password123", "InvalidDept")  # Invalid student dept
        with self.assertRaises(CustomValueError):
            user.Staff("e001", "Jane Smith", "password456", "InvalidDept")  # Invalid staff dept
        with self.assertRaises(CustomValueError):
            user.Others("o001", "Bob Wilson", "password789")  # Non-empty dept for others

    def test_user_authentication_and_staff_check(self):
        """
        3. User authentication and staff identification tests.
        Test password checking and library staff identification
        """
        # Password checking
        student = user.Student("s001", "John Doe", "password123", "IT")
        self.assertTrue(student.check_password("password123"))  # Correct password
        self.assertFalse(student.check_password("wrongpassword"))  # Incorrect password
        
        # Library staff identification
        library_staff = user.Staff("e001", "Jane Smith", "password456", "Library")
        self.assertTrue(library_staff.is_library_staff())  # Library staff
        
        non_library_staff = user.Staff("e002", "Bob Wilson", "password789", "IT")
        self.assertFalse(non_library_staff.is_library_staff())  # Non-library staff
        
        self.assertFalse(student.is_library_staff())  # Student is not staff

    def test_get_policy_student(self):
        """
        3.6 Get policy - student.
        Test that student policy is correctly returned
        """
        student = user.Student("s001", "John Doe", "password123", "IT")
        policy = student.get_policy()
        self.assertEqual(policy['days_allowed'], 10)
        self.assertEqual(policy['quota'], 4)

    def test_get_policy_staff(self):
        """
        3.7 Get policy - staff.
        Test that staff policy is correctly returned
        """
        staff = user.Staff("e001", "Jane Smith", "password456", "Library")
        policy = staff.get_policy()
        self.assertEqual(policy['days_allowed'], 30)
        self.assertEqual(policy['quota'], 10)

    def test_get_policy_others(self):
        """
        3.8 Get policy - others.
        Test that others policy is correctly returned
        """
        others = user.Others("o001", "Bob Wilson", "password789")
        policy = others.get_policy()
        self.assertEqual(policy['days_allowed'], 7)
        self.assertEqual(policy['quota'], 2)

    def test_find_user_by_id_existing(self):
        """
        4.1 Find user by ID - existing user.
        Test that existing user is found correctly
        """
        student = user.Student("s001", "John Doe", "password123", "IT")
        found_user = user.User.find_user_by_id("s001")
        self.assertEqual(found_user, student)

    def test_find_user_by_id_non_existing(self):
        """
        4.2 Find user by ID - non-existing user.
        Test that UserNotFoundError is raised for non-existing user
        """
        with self.assertRaises(UserNotFoundError):
            user.User.find_user_by_id("nonexistent")

    def test_get_loan_count(self):
        """
        5.1 Get loan count.
        Test that loan count is correctly calculated
        """
        student = user.Student("s001", "John Doe", "password123", "IT")
        # Add some mock loans
        student.loans = [
            {'returned_date': None},
            {'returned_date': '10/09/2025'},
            {'returned_date': None}
        ]
        self.assertEqual(student.get_loan_count(), 2)

    def test_get_active_loans(self):
        """
        5.2 Get active loans.
        Test that active loans are correctly returned
        """
        student = user.Student("s001", "John Doe", "password123", "IT")
        loan1 = {'book_ID': 'b001', 'returned_date': None}
        loan2 = {'book_ID': 'b002', 'returned_date': '10/09/2025'}
        loan3 = {'book_ID': 'b003', 'returned_date': None}
        student.loans = [loan1, loan2, loan3]
        
        active_loans = student.get_active_loans()
        self.assertEqual(len(active_loans), 2)
        self.assertIn(loan1, active_loans)
        self.assertIn(loan3, active_loans)
        self.assertNotIn(loan2, active_loans)



    def test_str_representation(self):
        """
        6.1 String representation.
        Test that string representation is correct
        """
        student = user.Student("s001", "John Doe", "password123", "IT")
        self.assertEqual(str(student), "John Doe (Student)")

    def test_multiple_users_in_list(self):
        """
        6.2 Multiple users in list.
        Test that multiple users are correctly added to users list
        """
        student = user.Student("s001", "John Doe", "password123", "IT")
        staff = user.Staff("e001", "Jane Smith", "password456", "Library")
        others = user.Others("o001", "Bob Wilson", "password789")
        
        self.assertEqual(len(user.User.users), 3)
        self.assertIn(student, user.User.users)
        self.assertIn(staff, user.User.users)
        self.assertIn(others, user.User.users)

    def test_valid_departments(self):
        """
        6.3 Valid departments.
        Test that all valid departments are accepted
        """
        valid_departments = ["IT", "Business", "Arts", "Science", "Engineering", "Education", "Medicine", "Library"]
        
        for dept in valid_departments:
            user.User.users.clear()  # Clear for each iteration
            student = user.Student(f"s{dept}", "John Doe", "password123", dept)
            self.assertEqual(student.department, dept)
            
            staff = user.Staff(f"e{dept}", "Jane Smith", "password456", dept)
            self.assertEqual(staff.department, dept)

    def test_get_total_fines_no_overdue(self):
        """
        7.1 Get total fines - no overdue books.
        Test that total fines is 0 when no books are overdue
        """
        student = user.Student("s001", "John Doe", "password123", "IT")
        student.loans = [
            {
                'book_ID': 'P001',
                'type': 'physical',
                'due_date': '20/09/2025',  # Future date
                'returned_date': None
            }
        ]
        total_fines = student.get_total_fines("15/09/2025")
        self.assertEqual(total_fines, 0.0)

    def test_get_total_fines_with_overdue(self):
        """
        7.2 Get total fines - with overdue books.
        Test that total fines is calculated correctly for overdue books
        """
        student = user.Student("s001", "John Doe", "password123", "IT")
        student.loans = [
            {
                'book_ID': 'P001',
                'type': 'physical',
                'due_date': '10/09/2025',  # 5 days overdue
                'returned_date': None
            }
        ]
        # Student has 0 grace days, 1.0 fine per day
        # 5 days overdue * 1.0 = 5.0
        total_fines = student.get_total_fines("15/09/2025")
        self.assertEqual(total_fines, 5.0)

    def test_get_total_fines_staff_with_grace(self):
        """
        7.3 Get total fines - staff with grace period.
        Test that staff grace period is considered in fine calculation
        """
        staff = user.Staff("e001", "Jane Smith", "password456", "Library")
        staff.loans = [
            {
                'book_ID': 'P001',
                'type': 'physical',
                'due_date': '10/09/2025',  # 5 days overdue
                'returned_date': None
            }
        ]
        # Staff has 2 grace days, 0.5 fine per day
        # (5 - 2) days overdue * 0.5 = 1.5
        total_fines = staff.get_total_fines("15/09/2025")
        self.assertEqual(total_fines, 1.5)

    def test_get_total_fines_returned_books_ignored(self):
        """
        7.4 Get total fines - returned books ignored.
        Test that returned books are not included in fine calculation
        """
        student = user.Student("s001", "John Doe", "password123", "IT")
        student.loans = [
            {
                'book_ID': 'P001',
                'type': 'physical',
                'due_date': '10/09/2025',
                'returned_date': '12/09/2025'  # Already returned
            },
            {
                'book_ID': 'P002',
                'type': 'physical',
                'due_date': '10/09/2025',
                'returned_date': None
            }
        ]
        total_fines = student.get_total_fines("15/09/2025")
        self.assertEqual(total_fines, 5.0)  # Only P002 counts

    def test_get_total_fines_online_books_ignored(self):
        """
        7.5 Get total fines - online books ignored.
        Test that online books are not included in fine calculation
        """
        student = user.Student("s001", "John Doe", "password123", "IT")
        student.loans = [
            {
                'book_ID': 'O001',
                'type': 'online',
                'due_date': '10/09/2025',
                'returned_date': None
            }
        ]
        total_fines = student.get_total_fines("15/09/2025")
        self.assertEqual(total_fines, 0.0)

    def test_get_overdue_loans(self):
        """
        7.6 Get overdue loans.
        Test that overdue loans are correctly identified
        """
        student = user.Student("s001", "John Doe", "password123", "IT")
        loan1 = {
            'book_ID': 'P001',
            'type': 'physical',
            'due_date': '10/09/2025',  # Overdue
            'returned_date': None
        }
        loan2 = {
            'book_ID': 'P002',
            'type': 'physical',
            'due_date': '20/09/2025',  # Not overdue
            'returned_date': None
        }
        loan3 = {
            'book_ID': 'P003',
            'type': 'physical',
            'due_date': '05/09/2025',  # Overdue
            'returned_date': None
        }
        student.loans = [loan1, loan2, loan3]
        
        overdue_loans = student.get_overdue_loans("15/09/2025")
        self.assertEqual(len(overdue_loans), 2)
        self.assertIn(loan1, overdue_loans)
        self.assertIn(loan3, overdue_loans)
        self.assertNotIn(loan2, overdue_loans)

    def test_can_renew_valid(self):
        """
        7.7 Can renew - valid renewal.
        Test that valid renewal returns True
        """
        student = user.Student("s001", "John Doe", "password123", "IT")
        student.loans = [
            {
                'book_id': 'P001',
                'type': 'physical',
                'due_date': '20/09/2025',  # Not overdue
                'returned_date': None,
                'renewed': False
            }
        ]
        can_renew, message = student.can_renew('P001', "15/09/2025")
        self.assertTrue(can_renew)
        self.assertEqual(message, "")

    def test_can_renew_already_renewed(self):
        """
        7.8 Can renew - already renewed.
        Test that already renewed book cannot be renewed again
        """
        student = user.Student("s001", "John Doe", "password123", "IT")
        student.loans = [
            {
                'book_id': 'P001',
                'type': 'physical',
                'due_date': '20/09/2025',
                'returned_date': None,
                'renewed': True
            }
        ]
        can_renew, message = student.can_renew('P001', "15/09/2025")
        self.assertFalse(can_renew)
        self.assertEqual(message, "该书已续借过，不能再次续借。")

    def test_can_renew_overdue(self):
        """
        7.9 Can renew - overdue book.
        Test that overdue book cannot be renewed
        """
        student = user.Student("s001", "John Doe", "password123", "IT")
        student.loans = [
            {
                'book_id': 'P001',
                'type': 'physical',
                'due_date': '10/09/2025',  # Overdue
                'returned_date': None,
                'renewed': False
            }
        ]
        can_renew, message = student.can_renew('P001', "15/09/2025")
        self.assertFalse(can_renew)
        self.assertEqual(message, "该书已逾期，不能续借。")

    def test_can_renew_not_found(self):
        """
        7.10 Can renew - book not found.
        Test that non-existing loan cannot be renewed
        """
        student = user.Student("s001", "John Doe", "password123", "IT")
        student.loans = []
        can_renew, message = student.can_renew('P001', "15/09/2025")
        self.assertFalse(can_renew)
        self.assertEqual(message, "未找到可续借的借阅记录。")

    def test_has_renewed_true(self):
        """
        7.11 Has renewed - true case.
        Test that renewed book is correctly identified
        """
        student = user.Student("s001", "John Doe", "password123", "IT")
        student.loans = [
            {
                'book_ID': 'P001',
                'type': 'physical',
                'returned_date': None,
                'renewed': True
            }
        ]
        self.assertTrue(student.has_renewed('P001'))

    def test_has_renewed_false(self):
        """
        7.12 Has renewed - false case.
        Test that non-renewed book is correctly identified
        """
        student = user.Student("s001", "John Doe", "password123", "IT")
        student.loans = [
            {
                'book_ID': 'P001',
                'type': 'physical',
                'returned_date': None,
                'renewed': False
            }
        ]
        self.assertFalse(student.has_renewed('P001'))

    def test_has_renewed_not_found(self):
        """
        7.13 Has renewed - book not found.
        Test that non-existing loan returns False
        """
        student = user.Student("s001", "John Doe", "password123", "IT")
        student.loans = []
        self.assertFalse(student.has_renewed('P001'))

    def test_get_fine_policy_student(self):
        """
        7.14 Get fine policy - student.
        Test that student fine policy is correct
        """
        student = user.Student("s001", "John Doe", "password123", "IT")
        grace, fine_per_day = student.get_fine_policy()
        self.assertEqual(grace, 0)
        self.assertEqual(fine_per_day, 1.0)

    def test_get_fine_policy_staff(self):
        """
        7.15 Get fine policy - staff.
        Test that staff fine policy is correct
        """
        staff = user.Staff("e001", "Jane Smith", "password456", "Library")
        grace, fine_per_day = staff.get_fine_policy()
        self.assertEqual(grace, 2)
        self.assertEqual(fine_per_day, 0.5)

    def test_get_fine_policy_others(self):
        """
        7.16 Get fine policy - others.
        Test that others fine policy is correct
        """
        others = user.Others("o001", "Bob Wilson", "password789")
        grace, fine_per_day = others.get_fine_policy()
        self.assertEqual(grace, 0)
        self.assertEqual(fine_per_day, 1.0)
    
    def test_load_users_from_csv_file_not_found(self):
        """
        8.1 Load users from CSV - file not found.
        Test that FileNotFoundError is raised when CSV file doesn't exist
        """
        user.User.users.clear()
        with self.assertRaises(FileNotFoundError):
            user.User.load_users_from_csv("nonexistent_file.csv")

    def test_load_users_from_csv_errors(self):
        """
        8.2 Load users from CSV - error cases.
        Test various error conditions when loading CSV
        """
        import tempfile
        import os
        
        user.User.users.clear()
        
        # Test missing required field
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as f:
            f.write("user_id,name,password\n")  # Missing role field
            f.write("s001,John Doe,password123\n")
            temp_file = f.name
        
        try:
            with self.assertRaises(MissingRequiredFieldError):
                user.User.load_users_from_csv(temp_file)
        finally:
            os.unlink(temp_file)
        
        # Test empty required field
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as f:
            f.write("user_id,name,password,role\n")
            f.write("s001,,password123,Student\n")  # Empty name field
            temp_file = f.name
        
        try:
            with self.assertRaises(MissingRequiredFieldError):
                user.User.load_users_from_csv(temp_file)
        finally:
            os.unlink(temp_file)
        
        # Test invalid user creation
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as f:
            f.write("user_id,name,password,role\n")
            f.write("invalid_id,John Doe,password123,Student\n")  # Invalid user_id format
            temp_file = f.name
        
        try:
            with self.assertRaises(CustomError):
                user.User.load_users_from_csv(temp_file)
        finally:
            os.unlink(temp_file)

    def test_load_users_from_csv_valid_data(self):
        """
        8.5 Load users from CSV - valid data.
        Test successful loading of valid CSV data
        """
        import tempfile
        import os
        
        user.User.users.clear()
        
        # Create a temporary CSV file with valid data
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as f:
            f.write("user_id,name,password,role\n")
            f.write("s001,John Doe,password123,Student\n")
            f.write("e001,Jane Smith,password456,Staff\n")
            f.write("o001,Bob Wilson,password789,Others\n")
            temp_file = f.name
        
        try:
            user.User.load_users_from_csv(temp_file)
            self.assertEqual(len(user.User.users), 3)
            
            # Check that users were created correctly
            student = user.User.find_user_by_id("s001")
            self.assertIsInstance(student, user.Student)
            self.assertEqual(student.name, "John Doe")
            
            staff = user.User.find_user_by_id("e001")
            self.assertIsInstance(staff, user.Staff)
            self.assertEqual(staff.name, "Jane Smith")
            
            others = user.User.find_user_by_id("o001")
            self.assertIsInstance(others, user.Others)
            self.assertEqual(others.name, "Bob Wilson")
            
        finally:
            os.unlink(temp_file)

    def test_load_users_from_csv_with_department(self):
        """
        8.6 Load users from CSV - with department.
        Test loading CSV data that includes department information
        """
        import tempfile
        import os
        
        user.User.users.clear()
        
        # Create a temporary CSV file with department data
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as f:
            f.write("user_id,name,password,role,department\n")
            f.write("s001,John Doe,password123,Student,IT\n")
            f.write("e001,Jane Smith,password456,Staff,Library\n")
            temp_file = f.name
        
        try:
            user.User.load_users_from_csv(temp_file)
            self.assertEqual(len(user.User.users), 2)
            
            student = user.User.find_user_by_id("s001")
            self.assertEqual(student.department, "IT")
            
            staff = user.User.find_user_by_id("e001")
            self.assertEqual(staff.department, "Library")
            
        finally:
            os.unlink(temp_file)
    
if __name__ == "__main__":
    unittest.main()
