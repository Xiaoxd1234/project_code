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