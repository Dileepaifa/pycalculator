# -*- coding: utf-8 -*-

"""pycalculator

    A simple calculator in Python.

    It reads a string from the command line and returns the calculation.

    Python version: 3.X

    Usage: python pycalculator/calc.py "5+3 -2"
           python pycalculator/calc.py "5+3 -2222     + 55/22.987/44"
           python pycalculator/calc.py "5+3^2"

    It currently supports the operators: +, -, *, /, ^

    '(' and ')' are included in the grammar, but the parser does not support
    them yet (work in progress).

    Additionally, if we need to add new operations to the calculator
    we just need to modify the graph of the AFD (states module) and add
    new rules to the grammar (grammar module).

    Tests: python -m unittest discover

    :copyright: (c) 2014 by Julio Vicente Trigo Guijarro.
    :license: BSD, see LICENSE for more details.

"""
__version__ = '0.2.0'
