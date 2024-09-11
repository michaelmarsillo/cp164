"""
-------------------------------------------------------
[Lab 1, Task 5]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2024-01-12"
-------------------------------------------------------
"""
# Imports
from Food_utilities import read_foods

fh = open('foods.txt', 'r', encoding = "utf-8")
foods = read_foods(fh)
print(foods)
fh.close()

for f in foods:
    print(f)
    print()