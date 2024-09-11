"""
-------------------------------------------------------
[Assignment 6, Task 2]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2024-02-14"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_linked import Priority_Queue

pq = Priority_Queue()

pq.insert('a')
pq.insert('b')
pq.insert('c')

print(pq._front._value, pq._count)

