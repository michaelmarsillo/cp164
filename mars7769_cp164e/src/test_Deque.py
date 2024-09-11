"""
-------------------------------------------------------
Exam: Simple Deques testing
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2024-04-19"
-------------------------------------------------------
"""
# pylint: disable=protected-access

# Imports
from Deque_linked import Deque

# Constants
VALUES = [3, 8, 6, 7, 6, 2, 4, 6]
SEP = '-' * 60


def to_python_list(source):
    """
    Testing helper method. Copies Deque values to a Python list.
    """
    values = []
    for value in source:
        values.append(value)
    return values


def to_Deque(values):
    """
    Testing helper method. Copies Python list values to a Deque.
    """
    source = Deque()
    for value in values:
        source.insert_front(value)
    return source


def test_is_mirror():
    """
    Tests the 'is_mirror' method.
    """
    print(SEP)
    print("Test 'is_mirror'")
    print()

    source = to_Deque(VALUES)
    mirror = source.is_mirror()
    print(f"    Deque: {to_python_list(source)} - mirror: {mirror}")
    source = to_Deque([1, 2, 3, 2, 1])
    mirror = source.is_mirror()
    print(f"    Deque: {to_python_list(source)} - mirror: {mirror}")


def test_append_front():
    """
    Tests the 'append_front' method.
    """
    print(SEP)
    print("Test 'append_front'")
    print()

    source = to_Deque(VALUES)
    print(f"    Deque: {to_python_list(source)}")
    source.append_front()
    print(f"    After 'append_front': {to_python_list(source)}")
    print()


if __name__ == "__main__":
    print("Deque_linked Testing")
    test_is_mirror()
    test_append_front()
