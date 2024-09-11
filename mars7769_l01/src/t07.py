"""
-------------------------------------------------------
[Lab 1, Task 7]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2024-01-12"
-------------------------------------------------------
"""
# Imports
from Food_utilities import read_foods
from Food_utilities import get_vegetarian

filename = 'foods.txt'
file_variable = open(filename, 'r')

foods = read_foods(file_variable)

v_foods = get_vegetarian(foods)
print(v_foods)

