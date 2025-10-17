import csv
import datetime
import re
from custom_errors import CustomValueError, CustomTypeError, MissingRequiredFieldError

class Book:
    """
    the book class that contains all the book variables for a book object
    """
    #实例共享变量
    books = []

    def __init__(self, book_ID, book_type, total_copy, title, author, year, keywords=None):
        
        # 类型检查
        if book_type not in ["physical", "online"]:
            raise CustomValueError(f"Invalid book type: {book_type}")
        if not title or not author or not year:
            raise MissingRequiredFieldError("Title, author, and year are required fields.")
        try:
            self.year = int(year)
            assert self.year > 0, "Year must be positive."
        except Exception:
            raise CustomValueError("Year must be a positive integer.")
        try:
            self.total_copy = int(total_copy)
            assert self.total_copy > 0, "Copies must be positive."
        except Exception:
            raise CustomValueError("Copies must be a positive integer.")
        self.book_ID = book_ID
        self.book_type = book_type
        self.title = title
        self.author = author
        # 关键词处理
        self.keywords = []
        if keywords is None:
            pass
        elif isinstance(keywords, list):
            for key in keywords:
                if not re.fullmatch(r'[A-Za-z0-9\-]+', key.strip()):
                    raise CustomValueError(f"Invalid keyword: {key.strip()}")
                self.keywords.append(key.strip())
        elif isinstance(keywords, str):
            if keywords:
                for key in keywords.split(":"):
                    if not re.fullmatch(r'[A-Za-z0-9\-]+', key.strip()):
                        raise CustomValueError(f"Invalid keyword: {key.strip()}")
                    self.keywords.append(key.strip())
        else:
            raise CustomTypeError("Keywords must be None, list, or str")
        if len(self.keywords) > 5:
            raise CustomValueError("A book can have at most 5 keywords")
        
        # 断言验证对象状态
        assert self.book_ID, "Book ID should never be empty"
        assert self.book_type in ["physical", "online"], "Book type must be valid"
        assert isinstance(self.keywords, list), "Keywords should always be a list"
        
        Book.books.append(self)

    def match_keywords(self, search_keywords):
        # 返回匹配的关键词数量
        return len(set(k.lower() for k in self.keywords) & set(s.lower() for s in search_keywords))

    @staticmethod
    def extract_keywords_from_title(title, all_keywords):
        # 从书名中提取关键词（与现有关键词库比对，返回按字母排序的列表）
        title_words = set(re.findall(r'\w+', title.lower()))
        matched = sorted([kw for kw in all_keywords if kw.lower() in title_words])
        return matched

    @staticmethod
    def generate_new_id(book_type):
        # 生成新书唯一ID
        prefix = 'P' if book_type == 'physical' else 'E'
        ids = [int(b.book_ID[1:]) for b in Book.books if b.book_ID.startswith(prefix) and b.book_ID[1:].isdigit()]
        next_id = max(ids) + 1 if ids else 1
        return f"{prefix}{next_id:04d}"

    @staticmethod
    def get_all_keywords():
        # 获取所有已存在的关键词（去重，按字母排序）
        keywords = set()
        for b in Book.books:
            keywords.update(b.keywords)
        return sorted(keywords)

    def available_copies(self, active_loan_amount):
        if self.is_online_book():
            return 0  # 在线书籍副本数恒为0，但可无限借阅
        active_loan_amount = active_loan_amount or 0
        return max(self.total_copy - active_loan_amount, 0)

    def can_borrow(self, loans):
        if self.is_online_book():
            return True  # 在线书籍总是可借
        active = self.get_active_loan_count(loans)
        return self.available_copies(active) > 0

    def is_physical_book(self) -> bool:
        return self.book_type == "physical"

    def is_online_book(self) -> bool:
        return self.book_type == "online"

    def __str__(self):
        return f"{self.book_ID} '{self.title}' by {self.author} ({self.year})."

    @staticmethod
    def find_book_by_id(book_id):
        from custom_errors import BookNotFoundError
        for book in Book.books:
            if book.book_ID == book_id:
                return book
        raise BookNotFoundError(f"Book with ID {book_id} not found.")

    @staticmethod
    def load_books_from_csv(file_path):
        from custom_errors import MissingRequiredFieldError, CustomValueError, CustomTypeError
        Book.books.clear()
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                book_ID = row.get('book_id')
                book_type = row.get('type')
                total_copy = row.get('copies')
                title = row.get('title')
                author = row.get('author')
                year = row.get('year')
                keywords = row.get('keywords', "")
                # 必填字段检查
                if not book_ID or not book_type or not total_copy or not title or not author or not year:
                    raise MissingRequiredFieldError(f"Missing required field in book record: {row}")
                # 类型和内容检查由Book构造函数完成
                try:
                    Book(book_ID, book_type, total_copy, title, author, year, keywords)
                except Exception as e:
                    raise CustomValueError(f"Invalid book record: {row}, error: {e}")

    def get_active_loan_count(self, loans):
        return sum(1 for loan in loans if loan['book_ID'] == self.book_ID and not loan.get('returned_date'))







