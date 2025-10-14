import csv
import datetime
import re

class Book:
    """
    the book class that contains all the book variables for a book object
    """

    books = []

    def __init__(self, book_ID, book_type, total_copy, title, author, year, keywords = ""):
        """
        constructor to initialise a book object 
        parameters:
            -book_ID: str
            -book_type:str
            -total_copy:int
            -title:str
            -author:str
            -year:int
            -keywords:list
        """
        self.book_ID = book_ID
        self.book_type = book_type
        self.total_copy = total_copy
        self.title = title
        self.author = author
        self.year = year
        self.keywords = []
        if keywords:
            for key in keywords.split(":"):
                self.keywords.append(key.strip())
                #keywords from the csv file is : separated for each book

        Book.books.append(self)

    def available_copies(self, active_loan_amount):
        """
        two cases:
        online is not applicable
        physical books have available copies
        """
        if self.is_online_book():
            return None
  
        active_loan_amount = active_loan_amount or 0
        return max(self.total_copy - active_loan_amount, 0)
            


    def is_physical_book(self) -> bool:
        """
        check if the book is physical 
        return:boolean
        """
        return self.book_type == "physical"

    def is_online_book(self) -> bool:
        """
        check if the book is online
        return:boolean
        """
        return self.book_type == "online"

    def __str__(self):
        """
        display message as per the example
        """
        return f"{self.book_ID} '{self.title}' by {self.author} ({self.year})."







