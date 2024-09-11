"""
-------------------------------------------------------
[Lab 5, Task 2]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2024-02-09"
-------------------------------------------------------
"""
# Imports
from functions import gcd

m = int(input("Enter an integer: "))
n = int(input("Enter another integer: "))
ans = gcd(m, n)

print("The greatest common denominator of", m, "and", n, "is", ans)

