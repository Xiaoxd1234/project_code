Task 1 - Welcome to the Library's Database [8 marks]
You are asked to design and implement a Python-based system for managing a small library. The system should support the following core tasks, including manage users of different types (students, staff, and other members), manage the collection of books in the library and track and update loan records for borrowed books.

Description
The library has provided you with three CSV files containing its current data in the data folder: users.csv for user information, books.csv for book information and loans.csv containing loan history.

In Task 1-3, you can assume all CSV files contain valid data.

You are allowed to modify the import statements in the scaffold or move the import statements to different modules if required; but you are not allowed to import any modules which weren't originally imported in the scaffold.

Users (users.csv)
This file contains details of all registered users:

Fields: user ID, password, name, role, and department (for students and staff only).

User types:

Student (s prefix in the user ID)

Staff (e prefix in the user ID)

Others (o prefix in the user ID)

Each user type follows specific borrowing policies:

Users
Physical
 
book
Online
Quota
Student
10 days
Unlimited
4
Staff
14 days
Unlimited
6
Other
7 days
Unlimited
2
Users
Student
Staff
Other
​
  
Physical book
10 days
14 days
7 days
​
  
Online
Unlimited
Unlimited
Unlimited
​
  
Quota
4
6
2
​
 
​
 

All users can borrow, return, and renew books, as well as view their active loans and loan policies. Only staff can add, update, or view detailed information about users and books. (More detail in Task 2-3).

Books (books.csv)
This file contains information about books in the collection:

Fields: book ID, type (e.g., physical or online), total copies, title, authors, year, and keywords (colon-separated). 

Each book has a unique ID beginning with a character that denotes its category, followed by 4 digits.

Physical books are identified by the prefix P in the Book ID.

Online books (e-book) are identified by the prefix E in the Book ID.

For online books, the total copies field is always 0.

Loans (loans.csv)
This file contains borrowing records:

Fields: user ID, book ID, borrow date, due date, returned date. All dates are in the following format dd/mm/yyyy.

The due date is automatically calculated based on loan policy.

Active loans are those without a returned date.

Your Task
Write a program that reads users, books and loans from files users.csv, books.csv and loans.csv and a simple menu that allow interaction with the data.

You are provided with 3 modules: user.py, book.py and task1.py. Your task is to 

Complete the implementation User and Book class in the users.py and books.py modules. You are allowed to add additional classes and functions if necessary.

Implement the interaction menu in task1.py 

Login Menu
When the program starts, the user is prompted to log in with their ID and password.

If the user id does not exist or user id and password does not match, the program will print "Invalid credentials. x attempt(s) remaining." and prompt user to login again.

Successful login displays a welcome message with the user's name and role.

Users have three login attempts before the program prints a message "Sorry you're out of attempts. Please contact your librarian for assistance." and back to welcome and login menu.

In the login menu, user can type "quit" to terminate the program.

Welcome to Library
Login as: s31267
Password: chr1267
Logged in as Chris Manner (Student)
Main menu
Once logged in, users see a personalized main menu based on their role.

For student, other users, and staff members outside the Library department:

Logged in as Chris Manner (Student)
==================================
My Library Account
0. Quit
1. Log out
2. View account policies
3. View my loans
==================================
Enter your choice:

For staff from the Library department:

Logged in as Mary Alan (Staff)
==================================
My Library Account
0. Quit
1. Log out
2. View account policies
3. View my loans
4. Library Report
==================================
Enter your choice:

A user's input may provide incorrect choice, e.g. 5 or four. In this case your program should prompt for input again.

0. Quit
The program will print the message: "Goodbye!", and terminates.

1. Log out
The user is logged out and returned to the welcome screen and login menu.

2. View account policies
Upon entering 2, the program will display user current membership policies, and their total loans.

Logged in as Chris Manner (Student)
==================================
My Library Account
0. Quit
1. Log out
2. View account policies
3. View my loans
==================================
Enter your choice: 2
Student Chris Manner. Policies: maximum of 10 days, 4 items. Current loans: 2 (1 physical / 1 online).

3. View my loans
Upon entering 3, the program will display all active loans (sorted by due date). Active loans are those without a returned date.

Logged in as Chris Manner (Student)
==================================
My Library Account
0. Quit
1. Log out
2. View account policies
3. View my loans
==================================
Enter your choice: 3
You are currently have 2 loan(s).
1. P0006 'Hands-On ML' by Aurelien Geron (2019). Due date: 13/09/2025.
2. E0001 'Python Crash Course' by Eric Matthes (2015). Due date: 15/09/2025.

4. Library Report (Library Staff only)
Upon entering 4, library staff can access a summary report of the library. This report provides key statistics, including the total number of users (with a breakdown by role), as well as details about the book collection and available books which currently have one or more copies available.

Logged in as Mary Alan (Staff)
==================================
My Library Account
0. Quit
1. Log out
2. View account policies
3. View my loans
4. Library Report
==================================
Enter your choice: 4
Library Report
- 9 users, including 4 student(s), 3 staff and 2 others.
- 14 books, including 10 physical book(s) (7 currently available) and 4 online book(s).

---

【中文翻译】

任务1 - 欢迎来到图书馆数据库 [8分]
你需要设计并实现一个基于Python的小型图书馆管理系统。系统应支持以下核心任务，包括管理不同类型的用户（学生、教职工和其他成员）、管理图书馆的藏书，以及跟踪和更新借阅记录。

说明
图书馆为你提供了三个CSV文件，包含当前数据：users.csv（用户信息）、books.csv（图书信息）、loans.csv（借阅历史）。

在任务1-3中，你可以假设所有CSV文件都包含有效数据。

你可以修改脚手架中的import语句或将import语句移动到不同模块，但不能导入脚手架中未原本导入的模块。

用户（users.csv）
该文件包含所有注册用户的详细信息：

字段：用户ID、密码、姓名、角色，以及（仅限学生和教职工）部门。

用户类型：
- 学生（用户ID以s开头）
- 教职工（用户ID以e开头）
- 其他（用户ID以o开头）

每种用户类型有特定的借阅政策：

| 用户类型 | 物理书借期 | 在线书借期 | 借阅配额 |
|----------|-----------|-----------|----------|
| 学生     | 10天      | 无限      | 4本      |
| 教职工   | 14天      | 无限      | 6本      |
| 其他     | 7天       | 无限      | 2本      |

所有用户都可以借阅、归还和续借图书，并查看自己的活跃借阅和借阅政策。只有教职工可以添加、更新或查看用户和图书的详细信息（更多内容见任务2-3）。

图书（books.csv）
该文件包含馆藏图书的信息：

字段：图书ID、类型（如物理或在线）、总库存、书名、作者、年份和关键词（用冒号分隔）。

每本书都有唯一的ID，首字符表示类别，后跟4位数字。

物理书的ID以P开头。

在线书（电子书）的ID以E开头。

对于在线书，总库存字段始终为0。

借阅（loans.csv）
该文件包含借阅记录：

字段：用户ID、图书ID、借阅日期、到期日期、归还日期。所有日期格式为dd/mm/yyyy。

到期日期根据借阅政策自动计算。

活跃借阅是指没有归还日期的记录。

你的任务
编写一个程序，从users.csv、books.csv和loans.csv文件读取数据，并通过简单菜单与数据交互。

你已获得3个模块：user.py、book.py和task1.py。你的任务是：
- 完善users.py和books.py模块中的User和Book类实现。你可以根据需要添加其他类和函数。
- 在task1.py中实现交互菜单。

登录菜单
程序启动时，用户需输入ID和密码登录。

如果用户ID不存在或ID和密码不匹配，程序会打印“Invalid credentials. x attempt(s) remaining.”并提示用户重新登录。

登录成功后，显示欢迎信息，包括用户名和角色。

用户有三次登录机会，三次失败后程序打印“Sorry you're out of attempts. Please contact your librarian for assistance.”并返回欢迎和登录菜单。

在登录菜单中，用户可以输入“quit”退出程序。

主菜单
登录后，用户会看到基于角色的个性化主菜单。

对于学生、其他用户和非图书馆部门教职工：

已登录：Chris Manner（学生）
==================================
我的图书馆账户
0. 退出
1. 注销
2. 查看账户政策
3. 查看我的借阅
==================================
请输入你的选择：

对于图书馆部门教职工：

已登录：Mary Alan（教职工）
==================================
我的图书馆账户
0. 退出
1. 注销
2. 查看账户政策
3. 查看我的借阅
4. 图书馆报告
==================================
请输入你的选择：

如果用户输入了错误选项（如5或four），程序应提示重新输入。

0. 退出
程序打印“Goodbye!”并终止。

1. 注销
用户注销并返回欢迎和登录界面。

2. 查看账户政策
输入2后，程序显示用户当前会员政策及其总借阅数。

3. 查看我的借阅
输入3后，程序显示所有活跃借阅（按到期日期排序）。活跃借阅是指没有归还日期的记录。

4. 图书馆报告（仅限图书馆教职工）
输入4后，图书馆教职工可查看图书馆统计报告，包括用户总数（按角色细分）、馆藏图书详情及当前有库存的图书。

---

Examples
User inputs are in bold font below.

Example 1
Welcome to Library
Login as: s312
Password: chr1267
Invalid credentials. 2 attempt(s) remaining.
Login as: s31267
Password: chr12
Invalid credentials. 1 attempt(s) remaining.
Login as: s31267
Password: chr126
Sorry you're out of attempts. Please contact your librarian for assistance.
Welcome to Library
Login as: quit
Goodbye!

Example 2
Welcome to Library
Login as: s31267
Password: chr1267
Logged in as Chris Manner (Student)
==================================
My Library Account
0. Quit
1. Log out
2. View account policies
3. View my loans
==================================
Enter your choice: 2
Student Chris Manner. Policies: maximum of 10 days, 4 items. Current loans: 2 (1 physical / 1 online).
==================================
My Library Account
0. Quit
1. Log out
2. View account policies
3. View my loans
==================================
Enter your choice: 3
You are currently have 2 loan(s).
1. P0006 'Hands-On ML' by Aurelien Geron (2019). Due date: 13/09/2025.
2. E0001 'Python Crash Course' by Eric Matthes (2015). Due date: 15/09/2025.
==================================
My Library Account
0. Quit
1. Log out
2. View account policies
3. View my loans
==================================
Enter your choice: 0
Goodbye!

Example 3
Welcome to Library
Login as: e118102
Password: pa55word
Logged in as Mary Alan (Staff)
==================================
My Library Account
0. Quit
1. Log out
2. View account policies
3. View my loans
4. Library Report
==================================
Enter your choice: 4
Library report
- 9 users, including 4 student(s), 3 staff, and 2 others.
- 14 books, including 10 physical book(s) (7 currently available) and 4 online book(s).
==================================
My Library Account
0. Quit
1. Log out
2. View account policies
3. View my loans
4. Library Report
==================================
Enter your choice: 5
Enter your choice: 3
You are currently have 1 loan(s).
1. P0004 'The Hitchhiker's Guide to the Galaxy' by Douglas Adams (1985). Due date: 17/09/2025.
==================================
My Library Account
0. Quit
1. Log out
2. View account policies
3. View my loans
4. Library Report
==================================
Enter your choice: 0
Goodbye!

Example 4
Welcome to Library
Login as: o56789
Password: hackme
Logged in as Chloe (Others)
==================================
My Library Account
0. Quit
1. Log out
2. View account policies
3. View my loans
==================================
Enter your choice: 2
Others Chloe. Policies: maximum of 7 days, 2 items. Current loans: 0 (0 physical / 0 online).
==================================
My Library Account
0. Quit
1. Log out
2. View account policies
3. View my loans
==================================
Enter your choice: 3
You are currently have 0 loan(s).
==================================
My Library Account
0. Quit
1. Log out
2. View account policies
3. View my loans
==================================
Enter your choice: 0
Goodbye!

Example 5
Login as: e45261
Password: readmore
Logged in as Lan Nguyen (Staff)
==================================
My Library Account
0. Quit
1. Log out
2. View account policies
3. View my loans
==================================
Enter your choice: 2
Staff Lan Nguyen. Policies: maximum of 14 days, 6 items. Current loans: 1 (1 physical / 0 online).
==================================
My Library Account
0. Quit
1. Log out
2. View account policies
3. View my loans
==================================
Enter your choice: 3
You are currently have 1 loan(s).
1. P0019 'Principles of Marketing' by Philip Kotler (2016). Due date: 21/09/2025.
==================================
My Library Account
0. Quit
1. Log out
2. View account policies
3. View my loans
==================================
Enter your choice: 0
Goodbye!