"""Unit tests for the max_integer function in max_integer.py."""


import unittest
from max_integer_func import max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function."""
    def test_empty_list(self):
        """Test for an empty list."""
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        """Test for a list with one element."""
        self.assertEqual(max_integer([42]), 42)

    def test_multiple_elements(self):
        """Test for a list with multiple elements."""
        self.assertEqual(max_integer([1, 5, 3, 9, 2]), 9)

    def test_negative_numbers(self):
        """Test for a list with negative numbers."""
        self.assertEqual(max_integer([-1, -5, -3, -9, -2]), -1)

    def test_identical_elements(self):
        """Test for a list where all elements are the same."""
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_non_integer_elements(self):
        """Test for a list with non-integer elements."""
        with self.assertRaises(TypeError):
            max_integer([1, "two", 3])

    def test_large_numbers(self):
        """Test for a list with large numbers."""
        self.assertEqual(max_integer([1000000, 5000000, 99999999]), 99999999)

if __name__ == '__main__':
    unittest.main()