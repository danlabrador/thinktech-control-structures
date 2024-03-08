# tests/test_activity13.py

import sys
import os

# Adjust the path to include the directory where test_utils.py is located
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from test_utils import describe
from activity13 import max_subarray_sum

# Descriptive testing using the improved test_utils.py
if __name__ == "__main__":
    test = describe("Activity 13: Maximum Subarray Sum")

    # Test with a mix of positive and negative numbers
    test("Mixed positive and negative numbers", max_subarray_sum, 6, [-2, 1, -3, 4, -1, 2, 1, -5, 4])
    # Test with all positive numbers
    test("All positive numbers", max_subarray_sum, 28, [4, 8, 2, 10, 4])
    # Test with all negative numbers (should return 0 if no positive subarray exists, or the highest negative number)
    test("All negative numbers", max_subarray_sum, 0, [-1, -2, -3, -4])
    # Test with an empty array (should return 0 or appropriate value for empty input)
    test("Empty array", max_subarray_sum, 0, [])
    # Test with a single negative number
    test("Single negative number", max_subarray_sum, -1, [-1])
    # Test with a single positive number
    test("Single positive number", max_subarray_sum, 5, [5])
    # Test with alternating high positive and negative numbers
    test("Alternating high positive and negative numbers", max_subarray_sum, 100, [50, -50, 100, -100, 50])
    # Test with increasing numbers
    test("Increasing numbers", max_subarray_sum, 10, [1, 2, 3, 4])
