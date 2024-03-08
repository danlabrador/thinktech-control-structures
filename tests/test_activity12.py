# tests/test_activity12.py

import sys
import os

# Adjust the path to include the directory where test_utils.py is located
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from test_utils import describe
from activity12 import is_palindrome

# Descriptive testing using the improved test_utils.py
if __name__ == "__main__":
    test = describe("Activity 12: Palindrome Checker")

    # Test with a simple palindrome
    test("Simple palindrome", is_palindrome, True, "radar")
    # Test with a non-palindrome
    test("Non-palindrome", is_palindrome, False, "python")
    # Test with a single character (which is a palindrome)
    test("Single character", is_palindrome, True, "a")
    # Test with an empty string (considered a palindrome by some definitions)
    test("Empty string", is_palindrome, True, "")
    # Test with a mixed case palindrome
    test("Mixed case palindrome", is_palindrome, True, "Racecar")
    # Test with spaces and punctuation (should ignore or consider based on implementation)
    test("Phrase palindrome", is_palindrome, True, "A man, a plan, a canal, Panama")
    # Test with a long non-palindrome
    test("Long non-palindrome", is_palindrome, False, "thisisdefinitelynotapalindrome")
    # Test with numeric characters
    test("Numeric palindrome", is_palindrome, True, "12321")
