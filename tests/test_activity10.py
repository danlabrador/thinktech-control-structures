# tests/test_activity10.py

import sys
import os

# Adjust the path to include the directory where test_utils.py is located
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from test_utils import describe
from activity10 import is_prime

# Descriptive testing using the improved test_utils.py
if __name__ == "__main__":
    test = describe("Activity 10: Prime Number Checker")

    # Test with a prime number
    test("Prime number", is_prime, True, 29)
    # Test with a non-prime number
    test("Non-prime number", is_prime, False, 4)
    # Test with 1, traditionally not considered a prime number
    test("Number one", is_prime, False, 1)
    # Test with a large prime number
    test("Large prime number", is_prime, True, 7919)
    # Test with a large non-prime number
    test("Large non-prime number", is_prime, False, 7920)
    # Test with the smallest prime number
    test("Smallest prime number", is_prime, True, 2)
    # Test with a negative number, which cannot be prime
    test("Negative number", is_prime, False, -3)
    # Test with 0, which is not a prime number
    test("Zero", is_prime, False, 0)
