# tests/test_activity7.py

import sys
import os

# Adjust the path to include the directory where test_utils.py is located
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from test_utils import describe
from activity7 import find_min_max

# Descriptive testing using the improved test_utils.py
if __name__ == "__main__":
    test = describe("Activity 7: Find Minimum and Maximum")

    # Test with a list of integers
    test("List of integers", find_min_max, (1, 5), [1, 2, 3, 4, 5])
    # Test with an empty list, expect a specific response or exception handling
    test("Empty list", find_min_max, (None, None), [])
    # Test with all elements being the same
    test("All elements same", find_min_max, (2, 2), [2, 2, 2, 2])
    # Test with negative numbers
    test("Negative numbers", find_min_max, (-5, -1), [-1, -2, -3, -4, -5])
    # Test with a large range of numbers
    test("Large range", find_min_max, (-100, 100), range(-100, 101))
    # Test with mixed negative and positive numbers
    test("Mixed numbers", find_min_max, (-10, 10), [-10, -5, 0, 5, 10])
    # Test with a single element
    test("Single element", find_min_max, (42, 42), [42])
    # Test with floating point numbers
    test("Floating point numbers", find_min_max, (-2.5, 3.5), [-2.5, -1.0, 0, 1.5, 3.5])
