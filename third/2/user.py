from abc import ABC, abstractmethod
import csv
import datetime
import re

TODAY = "15/09/2025"

class User(ABC):
    """
    an abstract parent class representing all kinds of library users
    """
    # a list of all library users
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
    def get_policy(self) -> dict:
        """返回用户的借阅政策，包含days_allowed和quota"""
        pass

    def get_active_loans(self):
        """返回所有未归还的借阅记录"""
        return [l for l in self.loans if not l.get('returned_date')]

    def get_loan_count(self):
        physical = sum(1 for loan in self.loans if loan['type'] == 'physical' and not loan.get('returned_date'))
        online = sum(1 for loan in self.loans if loan['type'] == 'online' and not loan.get('returned_date'))
        total = physical + online
        return total, physical, online

    def get_fine_policy(self):
        # 返回罚款策略（宽限期、每日罚款）
        if self.role == 'Student':
            return 0, 0.5
        elif self.role == 'Staff':
            return 2, 0.5
        else:
            return 0, 1.0

    def get_total_fines(self, today_str=None):
        # 计算所有未归还的实体书罚款总额
        total_fine = 0.0
        grace, fine_per_day = self.get_fine_policy()
        today = datetime.datetime.strptime(today_str or TODAY, '%d/%m/%Y')
        for loan in self.loans:
            if loan['type'] == 'physical' and not loan.get('returned_date'):
                due = datetime.datetime.strptime(loan['due_date'], '%d/%m/%Y')
                overdue_days = (today - due).days - grace
                if overdue_days > 0:
                    total_fine += overdue_days * fine_per_day
        return total_fine

    def get_overdue_loans(self, today_str=None):
        # 返回所有逾期未还的实体书借阅记录
        grace, _ = self.get_fine_policy()
        today = datetime.datetime.strptime(today_str or TODAY, '%d/%m/%Y')
        overdue = []
        for loan in self.loans:
            if loan['type'] == 'physical' and not loan.get('returned_date'):
                due = datetime.datetime.strptime(loan['due_date'], '%d/%m/%Y')
                overdue_days = (today - due).days - grace
                if overdue_days > 0:
                    overdue.append(loan)
        return overdue
    #静态方法
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
        super().__init__(user_ID, name, password, role="Student", department=department)
    
    def get_policy(self) -> dict:
        return {"days_allowed": 10, "quota": 4}

class Staff(User):
    def __init__(self, user_ID, name, password, department):
        super().__init__(user_ID, name, password, role="Staff", department=department)
    
    def get_policy(self) -> dict:
        return {"days_allowed": 14, "quota": 6}

class Others(User):
    def __init__(self, user_ID, name, password):
        super().__init__(user_ID, name, password, role="Others", department="")
    
    def get_policy(self) -> dict:
        return {"days_allowed": 7, "quota": 2}
        