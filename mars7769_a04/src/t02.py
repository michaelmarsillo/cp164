"""
-------------------------------------------------------
[Assignment 4, Task 2]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2024-02-01"
-------------------------------------------------------
"""
# Imports
from Queue_array import Queue

s1 = Queue()
s2 = Queue()
s2.insert(1)
s1.insert(10)

equals = s1 == s2

print(equals)