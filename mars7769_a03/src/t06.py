"""
-------------------------------------------------------
[Assignment 3, Task 6]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2024-01-25"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from functions import postfix

string = "5 1 2 + 4 * + 3 -"
answer = postfix(string)

print(answer)
