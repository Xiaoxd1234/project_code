Task 2: Mark Accessing System
Great job so far! You have already implemented the basic functions for fixing incorrect marks and summarizing scores for each assignment.

In this task, you are required to design a simple CLI-based (Command Line Interface) system that allows lecturers and tutors to access and manage these marks.

Task Description
Write a program that allows users to do different things.

You have the freedom to design your own functions, but be careful to avoid unnecessary ones. 
Consider reusing functions with different parameters for different outputs.

The entry point of your program should be the main function main(user_info, mark_unprocessed) .

Main Menu

The program prompt of the main menu looks like:

Username should be case-insensitive here
Password should always be case-sensitive

=============
Welcome to the Mark system v0.0!
Please Login:
1.Exit
2.Login
Your choice (number only):
=============

If the user inputs 1, 2, it runs the corresponding function. Otherwise, the prompt is simply printed again. See Example 1 & 2 & 3

Menu after login

=============
Welcome Jueqing
Please choice one option below:
1.Exit
2.Re-Login
3.Show mark records
4.Show summarization
Your choice (number only):
=============

If the user inputs 1, 2, it runs the corresponding function. Otherwise, the prompt is simply printed again. See Example 4

For testing-purpose, please use exactly same order of menu options as above


Functionalities after Login

1. Exit: same as the `Exit` in the main menu

2. Re-Login: logout the current account, back to main menu (see Example 5)

3. Show mark records: show processed mark records, format needed! (see Example  6)

4. Show summarization: show the summarization statistics of mark records, based on selected Assignment split (see Example  7)

If the user enters an invalid option, the program must repeatedly prompt them until a valid option is provided.

you may copy codes from your task1.py file for re-using purpose


Examples
==== dashes are used for demonstration purpose only, you can decide where to use/show them by yourself.

Example 1

==================================
Welcome to the Mark system v0.0!
Please Login:
1.Exit
2.Login
Your choice (number only): 2
==================================
Please key your account name:
Please key your password:

Example 2

==================================
Welcome to the Mark system v0.0!
Please Login:
1.Exit
2.Login
Your choice (number only): 1
==================================
See u!

Example 3

==================================
Welcome to the Mark system v0.0!
Please Login:
1.Exit
2.Login
Your choice (number only): 3
==================================
Welcome to the Mark system v0.0!
Please Login:
1.Exit
2.Login
Your choice (number only):

Example 4a

==================================
Welcome to the Mark system v0.0!
Please Login:
1.Exit
2.Login
Your choice (number only): 2
==================================
Please key your account name: jueqing
Please key your password: Jueqing123
==================================
Welcome Jueqing
Please choose one option below:
1.Exit
2.Re-Login
3.Show mark records
4.Show summarization
Your choice (number only):

Example 4b [unlimited attempts]

==================================
Welcome to the Mark system v0.0!
Please Login:
1.Exit
2.Login
Your choice (number only): 2
==================================
Please key your account name: jueqing
Please key your password: wrong_password
==================================
Incorrect username or password!
==================================
Welcome to the Mark system v0.0!
Please Login:
1.Exit
2.Login
Your choice (number only): 

Example 5

Welcome Jueqing
Please choose one option below:
1.Exit
2.Re-Login
3.Show mark records
4.Show summarization
Your choice (number only): 2
==================================
You have logged off successfully!
Welcome to the Mark system v0.0!
Please Login:
1.Exit
2.Login
Your choice (number only):

Example 6

Welcome Jueqing
Please choose one option below:
1.Exit
2.Re-Login
3.Show mark records
4.Show summarization
Your choice (number only): 3
==================================
Results:
Jueqing: 
    A1: 99
    A2: -inf
    A3: -inf
Trang: 
    A1: -inf
    A2: 100
    A3: 100
==================================
Welcome Jueqing
Please choose one option below:
1.Exit
2.Re-Login
3.Show mark records
4.Show summarization
Your choice (number only):

Example 7

Welcome Jueqing
Please choose one option below:
1.Exit
2.Re-Login
3.Show mark records
4.Show summarization
Your choice (number only): 4
==================================
Available Assignments: {'A3', 'A2', 'A1'}
The Assignment you want to check (e.g., A1): A2
==================================
Results For A2:
average_mark: 100.0
invalid_count: 1
valid_count: 1
==================================
Welcome Jueqing
Please choose one option below:
1.Exit
2.Re-Login
3.Show mark records
4.Show summarization
Your choice (number only):