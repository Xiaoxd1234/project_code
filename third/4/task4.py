from custom_errors import *

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
            try:
                user_id = input("Login as: ").strip()
                if user_id.lower() == "quit":
                    print("Goodbye!")
                    return
                if not user_id:
                    raise CustomValueError("User ID cannot be empty")
                
                password = input("Password: ").strip()
                if not password:
                    raise CustomValueError("Password cannot be empty")
                
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
            except CustomValueError as e:
                print(f"Input error: {e}")
            except Exception as e:
                print(f"Unexpected error during login: {e}")
        if not current_user:
            continue
        # 登录成功，进入主菜单
        print(f"Logged in as {current_user}")  # 只在登录成功后显示一次
        while True:
            print("="*34)
            print("My Library Account")
            print("0. Quit")
            print("1. Log out")
            print("2. View account policies")
            print("3. View my loans")
            print("4. Borrow and Return")
            print("5. Search by Keywords")
            if current_user.is_library_staff():
                print("6. Manage Library")
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
                    fines = current_user.get_total_fines()
                    print(f"{current_user.role} {current_user.name}. Policies: maximum of {current_user.days_allowed} days, {current_user.quota} items. Current loans: {total} ({physical} physical / {online} online). Fines: $ {fines:.2f}")
                    break
                elif choice == "3":
                    active_loans = [l for l in current_user.loans if not l['returned_date']]
                    print(f"You currently have {len(active_loans)} loan(s).")
                    for idx, l in enumerate(sorted(active_loans, key=lambda x: x['due_date'])):
                        b = book.Book.find_book_by_id(l['book_ID'])
                        print(f"{idx+1}. {b}\n Due date: {l['due_date']}.")
                    break
                elif choice == "4":
                    # Borrow and Return console
                    while True:
                        cmd = input("> ").strip()
                        if cmd.lower() == "quit":
                            break
                        elif cmd.lower().startswith("borrow "):
                            query = cmd[7:].strip()
                            # 查找书籍
                            matches = [b for b in book.Book.books if b.book_ID.lower() == query.lower() or b.title.lower() == query.lower()]
                            if not matches:
                                matches = [b for b in book.Book.books if query.lower() in b.title.lower()]
                            if not matches:
                                print(f"No books match '{query}'.")
                                continue
                            matches.sort(key=lambda b: b.book_ID)
                            print(f"Found {len(matches)} book(s).")
                            for b in matches:
                                active = b.get_active_loan_count(loans)
                                avail = b.available_copies(active)
                                print(f"- {b.book_ID} ({b.book_type}) '{b.title}' by {b.author} ({b.year}). Available copies: {avail}/{b.total_copy}.")
                            # 让用户确认ID
                            valid_ids = [b.book_ID for b in matches]
                            while True:
                                confirm_id = input("Confirm the Book ID you'd like to borrow: ").strip()
                                if confirm_id.lower() == "quit":
                                    break
                                if confirm_id not in valid_ids:
                                    continue
                                b = book.Book.find_book_by_id(confirm_id)
                                #这里不用再次检测的因为前边valid_ids已经判断过有效性了，所以肯定不会返回none，但是因为函数中返回了none，
                                # 所以这里语法上要写一下检测，才能合适的利用后续b的属性，虽然这种情况根本不用检测
                                if b is None:
                                    print("未找到该书籍ID，请重新输入。")
                                    continue
                                # 先检查额度和罚款
                                total, physical, online = current_user.get_loan_count()
                                fines = current_user.get_total_fines()
                                try:
                                    if fines > 0:
                                        raise CustomOperationError("Borrowing unavailable: unpaid fines. Review your loan details for more info.")
                                    if total >= current_user.quota:
                                        raise CustomLimitError("Borrowing unavailable: quota exceeded. Review your loan details for more info.")
                                    if not b.can_borrow(loans):
                                        raise CustomOperationError("No available copies.")
                                    
                                    # 借书成功
                                    due_date = (datetime.datetime.strptime(user.TODAY, '%d/%m/%Y') + datetime.timedelta(days=current_user.days_allowed)).strftime('%d/%m/%Y')
                                    new_loan = {'user_ID': current_user.user_ID, 'book_ID': b.book_ID, 'borrow_date': user.TODAY, 'due_date': due_date, 'returned_date': '', 'type': b.book_type}
                                    loans.append(new_loan)
                                    current_user.loans.append(new_loan)
                                    print(f"You have borrowed '{b.title}' by {b.author} ({b.year}). Due: {due_date}.")
                                    break
                                except CustomError as e:
                                    print(f"Borrowing error: {e}")
                                    break
                        elif cmd.lower().startswith("return "):
                            return_id = cmd[7:].strip()
                            # 找到最早到期的未归还副本
                            active_loans = [l for l in current_user.loans if l['book_ID'] == return_id and not l['returned_date']]
                            if not active_loans:
                                print(f"No loan record for {return_id}.")
                                continue
                            loan_to_return = sorted(active_loans, key=lambda l: l['due_date'])[0]
                            #跟前边一样同样的道理，因为后边调用了b.的各种属性，所以语法上这里要判断一下，当然前边已经判断过了，
                            # 所以这里这种情况肯定不会出现none的情况但是语法上还是要写一下，因为后边写到了b.的属性
                            b = book.Book.find_book_by_id(return_id)
                            if b is None:
                                print(f"未找到ID为{return_id}的书籍信息。")
                                continue
                            # 计算罚款
                            grace, fine_per_day = current_user.get_fine_policy()
                            due = datetime.datetime.strptime(loan_to_return['due_date'], '%d/%m/%Y')
                            today = datetime.datetime.strptime(user.TODAY, '%d/%m/%Y')
                            overdue_days = (today - due).days - grace
                            fine = 0.0
                            if b.is_physical_book() and overdue_days > 0:
                                fine = overdue_days * fine_per_day
                                print(f"Returned '{b.title}' by {b.author} ({b.year}). Overdue by {overdue_days} day(s). Fine: $ {fine:.2f}")
                            else:
                                print(f"Returned '{b.title}' by {b.author} ({b.year}).")
                            try:
                                if not loan_to_return:
                                    raise CustomOperationError(f"No loan record for {return_id}.")
                                if b is None:
                                    raise BookNotFoundError(f"Book with ID {return_id} not found.")
                                
                                # 计算罚款
                                grace, fine_per_day = current_user.get_fine_policy()
                                due = datetime.datetime.strptime(loan_to_return['due_date'], '%d/%m/%Y')
                                today = datetime.datetime.strptime(user.TODAY, '%d/%m/%Y')
                                overdue_days = (today - due).days - grace
                                fine = 0.0
                                if b.is_physical_book() and overdue_days > 0:
                                    fine = overdue_days * fine_per_day
                                    print(f"Returned '{b.title}' by {b.author} ({b.year}). Overdue by {overdue_days} day(s). Fine: $ {fine:.2f}")
                                else:
                                    print(f"Returned '{b.title}' by {b.author} ({b.year}).")
                                loan_to_return['returned_date'] = user.TODAY
                            except CustomError as e:
                                print(f"Return error: {e}")
                        elif cmd.lower().startswith("renew "):
                            renew_id = cmd[6:].strip()
                            # 找到最早到期且未归还的副本
                            active_loans = [l for l in current_user.loans if l['book_ID'] == renew_id and not l.get('returned_date')]
                            if not active_loans:
                                print(f"No loan record for {renew_id}.")
                                continue
                            loan_to_renew = sorted(active_loans, key=lambda l: l['due_date'])[0]
                            b = book.Book.find_book_by_id(renew_id)
                            if b is None:
                                print(f"未找到ID为{renew_id}的书籍信息。")
                                continue
                            # 续借资格判断
                            fines = current_user.get_total_fines()
                            if fines > 0:
                                print("Renewal denied: You have unpaid fines.")
                                continue
                            if current_user.has_renewed(renew_id):
                                print("Renewal unavailable: Each book can only be renewed once.")
                                continue
                            due = datetime.datetime.strptime(loan_to_renew['due_date'], '%d/%m/%Y')
                            today = datetime.datetime.strptime(user.TODAY, '%d/%m/%Y')
                            new_due = due + datetime.timedelta(days=5)
                            if new_due < today:
                                print("Renewal denied: This book is already overdue.")
                                continue
                            # 续借成功
                            try:
                                if not loan_to_renew:
                                    raise CustomOperationError(f"No loan record for {renew_id}.")
                                if b is None:
                                    raise BookNotFoundError(f"Book with ID {renew_id} not found.")
                                
                                # 续借资格判断
                                fines = current_user.get_total_fines()
                                if fines > 0:
                                    raise CustomOperationError("Renewal denied: You have unpaid fines.")
                                if current_user.has_renewed(renew_id):
                                    raise CustomLimitError("Renewal unavailable: Each book can only be renewed once.")
                                due = datetime.datetime.strptime(loan_to_renew['due_date'], '%d/%m/%Y')
                                today = datetime.datetime.strptime(user.TODAY, '%d/%m/%Y')
                                new_due = due + datetime.timedelta(days=5)
                                if new_due < today:
                                    raise CustomDateError("Renewal denied: This book is already overdue.")
                                
                                # 续借成功
                                loan_to_renew['due_date'] = new_due.strftime('%d/%m/%Y')
                                loan_to_renew['renewed'] = True
                                print(f"Renew '{b.title}' by {b.author} ({b.year}) successfully. New due date: {loan_to_renew['due_date']}")
                            except CustomError as e:
                                print(f"Renewal error: {e}")
                        else:
                            continue
                    break
                elif choice == "5":
                    # 按关键词搜索
                    keywords_input = input("Enter search keywords (separated by comma): ").strip()
                    keywords = [k.strip().lower() for k in keywords_input.split(",") if k.strip()]
                    if not keywords:
                        print("Found 0 book(s).")
                        break
                    results = []
                    for b in book.Book.books:
                        match_count = b.match_keywords(keywords)
                        if match_count > 0:
                            results.append((b, match_count))
                    # 排序：匹配数量（降序）、年份（降序）、ID（升序）
                    results.sort(key=lambda x: (-x[1], -int(x[0].year), x[0].book_ID))
                    print(f"Found {len(results)} book(s).")
                    for idx, (b, _) in enumerate(results):
                        print(f"{idx+1}. {b.book_ID} '{b.title}' by {b.author} ({b.year}).")
                    break
                elif choice == "6" and current_user.is_library_staff():
                    # Manage Library
                    while True:
                        cmd = input("> ").strip().lower()
                        if cmd == "quit":
                            break
                        elif cmd == "report":
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
                        elif cmd == "add physical":
                            title = input("Title: ").strip()
                            author = input("Authors: ").strip()
                            year = input("Year: ").strip()
                            copies = input("Copies: ").strip()
                            if not title or not author or not year or not copies:
                                print("All fields are required.")
                                continue
                            try:
                                year = int(year)
                                total_copy = int(copies)
                                if total_copy <= 0:
                                    print("Number of copies must be positive.")
                                    continue
                            except ValueError:
                                print("Year and copies must be numbers.")
                                continue
                            # 自动分配ID和关键词
                            new_id = book.Book.generate_new_id("physical")
                            all_keywords = book.Book.get_all_keywords()
                            auto_keywords = book.Book.extract_keywords_from_title(title, all_keywords)
                            new_book = book.Book(new_id, "physical", total_copy, title, author, year, auto_keywords)
                            print(f"Detected keywords: {':'.join(auto_keywords) if auto_keywords else 'None'}")
                            print(f"Adding {new_id} '{title}' by {author} ({year}).")
                        elif cmd == "add online":
                            title = input("Title: ").strip()
                            author = input("Authors: ").strip()
                            year = input("Year: ").strip()
                            if not title or not author or not year:
                                print("All fields are required.")
                                continue
                            try:
                                year = int(year)
                            except ValueError:
                                print("Year must be a number.")
                                continue
                            # 自动分配ID和关键词
                            new_id = book.Book.generate_new_id("online")
                            all_keywords = book.Book.get_all_keywords()
                            auto_keywords = book.Book.extract_keywords_from_title(title, all_keywords)
                            new_book = book.Book(new_id, "online", 0, title, author, year, auto_keywords)
                            print(f"Detected keywords: {':'.join(auto_keywords) if auto_keywords else 'None'}")
                            print(f"Adding {new_id} '{title}' by {author} ({year}).")
                        else:
                            continue
                    break
                # Invalid choice - continue the inner loop to re-prompt without reprinting menu
            
            if choice == "1":  # Log out
                break

if __name__ == "__main__":
    main('data/users.csv', 'data/books.csv', 'data/loans.csv')
