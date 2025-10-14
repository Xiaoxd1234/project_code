from abc import ABC, abstractmethod
import csv
import datetime
import re

class User(ABC):
    """
    an abstract parent class representing all kinds of library users
    """
    
    #a list of all library users
    users = []
    
    def __init__(self, user_ID, name, password, role, department):
        """
        a constructor to initialise a library user 
        parameters:
            -user_id:str
            -name:str
            -role:str
            -department: str for students and staff and "" for Others
            -days_allowed:int (depends on the user role)
            -quota:int (depends on the user role)
        """
        self.user_ID = user_ID
        self.name = name
        self.password = password
        self.role = role
        self.department = department or ""
        #only students and staff have departments, others don't have department
        
        
        self.days_allowed = None
        self.quota = None
        #child class will set their own days 


        self.loans=[]
        #an empty list to store current loans of the current user

        User.users.append(self)
        #append the instantiated object to the list


    def __str__(self):
        """
        the printed version of the current user
        """
        return f"{self.name} ({self.role})"


    def is_library_staff(self)->bool:
        """
        check if the staff is a library staff
        return a boolean value
        no parameters
        """

        if self.role == "Staff" and self.department == "Library":
            return True
        else:
            return False

        
class Student(User):
    """
    inherits from User class
    """
    def __init__(self, user_ID, name, password, department):
        """
        constructor to instantiate a student user object
        """
        super().__init__(
            user_ID,
            name,
            password,
            role = "Student",
            department = department)
        self.days_allowed = 10
        self.quota = 4

class Staff(User):
    """
    inherits from User class
    """
    def __init__(self, user_ID, name, password, department):
        """
        constructor to instantiate a staff user object
        """
        super().__init__(
        user_ID,
        name,
        password,
        role = "Staff",
        department = department)
        self.days_allowed = 14
        self.quota = 6



class Others(User):
    """
    inherits from User class
    """
    def __init__(self, user_ID, name, password):
        """
        constructor to instantiate an Others user object
        """
        super().__init__(
            user_ID,
            name,
            password,
            role = "Others",
            department = ""
        )
        self.days_allowed = 7
        self.quota = 2
        
        

