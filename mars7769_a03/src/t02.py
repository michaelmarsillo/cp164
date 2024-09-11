"""
-------------------------------------------------------
[Assignment 3, Task 2]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2024-01-25"
-------------------------------------------------------
"""
# Imports
from utilities import array_to_stack
from Stack_array import Stack

target = Stack()
source1 = Stack()
source2 = Stack()
array_to_stack(source1, [5, 8, 12, 8])
array_to_stack(source2, [3, 6, 1, 7, 9, 14])
target.combine(source1, source2)

print(target._values)
