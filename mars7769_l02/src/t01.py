"""
-------------------------------------------------------
[lab 2, Task 1]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2024-01-18"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack

s = Stack()
b = s.is_empty()
print(b)

value = 4
s.push(value)

print(s.peek())