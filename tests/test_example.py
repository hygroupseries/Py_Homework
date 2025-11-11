"""
Test cases for example homework.
"""

import sys
import os

# Add parent directory to path to import homework module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from homework.example import add_numbers, multiply_numbers


def test_add_numbers():
    """Test the add_numbers function."""
    assert add_numbers(2, 3) == 5
    assert add_numbers(0, 0) == 0
    assert add_numbers(-1, 1) == 0
    assert add_numbers(-5, -3) == -8


def test_multiply_numbers():
    """Test the multiply_numbers function."""
    assert multiply_numbers(2, 3) == 6
    assert multiply_numbers(0, 5) == 0
    assert multiply_numbers(-2, 3) == -6
    assert multiply_numbers(-4, -2) == 8


if __name__ == "__main__":
    # Run tests manually
    test_add_numbers()
    test_multiply_numbers()
    print("All tests passed!")
