#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""calc script."""

import sys

from pycalculator.grammar import Analyzer


def validate_argv(argv):
    """Validates argv."""
    if len(argv) != 2:
        raise Exception("Incorrect number of parameters.")

if __name__ == "__main__":
    validate_argv(sys.argv)

    analzr = Analyzer(sys.argv[1])
    print(analzr.analyze())
