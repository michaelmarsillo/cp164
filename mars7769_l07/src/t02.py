"""
-------------------------------------------------------
[Lab 7, Task 2]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2024-02-29"
-------------------------------------------------------
"""
# Imports
from List_linked import List

l = List()
l2 = List()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l2.append(1)
l2.append(2)
l2.append(3)
l2.append(4)
l2.append(5)

print(l.is_identical_r(l2))