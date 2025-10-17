from abc import ABC, abstractmethod
import csv
import datetime
import re
from custom_errors import *
TODAY = "15/09/2025"

class User(ABC):
    """
    an abstract parent class representing all kinds of library users
    """
    # a list of all library users
    users = []

    def __init__(self, user_ID, name, password, role, department):
        # Validate user ID
        if not user_ID or not isinstance(user_ID, str):
            raise CustomValueError("User ID must be a non-empty string")
        
        # Validate name
        if not name or not all(word.isalpha() for word in name.split()):
            raise CustomValueError("Name must contain only alphabetic characters")
        
        # Validate password
        if not password:
            raise CustomValueError("Password cannot be empty")
        
        # Validate department
        valid_departments = ["IT", "Business", "Arts", "Science", "Engineering", "Education", "Medicine", "Library"]
        if role in ["Student", "Staff"] and department not in valid_departments:
            raise CustomValueError(f"Invalid department for {role}: {department}")
        if role == "Others" and department:
            raise CustomValueError("Department must be empty for Others")
        
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

    @abstractmethod
    def get_policy(self)->dict:
        """返回用户的借阅政策信息"""
        pass

    def get_active_loans(self):
        """返回用户的活跃借阅记录"""
        return [loan for loan in self.loans if not loan.get('returned_date')]

    def check_password(self, password):
        return self.password == password

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

    def can_renew(self, book_id, today_str=None):
        # 判断用户是否可以续借指定书籍
        for loan in self.loans:
            if loan['book_id'] == book_id and loan['type'] == 'physical' and not loan.get('returned_date'):
                # 已续借过不可再续借
                if loan.get('renewed'):
                    return False, "该书已续借过，不能再次续借。"
                # 已逾期不可续借
                grace, _ = self.get_fine_policy()
                today = datetime.datetime.strptime(today_str or TODAY, '%d/%m/%Y')
                due = datetime.datetime.strptime(loan['due_date'], '%d/%m/%Y')
                overdue_days = (today - due).days - grace
                if overdue_days > 0:
                    return False, "该书已逾期，不能续借。"
                return True, ""
        return False, "未找到可续借的借阅记录。"

    def has_renewed(self, book_id):
        # 判断某本书是否已续借过
        for loan in self.loans:
            if loan['book_ID'] == book_id and loan['type'] == 'physical' and not loan.get('returned_date'):
                return loan.get('renewed', False)
        return False
    #静态方法
    @staticmethod
    def find_user_by_id(user_id):
        for user in User.users:
            if user.user_ID == user_id:
                return user
        return None

    @staticmethod
    def load_users_from_csv(file_path):
        from custom_errors import MissingRequiredFieldError, CustomValueError
        User.users.clear()
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                user_id = row.get('user_id')
                name = row.get('name')
                password = row.get('password')
                role = row.get('role')
                department = row.get('department', "")
                
                # 必填字段检查
                if not user_id or not name or not password or not role:
                    raise MissingRequiredFieldError(f"Missing required field in user record: {row}")
                
                # 创建用户对象时处理可能的异常
                try:
                    if user_id.startswith('s'):
                        Student(user_id, name, password, department)
                    elif user_id.startswith('e'):
                        Staff(user_id, name, password, department)
                    elif user_id.startswith('o'):
                        Others(user_id, name, password)
                    else:
                        raise CustomValueError(f"Invalid user ID format: {user_id}")
                except Exception as e:
                    raise CustomValueError(f"Invalid user record: {row}, error: {e}")

class Student(User):
    def __init__(self, user_ID, name, password, department):
        super().__init__(user_ID, name, password, role="Student", department=department)

    def get_policy(self):
        """返回学生的借阅政策"""
        return {
            'days_allowed': 10,
            'quota': 4
        }

class Staff(User):
    def __init__(self, user_ID, name, password, department):
        super().__init__(user_ID, name, password, role="Staff", department=department)

    def get_policy(self):
        """返回员工的借阅政策"""
        return {
            'days_allowed': 14,
            'quota': 6
        }

class Others(User):
    def __init__(self, user_ID, name, password):
        super().__init__(user_ID, name, password, role="Others", department="")

    def get_policy(self):
        """返回其他用户的借阅政策"""
        return {
            'days_allowed': 7,
            'quota': 2
        }
        