"""
This file contains custom errors that have been created for the purpose of testing 
you on your knowledge of how and when to raise errors. 
You need not change anything in this file, it is purely here to function as an 
import-able resource for your tasks
"""

class CustomError(Exception):
    """
    This error should be raised when the value isn't what its expected to be.
    """
    errors = []
    def __init__(self, message):
        super().__init__(message)
        CustomError.errors.append(self)


class CustomValueError(CustomError):
    """
    This error should be raised when the value isn't what its expected to be.
    """
    pass

class CustomTypeError(CustomError):
    """
    This error should be raised when the type of the value isn't what its expected to be.
    """
    pass

class CustomAttributeError(CustomError):
    """
    This error should be raised when the attribute doesn't exist as expected
    """
    pass

class CustomKeyError(CustomError):
    """
    This error should be raised when a key is expected to exist in a dictionary but doesn't exist.
    """
    pass

class CustomOperationError(CustomError):
    """
    Raised when an invalid borrow or return action is attempted.
    """
    pass

class CustomLimitError(CustomError):
    """
    Raised when a user exceeds their quota or borrowing limit.
    """
    pass

class CustomDateError(CustomError):
    """
    Raised when a date is in the wrong format or when the date logic is invalid (e.g., borrow date occurs in the future).
    """
    pass

class MissingRequiredFieldError(CustomError):
    """
    Raised when a required field is missing.
    """
    pass

class UserNotFoundError(CustomError):
    """
    Raised when a loan references a user that does not exist.
    """
    pass

class BookNotFoundError(CustomError):
    """
    Raised when a loan references a user that does not exist.
    """
    pass

