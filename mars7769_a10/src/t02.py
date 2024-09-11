"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2024-03-26"
-------------------------------------------------------
"""
# Imports
from Sorts_List_linked import Sorts
from List_linked import List

a = List()
a.append(56)
a.append(54)
a.append(133)
a.append(3)
a.append(35)
a.append(52)
a.append(15423120)

Sorts.radix_sort(a)

print(a._front._value)