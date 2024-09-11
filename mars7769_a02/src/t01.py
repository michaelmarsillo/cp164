"""
-------------------------------------------------------
[Task 1, Assignment 2]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2024-01-17"
-------------------------------------------------------
"""
# Imports
from Food_utilities import by_origin
from Food import Food

f = Food("grape", 3, True, 61)
f2 = Food("apple", 3, True, 77)
f3 = Food("banana", 1, True, 60)

foods = [f, f2, f3]

o_foods = by_origin(foods, 3)

for i in o_foods:
    print(i)
