"""
-------------------------------------------------------
[Lab 7, Task 1]
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

l.append(1)
l.append(2)
l.append(2)
l.append(4)
l.append(5)
l.append(2)
key = 2
p, c, i = l._linear_search_r(key)
print(p._value, c._value, i)