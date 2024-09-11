"""
-------------------------------------------------------
[Lab 1, Task 6]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2024-01-12"
-------------------------------------------------------
"""
# Imports
from Food_utilities import write_foods
from Food_utilities import read_foods

file_variable = open('foods.txt', 'r')

foods = read_foods(file_variable)
print(foods)

file_variable.close()

file_variable = open('new_foods.txt', 'w')

write_foods(file_variable, foods)
file_variable.close()