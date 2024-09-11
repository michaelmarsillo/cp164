"""
-------------------------------------------------------
[Lab 4, Task 2]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2024-02-02"
-------------------------------------------------------
"""
# Imports
from List_array import List
from utilities import array_to_list, list_to_array

llist = List()
source = [1, 2, 3, 4, 5, 6, 7]
array_to_list(llist, source)
print(llist._values, source)

target = []
list_to_array(llist, target)
print(llist._values, target)
