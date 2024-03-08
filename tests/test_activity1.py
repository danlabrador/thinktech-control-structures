# tests/test_activity1.py

import sys
import os

# Adjust the path to include the directory where test_utils.py is located
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from test_utils import describe
from activity1 import filter_positive_numbers

# Descriptive testing using the improved test_utils.py
if __name__ == "__main__":
    test = describe("Activity 1: Positive Numbers Filter")

    # Test with a mix of positive and negative numbers
    test("Mixed positive and negative numbers", filter_positive_numbers, [2, 4], [-1, 2, -3, 4, -5])
    # Test with all positive numbers
    test("All positive numbers", filter_positive_numbers, [1, 2, 3, 4], [1, 2, 3, 4])
    # Test with all negative numbers (should return an empty list)
    test("All negative numbers", filter_positive_numbers, [], [-2, -1, -3])
    # Test with an empty list (should return an empty list)
    test("Empty list", filter_positive_numbers, [], [])
    # Test with zeros included (should not be considered positive)
    test("Zeros included", filter_positive_numbers, [5], [0, -1, 5, -10, 0])
    # Test with large numbers
    test("Large numbers", filter_positive_numbers, [100, 200, 1000], [100, -300, 200, -400, 1000])
    # Test with very small positive numbers
    test("Very small positive numbers", filter_positive_numbers, [0.1, 0.2], [-0.5, 0.1, -0.2, 0.2])
