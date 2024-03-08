# tests/test_activity11.py

import sys
import os

# Adjust the path to include the directory where test_utils.py is located
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from test_utils import describe
from activity11 import generate_fibonacci

# Descriptive testing using the improved test_utils.py
if __name__ == "__main__":
    test = describe("Activity 11: Fibonacci Sequence Generator")

    # Test with n = 1 (first Fibonacci number)
    test("First Fibonacci number", generate_fibonacci, [0], 1)
    # Test with n = 2 (first two Fibonacci numbers)
    test("First two Fibonacci numbers", generate_fibonacci, [0, 1], 2)
    # Test with n = 5
    test("First five Fibonacci numbers", generate_fibonacci, [0, 1, 1, 2, 3], 5)
    # Test with n = 0 (should return an empty list)
    test("Zero Fibonacci numbers", generate_fibonacci, [], 0)
    # Test with a larger value of n
    test("First ten Fibonacci numbers", generate_fibonacci, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34], 10)
    # Test with negative n (should handle gracefully or return empty list based on implementation choice)
    test("Negative Fibonacci numbers", generate_fibonacci, [], -5)
