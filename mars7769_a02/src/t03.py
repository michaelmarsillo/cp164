"""
-------------------------------------------------------
[Task 3, Assignment 2]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2024-01-17"
-------------------------------------------------------
"""
# Imports
from Food_utilities import calories_by_origin
from Food import Food

f = Food("grape", 3, True, 1)
f2 = Food("apple", 3, True, 7)
f3 = Food("banana", 1, True, 6)

foods = [f, f2, f3]

by_origin = calories_by_origin(foods, 3)

print(by_origin)