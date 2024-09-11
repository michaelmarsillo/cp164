"""
-------------------------------------------------------
[Lab 3, Task 4]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2024-01-26"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_array import Priority_Queue
from utilities import priority_queue_test

fh = open('foods.txt', 'r')

print(priority_queue_test(fh))

fh.close()