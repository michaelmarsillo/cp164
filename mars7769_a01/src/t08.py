"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2024-01-09"
-------------------------------------------------------
"""
# Imports
from functions import matrix_stats

matrix = [
    [5, 10, 15],
    [20, 25, 30],
    [35, 40, 45]
]

small, large, total, average = matrix_stats(matrix)

print("Smallest:", small)
print("Largest:", large)
print("Total:", total)
print("Average:", average)