"""
-------------------------------------------------------
[Lab 3, Task 3]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2024-01-26"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_array import Priority_Queue
from utilities import array_to_pq, pq_to_array

source = [1, 2, 5, 4, 8, 6, 7, 3, 9]
target = []
q = Priority_Queue()
array_to_pq(q, source)
#pq_to_array(q, target)
# print(target)
print(q._values)