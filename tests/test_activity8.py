# tests/test_activity8.py

import sys
import os

# Adjust the path to include the directory where test_utils.py is located
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from test_utils import describe
from activity8 import sum_of_multiples

# Descriptive testing using the improved test_utils.py
if __name__ == "__main__":
    test = describe("Activity 8: Sum of Multiples")

    # Test with a basic example
    test("Basic example", sum_of_multiples, 23, 10)
    # Test with a larger limit
    test("Larger limit", sum_of_multiples, 233168, 1000)
    # Test with limit being a multiple of 3 and 5
    test("Limit is a multiple of 3 and 5", sum_of_multiples, 78, 20)
    # Test with limit as 0
    test("Limit as 0", sum_of_multiples, 0, 0)
    # Test with limit as 1
    test("Limit as 1", sum_of_multiples, 0, 1)
    # Test with negative limit
    test("Negative limit", sum_of_multiples, 0, -10)
    # Test with a very small limit
    test("Very small limit", sum_of_multiples, 0, 3)
    # Test with a limit just above 3 and 5
    test("Limit just above 3 and 5", sum_of_multiples, 8, 6)
