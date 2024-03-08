# tests/test_activity15.py

import sys
import os

# Adjust the path to include the directory where test_utils.py is located
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from test_utils import describe
from activity15 import binary_to_decimal

# Descriptive testing using the improved test_utils.py
if __name__ == "__main__":
    test = describe("Activity 15: Binary to Decimal Converter")

    # Test with a simple binary number
    test("Simple binary number", binary_to_decimal, 5, "101")
    # Test with a binary number consisting of all 1s
    test("All 1s", binary_to_decimal, 15, "1111")
    # Test with a binary number consisting of all 0s
    test("All 0s", binary_to_decimal, 0, "0000")
    # Test with a longer binary number
    test("Longer binary number", binary_to_decimal, 255, "11111111")
    # Test with a single 1
    test("Single 1", binary_to_decimal, 1, "1")
    # Test with a single 0
    test("Single 0", binary_to_decimal, 0, "0")
    # Test with a binary number that includes leading zeros
    test("Leading zeros", binary_to_decimal, 4, "000100")
    # Test with a "binary" string containing invalid characters (should handle gracefully or validate input)
    test("Invalid binary string", binary_to_decimal, None, "10201")
