import user
import book
import csv
import datetime

class loan:
    """
    Loan record class
    """
    def __init__(self, user_ID, book_ID, borrow_date, due_date, returned_date):
        self.user_ID = user_ID
        self.book_ID = book_ID
        self.borrow_date = borrow_date
        self.due_date = due_date
        self.returned_date = returned_date

    @staticmethod
    def load_loans_from_csv(file_path):
        loans = []
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                loans.append({
                    'user_ID': row['user_id'],
                    'book_ID': row['book_id'],
                    'borrow_date': row['borrow_date'],
                    'due_date': row['due_date'],
                    'returned_date': row['return_date']
                })
        return loans


def load_data(user_file, book_file, loan_file):
    user.User.load_users_from_csv(user_file)
    book.Book.load_books_from_csv(book_file)
    loans = loan.load_loans_from_csv(loan_file)
    # 关联用户和图书的借阅信息
    for l in loans:
        u = user.User.find_user_by_id(l['user_ID'])
        b = book.Book.find_book_by_id(l['book_ID'])
        if u and b:
            l['type'] = b.book_type
            u.loans.append(l)
    return loans


def main(user_file: str, book_file:str, loan_file:str) -> None:
    loans = load_data(user_file, book_file, loan_file)
    while True:
        print("Welcome to Library")
        attempts = 3
        current_user = None
        while attempts > 0:
            user_id = input("Login as: ").strip()
            if user_id.lower() == "quit":
                print("Goodbye!")
                return
            password = input("Password: ").strip()
            u = user.User.find_user_by_id(user_id)
            if not u or not u.check_password(password):
                attempts -= 1
                if attempts > 0:
                    print(f"Invalid credentials. {attempts} attempt(s) remaining.")
                else:
                    print("Sorry you're out of attempts. Please contact your librarian for assistance.")
            else:
                current_user = u
                break
        if not current_user:
            continue
        # 登录成功，进入主菜单
        while True:
            print(f"Logged in as {current_user}")
            print("="*34)
            print("My Library Account")
            print("0. Quit")
            print("1. Log out")
            print("2. View account policies")
            print("3. View my loans")
            if current_user.is_library_staff():
                print("4. Library Report")
            print("="*34)
            
            while True:
                choice = input("Enter your choice: ").strip()
                if choice == "0" or choice.lower() == "quit":
                    print("Goodbye!")
                    return
                elif choice == "1":
                    break
                elif choice == "2":
                    total, physical, online = current_user.get_loan_count()
                    print(f"{current_user.role} {current_user.name}. Policies: maximum of {current_user.days_allowed} days, {current_user.quota} items. Current loans: {total} ({physical} physical / {online} online).")
                    break
                elif choice == "3":
                    active_loans = [l for l in current_user.loans if not l['returned_date']]
                    print(f"You currently have {len(active_loans)} loan(s).")
                    for idx, l in enumerate(sorted(active_loans, key=lambda x: x['due_date'])):
                        b = book.Book.find_book_by_id(l['book_ID'])
                        print(f"{idx+1}. {b}\n Due date: {l['due_date']}.")
                    break
                elif choice == "4" and current_user.is_library_staff():
                    # 图书馆报告
                    students = [u for u in user.User.users if u.role == "Student"]
                    staffs = [u for u in user.User.users if u.role == "Staff"]
                    others = [u for u in user.User.users if u.role == "Others"]
                    total_books = len(book.Book.books)
                    physical_books = [b for b in book.Book.books if b.is_physical_book()]
                    online_books = [b for b in book.Book.books if b.is_online_book()]
                    available_physical = sum(1 for b in physical_books if b.available_copies(b.get_active_loan_count(loans)) > 0)
                    print("Library Report")
                    print(f"- {len(user.User.users)} users, including {len(students)} student(s), {len(staffs)} staff and {len(others)} others.")
                    print(f"- {total_books} books, including {len(physical_books)} physical book(s) ({available_physical} currently available) and {len(online_books)} online book(s).")
                    break
                # Invalid choice - continue the inner loop to re-prompt without reprinting menu
            
            if choice == "1":  # Log out
                break

if __name__ == "__main__":
    main('data/users.csv', 'data/books.csv', 'data/loans.csv')
