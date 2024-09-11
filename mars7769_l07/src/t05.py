"""
-------------------------------------------------------
[Lab 7, Task 5]
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
l.append(22)
l.append(33)
l.append(11)
l.append(55)
l.append(44)
l.append(None)

l.reverse_r()

print(l._rear._value, l._front._value, l._front._next._value, l._front._next._next._value,
      l._front._next._next._next._value, l._front._next._next._next._next._value, l._front._next._next._next._next._next._value)
