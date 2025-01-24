"""Unit tests for the max_integer function in max_integer.py."""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ class docstring"""
    def test_max_at_end(self):
        """Test case where the maximum number is at the end"""
        result = max_integer([1, 2, 3, 4, 5])
        self.assertEqual(result, 5)

    def test_max_at_beginning(self):
        """Test case where the maximum number is at the beginning"""
        result = max_integer([5, 4, 3, 2, 1])
        self.assertEqual(result, 5)

    def test_max_in_middle(self):
        """Test case where the maximum number is in the middle"""
        result = max_integer([1, 5, 3, 2, 4])
        self.assertEqual(result, 5)

    def test_one_negative_number(self):
        """Test case with one negative number in the list"""
        result = max_integer([1, -2, 3, 4, 5])
        self.assertEqual(result, 5)

    def test_only_negative_numbers(self):
        """Test case with only negative numbers in the list"""
        result = max_integer([-1, -2, -3, -4, -5])
        self.assertEqual(result, -1)

    def test_list_of_one_element(self):
        """Test case with a list containing one element"""
        result = max_integer([7])
        self.assertEqual(result, 7)

    def test_empty_list(self):
        """Test case for an empty list"""
        result = max_integer([])
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()
