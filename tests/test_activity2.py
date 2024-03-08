# tests/test_activity2.py

import sys
import os

# Adjust the path to include the directory where test_utils.py is located
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from test_utils import describe
from activity2 import count_even_numbers

# Descriptive testing using the improved test_utils.py
if __name__ == "__main__":
    test = describe("Activity 2: Even Numbers Counter")

    # Test with mixed even and odd numbers
    test("Mixed even and odd numbers", count_even_numbers, 3, [1, 2, 3, 4, 5, 6])
    # Test with all even numbers
    test("All even numbers", count_even_numbers, 5, [2, 4, 6, 8, 10])
    # Test with all odd numbers
    test("All odd numbers", count_even_numbers, 0, [1, 3, 5, 7, 9])
    # Test with zero
    test("Including zero", count_even_numbers, 1, [0])
    # Test with an empty list
    test("Empty list", count_even_numbers, 0, [])
    # Test with large even numbers
    test("Large even numbers", count_even_numbers, 2, [1000, 2002])
    # Test with negative even numbers
    test("Negative even numbers", count_even_numbers, 3, [-2, -4, -6])
    # Test with a large list
    test("Large list of mixed numbers", count_even_numbers, 50, list(range(1, 101)))
    # Test with repetitive numbers
    test("Repetitive numbers", count_even_numbers, 4, [2, 2, 2, 2])
