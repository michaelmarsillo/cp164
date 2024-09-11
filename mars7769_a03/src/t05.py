"""
-------------------------------------------------------
[Assignment 3, Task 5]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2024-01-25"
-------------------------------------------------------
"""
# Imports
from functions import is_palindrome_stack
from Stack_array import Stack

string = input("Enter a string: ")
palindrome = is_palindrome_stack(string)
print(palindrome)