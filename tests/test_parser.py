# -*- coding: utf-8 -*-

"""Parser tests."""

import unittest

from pycalculator.parser import Parser


class InputStringTestCase(unittest.TestCase):

    """Parser tests."""

    def test_parser_empty_input_string(self):
        parser = Parser("")
        self.assertFalse(parser.input_string, 'Empty input_string.')

    def test_parser_correct_input_string(self):
        parser = Parser('abcd')
        self.assertEqual(parser.input_string, 'abcd', 'Correct input_string.')
