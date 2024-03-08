# tests/test_activity5.py

import sys
import os

# Adjust the path to include the directory where test_utils.py is located
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from test_utils import describe
from activity5 import reverse_list

# Descriptive testing using the improved test_utils.py
if __name__ == "__main__":
    test = describe("Activity 5: Reverse a List")

    # Test with a list of integers
    test("List of integers", reverse_list, [5, 4, 3, 2, 1], [1, 2, 3, 4, 5])
    # Test with an empty list
    test("Empty list", reverse_list, [], [])
    # Test with a list of characters
    test("List of characters", reverse_list, ['d', 'c', 'b', 'a'], ['a', 'b', 'c', 'd'])
    # Test with a list containing mixed types
    test("Mixed types", reverse_list, [True, 'hello', 42, None], [None, 42, 'hello', True])
    # Test with a single element list
    test("Single element", reverse_list, [1], [1])
    # Test with a list of strings
    test("List of strings", reverse_list, ["world", "hello"], ["hello", "world"])
    # Test with repetitive elements
    test("Repetitive elements", reverse_list, [2, 2, 2, 2], [2, 2, 2, 2])
