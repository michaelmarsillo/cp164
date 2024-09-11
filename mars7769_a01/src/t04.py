"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2024-01-09"
-------------------------------------------------------
"""
# Imports
from functions import file_analyze

with open('testing.txt', 'r') as file:
    upper, lower, digits, whitespace, remaining = file_analyze(file)

print("Uppercase letters:", upper)
print("Lowercase letters:", lower)
print("Digits:", digits)
print("Whitespace characters:", whitespace)
print("Remaining characters:", remaining)