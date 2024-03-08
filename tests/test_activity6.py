# tests/test_activity6.py

import sys
import os

# Adjust the path to include the directory where test_utils.py is located
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from test_utils import describe
from activity6 import count_vowels

# Descriptive testing using the improved test_utils.py
if __name__ == "__main__":
    test = describe("Activity 6: Count Vowels in a String")

    # Test with a simple string
    test("Simple string", count_vowels, 2, "hello")
    # Test with an empty string
    test("Empty string", count_vowels, 0, "")
    # Test with all vowels
    test("All vowels", count_vowels, 5, "aeiou")
    # Test with a string with no vowels
    test("No vowels", count_vowels, 0, "bcdfg")
    # Test with mixed case
    test("Mixed case", count_vowels, 4, "HeLlO")
    # Test with a longer sentence
    test("Longer sentence", count_vowels, 11, "The quick brown fox jumps over the lazy dog")
    # Test with numbers and special characters
    test("Numbers and special characters", count_vowels, 3, "123@#aei!456")
    # Test with repeated vowels
    test("Repeated vowels", count_vowels, 8, "aardvark")
