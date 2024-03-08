# tests/test_activity9.py

import sys
import os

# Adjust the path to include the directory where test_utils.py is located
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from test_utils import describe
from activity9 import char_frequency

# Descriptive testing using the improved test_utils.py
if __name__ == "__main__":
    test = describe("Activity 9: Character Frequency Counter")

    # Test with a simple string
    test("Simple string", char_frequency, {'h': 1, 'e': 1, 'l': 2, 'o': 1}, "hello")
    # Test with an empty string
    test("Empty string", char_frequency, {}, "")
    # Test with a string with mixed case
    test("Mixed case", char_frequency, {'H': 1, 'e': 1, 'l': 2, 'o': 1}, "Hello")
    # Test with a string including spaces and punctuation
    test("Spaces and punctuation", char_frequency, {'a': 2, ' ': 3, 'b': 1, 'c': 1, '!': 1}, "a a b c!")
    # Test with numbers in the string
    test("String with numbers", char_frequency, {'1': 1, '2': 2, 'a': 1}, "12a2")
    # Test with a longer string
    test("Longer string", char_frequency, {'t': 2, 'h': 2, 'e': 3, ' ': 8, 'q': 1, 'u': 2, 'i': 1, 'c': 1, 'k': 1, 'b': 1, 'r': 2, 'o': 4, 'w': 1, 'n': 1, 'f': 1, 'x': 1, 'j': 1, 'm': 1, 'p': 1, 's': 1, 'v': 1, 'l': 1, 'a': 1, 'z': 1, 'y': 1, 'd': 1, 'g': 1}, "the quick brown fox jumps over the lazy dog")
    # Test with a string containing only the same character
    test("String with same character", char_frequency, {'a': 5}, "aaaaa")
    # Test with special characters only
    test("Special characters", char_frequency, {'@': 1, '#': 2, '!': 3}, "@#!!#!")
