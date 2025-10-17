import csv
import datetime
import re

class Book:
    """
    the book class that contains all the book variables for a book object
    """
    #实例共享变量
    books = []

    def __init__(self, book_ID, book_type, total_copy, title, author, year, keywords=None):
        self.book_ID = book_ID
        self.book_type = book_type
        self.total_copy = int(total_copy)
        self.title = title
        self.author = author
        self.year = int(year)
        # 支持传入None、list或字符串
        if keywords is None:
            self.keywords = []
        elif isinstance(keywords, list):
            self.keywords = keywords
        elif isinstance(keywords, str):
            self.keywords = []
            if keywords:
                for key in keywords.split(":"):
                    self.keywords.append(key.strip())
        else:
            raise TypeError("keywords must be None, list or str")
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
        for book in Book.books:
            if book.book_ID == book_id:
                return book
        return None

    @staticmethod
    def load_books_from_csv(file_path):
        Book.books.clear()
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                book_ID = row['book_id']
                book_type = row['type']
                total_copy = row['copies']
                title = row['title']
                author = row['author']
                year = row['year']
                keywords = row.get('keywords', "")
                Book(book_ID, book_type, total_copy, title, author, year, keywords)

    def get_active_loan_count(self, loans):
        return sum(1 for loan in loans if loan['book_ID'] == self.book_ID and not loan.get('returned_date'))







