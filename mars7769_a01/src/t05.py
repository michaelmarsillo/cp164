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
from functions import is_leap_year

year = int(input("Enter a year: "))

result = is_leap_year(year)
print(f"Is {year} a leap year? {result}.")