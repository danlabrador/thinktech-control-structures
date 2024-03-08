# tests/test_activity4.py

import sys
import os

# Adjust the path to include the directory where test_utils.py is located
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from test_utils import describe
from activity4 import generate_n_natural_numbers

# Descriptive testing using the improved test_utils.py
if __name__ == "__main__":
    test = describe("Activity 4: First N Natural Numbers")

    # Test with a small positive number
    test("Small positive number", generate_n_natural_numbers, [1, 2, 3, 4, 5], 5)
    # Test with n = 1
    test("n = 1", generate_n_natural_numbers, [1], 1)
    # Test with n = 0, should return an empty list
    test("n = 0", generate_n_natural_numbers, [], 0)
    # Test with a larger number
    test("Larger number", generate_n_natural_numbers, list(range(1, 21)), 20)
    # Test with n as a negative number, should handle gracefully or return empty list based on implementation choice
    test("Negative number", generate_n_natural_numbers, [], -5)
