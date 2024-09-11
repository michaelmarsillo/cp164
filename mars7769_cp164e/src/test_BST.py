"""
-------------------------------------------------------
Exam: Simple BST testing
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2024-04-23"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST


# Constants
VALUES = [11, 7, 6, 9, 8, 15, 12, 18]
SEP = '-' * 60


def to_BST(values):
    """
    Testing helper method. Copies Python list values to a BST.
    """
    bst = BST()

    for v in values:
        bst.insert(v)
    return bst


def test_flip():
    """
    Tests the 'flip' method.
    """
    print(SEP)
    print("Test 'flip'")
    print()
    bst = to_BST(VALUES)
    print(f"  Inorder: {bst.inorder()}")
    bst.flip()
    print(f"  Inorder: {bst.inorder()}")


def test_are_flipped():
    """
    Tests the 'are_flipped' method.
    """
    print(SEP)
    print("Test 'are_flipped'")
    print()
    bst1 = to_BST([])
    bst2 = to_BST([])
    bst2.flip()

    print(f"  are_flipped: {bst1.are_flipped(bst2)}")
    print()

    bst1 = to_BST(VALUES)
    bst2 = to_BST(VALUES)

    print(f"  are_flipped: {bst1.are_flipped(bst2)}")
    print()

    bst2.flip()

    print(f"  are_flipped: {bst1.are_flipped(bst2)}")
    print()


def test_total_height():
    """
    Tests the 'total_height' method.
    """
    print(SEP)
    print("Test 'total_height'")
    print()
    bst = to_BST(VALUES)
    print(f"  total height: {bst.total_height()}")


def test_furthest():
    """
    Tests the 'furthest' method.
    """
    print(SEP)
    print("Test 'furthest'")
    print()
    bst = to_BST([])

    print(f"  Preorder: {bst.preorder()}")
    print(f"  Furthest: {bst.furthest()}")
    print()

    bst = to_BST([VALUES[0]])
    print(f"  Preorder: {bst.preorder()}")
    print(f"  Furthest: {bst.furthest()}")
    print()

    bst = to_BST(VALUES)
    print(f"  Preorder: {bst.preorder()}")
    print(f"  Furthest: {bst.furthest()}")


if __name__ == "__main__":
    print("BST_linked Testing")
    test_flip()
    test_are_flipped()
    test_total_height()
    test_furthest()
