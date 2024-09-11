"""
-------------------------------------------------------
[Assignment 4, Task 4]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2024-02-01"
-------------------------------------------------------
"""
# Imports
from Queue_array import Queue

q = Queue()

q.insert(1)
q.insert(2)
q.insert(3)
q.insert(4)
q.insert(5)

target1, target2 = q.split_alt()

print("Target1: {}".format(target1._values))
print("Target2: {}".format(target2._values))

