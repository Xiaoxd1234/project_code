Task 1: Marks Cleaning & Transformation
Your tutor, Jueqing is getting trouble with processing your Assignment marks, he wants to get help from you and speed up the marking processing using Python.

Task 1A
Before moving into more sophisticated cases, Jueqing will show you a simple case to let you get familiar with the data you need to proceed later. One example is shown as below:

jueqing_mark = "A1: 100, A2: 95, A3: 91.5"
In the used management system, the mark should be stored as a dictionary as follows:

{"A1": 100, "A2": 95, "A3": 91.5}
Now, your first task is to convert any given strings like above into the desired dictionary, and wrap your solution as a function mark_str_to_dict.

WARNING: Do not delete or rename the functions provided in the scaffold.

 Do not add or remove parameters from the functions provided.

Do not remove the line if __name__ == "__main__":. It ensures that the code below only runs when you use the Run button, and not when you use the  Test button.

Task 1B
Great, now you know how to process the mark strings, but you may revise it to accommodate for handling more unexpected cases, for example, due to system fault, the mark could be sometimes greater than 100 or less than 0, which is factually invalid, so you need to fix this problem as well. One example is shown as below:

jueqing_mark = "A1: 100, A2: 200, A3: -100"
then after fixing and conversion, you should have:

{"A1": 100, "A2": -inf, "A3": -inf}
Note that -inf is floating pointing number which means

type(-inf) is float  # True
You have to figure out the way to define the above value python, considering the type casting.

Now, your task is to solve the above question (Task 1A) and wrap-up your solution as functions fix_invalid_value and mark_str_to_dict_revised in scaffold.

You can assume the problematic marks will only be numbers, i.e., not strings or other data types here.

Task 1C
Well done! Now your processing function is pretty powerful, we are going to handle multiple students' records using the defined function. For example,

{
    "Jueqing": "A1: 99, A2: 200, A3: -100",
    "Trang"  : "A1: 300, A2: 100, A3: 100"
}

then after conversion, you should have a collection for all students:

{
    "Jueqing": {"A1": 99,   "A2": -inf, "A3": -inf},
    "Trang"  : {"A1": -inf, "A2": 100,  "A3": 100 }
}

You should provide your solution for above request in the given function template process_multiple_students_marks.

Jueqing appreciates your help and would like to request one more feature: the ability to better analyze scores for different assignments, such as calculating the average score for A1. You are provided with a function template in the scaffold, named summarize_marks, which takes an input parameter split to specify which assignments to summarize. For example, built-upon the following mark dictionary:

{
    "Jueqing": {
        "A1": 100,
        "A2": -inf,
        "A3": -inf
    },
    "Trang"  : {
        "A1": -inf, 
        "A2": 100,  
        "A3": 100
    },
    "Expert" : {
        "A1": 100,
        "A2": 100,
        "A3": 100
    },
}

you should return a summarized result for split="A2" as follows:

{"average_mark": 100, "invalid_count": 1, "valid_count": 2}