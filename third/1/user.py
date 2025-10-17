from abc import ABC, abstractmethod
import csv

class User(ABC):
    users = []

    def __init__(self, user_ID, name, password, role, department):
        self.user_ID = user_ID
        self.name = name
        self.password = password
        self.role = role
        self.department = department or ""
        self.loans = []
        User.users.append(self)

    def __str__(self):
        return f"{self.name} ({self.role})"

    def is_library_staff(self) -> bool:
        return self.role == "Staff" and self.department == "Library"

    def check_password(self, password):
        return self.password == password

    @abstractmethod
    def get_policy(self) -> dict[str, int]:
        pass

    def get_loan_count(self):
        physical = sum(1 for loan in self.loans if loan['type'] == 'physical' and not loan.get('returned_date'))
        online = sum(1 for loan in self.loans if loan['type'] == 'online' and not loan.get('returned_date'))
        total = physical + online
        return total, physical, online

    def get_active_loans(self):
        return [l for l in self.loans if not l.get('returned_date')]

    @staticmethod
    def find_user_by_id(user_id):
        for user in User.users:
            if user.user_ID == user_id:
                return user
        return None

    @staticmethod
    def load_users_from_csv(file_path):
        User.users.clear()
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                user_id = row['user_id']
                name = row['name']
                password = row['password']
                role = row['role']
                department = row.get('department', "")
                if user_id.startswith('s'):
                    Student(user_id, name, password, department)
                elif user_id.startswith('e'):
                    Staff(user_id, name, password, department)
                elif user_id.startswith('o'):
                    Others(user_id, name, password)

class Student(User):
    def __init__(self, user_ID, name, password, department):
        super().__init__(user_ID, name, password, "Student", department)
    def get_policy(self):
        return {"days_allowed": 10, "quota": 4}

class Staff(User):
    def __init__(self, user_ID, name, password, department):
        super().__init__(user_ID, name, password, "Staff", department)
    def get_policy(self):
        return {"days_allowed": 14, "quota": 6}

class Others(User):
    def __init__(self, user_ID, name, password):
        super().__init__(user_ID, name, password, "Others", "")
    def get_policy(self):
        return {"days_allowed": 7, "quota": 2}
        
        

