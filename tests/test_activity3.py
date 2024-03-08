# tests/test_activity3.py

import sys
import os

# Adjust the path to include the directory where test_utils.py is located
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from test_utils import describe
from activity3 import sum_of_even_numbers

# Descriptive testing using the improved test_utils.py
if __name__ == "__main__":
    test = describe("Activity 3: Sum of Even Numbers")

    # Test with mixed even and odd numbers
    test("Mixed even and odd numbers", sum_of_even_numbers, 12, [1, 2, 3, 4, 5, 6])
    # Test with all even numbers
    test("All even numbers", sum_of_even_numbers, 20, [2, 4, 6, 8])
    # Test with all odd numbers, should result in 0
    test("All odd numbers", sum_of_even_numbers, 0, [1, 3, 5, 7, 9])
    # Test including zero
    test("Including zero", sum_of_even_numbers, 2, [0, 2])
    # Test with an empty list, should result in 0
    test("Empty list", sum_of_even_numbers, 0, [])
    # Test with large even numbers
    test("Large even numbers", sum_of_even_numbers, 4004, [2000, 2004])
    # Test with negative even numbers
    test("Negative even numbers", sum_of_even_numbers, -12, [-2, -4, -6])
    # Test with a large list of mixed numbers
    test("Large list of mixed numbers", sum_of_even_numbers, 2550, list(range(1, 101)))
    # Test with repetitive even numbers
    test("Repetitive even numbers", sum_of_even_numbers, 8, [2, 2, 2, 2])
