# -*- coding: utf-8 -*-

"""pycalculator: a simple calculator in Python.

    It currently supports the operators: +, -, *, /, **
    Parentheses are not supported yet.
    The parser is a deterministic finite automaton (DFA).
    It reads a string from the command line and returns an element
    (integer, decimal, operator) each time it is called.
    It is prepared to add new operations and scientific functions:
    more states will need to be added to the parser.

    Usage: python pycalculator/calc.py "5+3 -2"
           python pycalculator/calc.py "5+3 -2222     * 55/22.987**44"

    :copyright: (c) 2014 by Julio Vicente Trigo Guijarro.
    :license: BSD, see LICENSE for more details.

"""
__version__ = '0.1.0'
