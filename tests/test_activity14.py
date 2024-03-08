# tests/test_activity14.py

import sys
import os

# Adjust the path to include the directory where test_utils.py is located
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from test_utils import describe
from activity14 import generate_collatz_sequence

# Descriptive testing using the improved test_utils.py
if __name__ == "__main__":
    test = describe("Activity 14: Collatz Conjecture Sequence Generator")

    # Test with a starting number that leads to a short sequence
    test("Short sequence", generate_collatz_sequence, [6, 3, 10, 5, 16, 8, 4, 2, 1], 6)
    # Test with a starting number that leads to a longer sequence
    test("Longer sequence", generate_collatz_sequence, [27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242, 121, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732, 866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1], 27)
    # Test with 1 (should return [1] as per the conjecture)
    test("Starting with 1", generate_collatz_sequence, [1], 1)
    # Test with a number that has a direct path to 1
    test("Direct path to 1", generate_collatz_sequence, [2, 1], 2)
    # Test with a larger number
    test("Larger number", generate_collatz_sequence, [52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1], 52)
    # Test with a negative number (should handle gracefully based on implementation)
    test("Negative number", generate_collatz_sequence, [], -5)
