"""
-------------------------------------------------------
[Assignment 4, Task 6]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2024-02-01"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_array import Priority_Queue

pq = Priority_Queue()
pq.insert(1)
pq.insert(2)
pq.insert(3)
pq.insert(4)
pq.insert(5)

key = 3

print(pq._values)
target1, target2 = pq.split_key(key)
print(target1._values, target2._values)