# -*- coding: utf-8 -*-

"""Grammar tests."""

import unittest

from pycalculator.grammar import Analyzer


class GrammarTestCase(unittest.TestCase):

    """Grammar tests."""

    def test_grammar_empty_input_string(self):
        analzr = Analyzer("")
        self.assertRaises(Exception, analzr.analyze)

    def test_grammar_0(self):
        analzr = Analyzer("0")
        self.assertEqual(analzr.analyze(), 0, 'Cacl 0.')

    def test_grammar_sum_int(self):
        analzr = Analyzer("2+3")
        self.assertEqual(analzr.analyze(), 5, 'Cacl sum int.')

    def test_grammar_sum_float_1(self):
        analzr = Analyzer("2+3.2")
        self.assertEqual(analzr.analyze(), 5.2, 'Cacl sum float.')

    def test_grammar_sum_float_2(self):
        analzr = Analyzer("3.2+2")
        self.assertEqual(analzr.analyze(), 5.2, 'Cacl sum float.')

    def test_grammar_div_sum_int_float(self):
        analzr = Analyzer("3.2+4/2+6/3")
        self.assertEqual(analzr.analyze(), 7.2, 'Cacl sum and div.')
