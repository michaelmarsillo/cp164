"""
-------------------------------------------------------
[Assignment 6, Task 1]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2024-02-14"
-------------------------------------------------------
"""
# Imports
from Queue_linked import Queue

q = Queue()

q.insert(1)
q.insert(2)
q.insert(3)
q.insert(4)
q.insert(5)
q.remove()

print(q._front._value, q._rear._value, q.is_empty())
