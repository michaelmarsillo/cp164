"""
-------------------------------------------------------
[Lab 2, Task 3]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2024-01-18"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from utilities import stack_test
from Food_utilities import read_foods

s = Stack()

fh = open("foods.txt", "r")
foods = read_foods(fh)
st = stack_test(foods)

fh.close()
