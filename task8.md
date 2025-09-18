Task 8: Role-Based Vocabulary Management - Part B
Now that you have completed the implementation of the vocabulary management system in TextProcessor, it's time to take it a step further by building a role-based interface using Object-Oriented Programming (OOP) principles.

In this task, you will design and implement a user-driven vocabulary management system that supports interaction from different types of users (e.g., readers and admins). This task simulates a real-world collaborative environment, where access control and data integrity are critical.

🧩 Task Objective
You are required to implement the following two classes:

Role: defines the role of a user, including their name, access level, and identity information.

RoleBasedVocabSys: manages user login, menu display, command execution, and interaction with the TextProcessor object.

The program should simulate a terminal-like experience for different types of users, controlling what they can see and what actions they can perform.

👥 User Roles
The system supports two user roles:

Reader:

Can log in and view the vocabulary.

Can view the top 10 and bottom 10 most frequent words.

Cannot update or modify any part of the vocabulary.

Admin:

Has all the permissions of the reader.

Can update the vocabulary by adding new files or removing existing ones.

Has full access to the vocabulary update methods from TextProcessor. User credentials and access roles are provided as the varaiable users_info from the util.py module. in scaffold.

📋 Task Requirements
You must:

Implement the Role class, which should:

Store and return the user’s username, display name, and access level (e.g., "reader", "admin").

Provide getter methods: get_user_name(), get_access(), get_name().

Implement the RoleBasedVocabSys class, which should:

Handle login and logout.

Display different menus depending on whether a user is logged in and their access level.

Call TextProcessor functions (from Task 7) to manage the vocabulary.

Enforce role-based access control (e.g., only admins can update vocabularies).

Use the provided attributes and method names in the scaffold. Do not rename or remove any predefined code blocks.

Implement menu-based navigation where users can choose options via standard input:

Exit the system.

Login or Logout.

View the top 10 or bottom 10 frequent words.

Update vocabulary by adding/removing files (admin only).

🧠 Additional Notes
The vocabulary is loaded and managed via the TextProcessor object created in the constructor.

The files to be added/removed are fixed as data/for_admin/excluded.csv for this exercise, but you may generalize it in future tasks.

All user input should be validated using verify_user_choice.

The system should loop until the user chooses to exit.

---

任务8：基于角色的词汇管理 - Part B
在你已经完成了 TextProcessor 中词汇管理系统的实现后，现在需要进一步利用面向对象编程（OOP）原则，构建一个基于角色的界面。

在本任务中，你将设计并实现一个由用户驱动的词汇管理系统，支持不同类型用户（如读者和管理员）的交互。该任务模拟了一个真实的协作环境，其中访问控制和数据完整性至关重要。

🧩 任务目标
你需要实现以下两个类：

Role：定义用户的角色，包括其姓名、访问级别和身份信息。

RoleBasedVocabSys：管理用户登录、菜单显示、命令执行以及与 TextProcessor 对象的交互。

该程序应模拟不同类型用户的终端体验，控制他们能看到和能执行的操作。

👥 用户角色
系统支持两种用户角色：

读者：
- 可以登录并查看词汇表。
- 可以查看出现频率最高的前10个和最低的后10个单词。
- 不能更新或修改词汇表的任何部分。

管理员：
- 拥有读者的所有权限。
- 可以通过添加新文件或移除现有文件来更新词汇表。
- 拥有对 TextProcessor 的全部词汇更新方法的访问权限。用户凭证和访问角色通过 scaffold 中 util.py 模块的变量 users_info 提供。

📋 任务要求
你必须：

实现 Role 类，需：
- 存储并返回用户的用户名、显示名和访问级别（如“reader”、“admin”）。
- 提供 getter 方法：get_user_name()、get_access()、get_name()。

实现 RoleBasedVocabSys 类，需：
- 处理登录和登出。
- 根据用户是否登录及其访问级别显示不同菜单。
- 调用 TextProcessor 的相关函数（来自任务7）管理词汇表。
- 强制执行基于角色的访问控制（如仅管理员可更新词汇表）。
- 使用 scaffold 中提供的属性和方法名，不要重命名或移除任何预定义代码块。

实现基于菜单的导航，用户可通过标准输入选择操作：
- 退出系统。
- 登录或登出。
- 查看出现频率最高的前10个或最低的后10个单词。
- 更新词汇表（仅管理员可添加/移除文件）。

🧠 补充说明
- 词汇表通过在构造函数中创建的 TextP rocessor 对象进行加载和管理。
- 本练习中需添加/移除的文件固定为 data/for_admin/excluded.csv，后续任务可进一步泛化。
- 所有用户输入需通过 verify_user_choice 进行验证。
- 系统应循环运行，直到用户选择退出。