# -*- coding: utf-8 -*-

"""calc script."""

import sys

from pycalculator import parser


def validate_argv(argv):
    """Validates argv."""
    if len(argv) != 2:
        raise Exception("Incorrect number of parameters.")

if __name__ == "__main__":
    validate_argv(sys.argv)
    p = parser.Parser(sys.argv[1])
