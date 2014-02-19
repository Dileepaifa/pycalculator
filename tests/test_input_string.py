# -*- coding: utf-8 -*-

"""Input string tests."""

import unittest

from pycalculator.calc import validate_argv


class ArgvTestCase(unittest.TestCase):

    """Testing the argv validation."""

    def test_no_argv(self):
        self.assertRaises(TypeError, validate_argv, None)

    def test_empty_list(self):
        self.assertRaises(Exception, validate_argv, [])

    def test_1_element_list(self):
        self.assertRaises(Exception, validate_argv, [""])

    def test_2_element_list(self):
        self.assertIsNone(validate_argv(["", ""]), 'A list of 2 elements')

    def test_3_element_list(self):
        self.assertRaises(Exception, validate_argv, ["", "", ""])
