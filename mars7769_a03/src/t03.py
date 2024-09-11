"""
-------------------------------------------------------
[Assignment 3, Task 3]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2024-01-25"
-------------------------------------------------------
"""
# Imports
from functions import stack_reverse
from utilities import array_to_stack
from Stack_array import Stack

source1 = Stack()
array_to_stack(source1, [3, 6, 1, 7, 9, 14])
print(source1._values)
stack_reverse(source1)

print(source1._values)