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
        parser = Parser('1+2')
        self.assertEqual(parser.input_string, '1+2', 'Correct input_string.')

    def test_parser_leading_white_input_string(self):
        parser = Parser('    1+2')
        self.assertEqual(parser.input_string, '1+2', 'Testing leading whitespaces.')

    def test_parser_trailing_white_input_string(self):
        parser = Parser(' 1+2      ')
        self.assertEqual(parser.input_string, '1+2', 'Testing trailing whitespaces.')

    def test_parser_mixed_white_input_string(self):
        parser = Parser(' 1   \t  \n \r   \f \v  +2    ')
        self.assertEqual(parser.input_string, '1+2', 'Testing mixed whitespaces.')

    def test_end_of_expression(self):
        parser = Parser('+')
        self.assertRaises(Exception, parser.next_token)

    def test_integer(self):
        parser = Parser('222')
        self.assertEqual(parser.next_token(), '222', 'Testing integer.')

    def test_decimal(self):
        parser = Parser('222.98')
        self.assertEqual(parser.next_token(), '222.98', 'Testing decimal.')
