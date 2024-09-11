"""
-------------------------------------------------------
[Lab 10, Task 3]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2024-03-20"
-------------------------------------------------------
"""
# Imports
from test_Sorts_array import SORTS, test_sort

print(
    f"n:   100       |      Comparisons       | |         Swaps          |")
print("Algorithm      In Order Reversed   Random In Order Reversed   Random")
print("-------------- -------- -------- -------- -------- -------- --------")

for values in SORTS:
    test_sort(values[0], values[1])



