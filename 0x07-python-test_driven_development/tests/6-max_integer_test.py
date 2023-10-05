#!/usr/bin/python3
"""Unittests for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer_positive(self):
        """
        Test when the list contains positive integers.
        """
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_max_integer_mixed(self):
        """
        Test when the list contains mixed positive and negative integers.
        """
        result = max_integer([1, 3, 4, 2, -5, -1])
        self.assertEqual(result, 4)

    def test_max_integer_negative(self):
        """
        Test when the list contains negative integers.
        """
        result = max_integer([-1, -3, -4, -2])
        self.assertEqual(result, -1)

    def test_max_integer_single_element(self):
        """
        Test when the list contains a single element.
        """
        result = max_integer([42])
        self.assertEqual(result, 42)

    def test_max_integer_empty_list(self):
        """
        Test when the list is empty (should return None).
        """
        result = max_integer([])
        self.assertIsNone(result)

    def test_max_integer_duplicate_values(self):
        """
        Test when the list contains duplicate values.
        """
        result = max_integer([3, 3, 3, 3])
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()

