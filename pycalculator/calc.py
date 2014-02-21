#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""calc script."""

import sys

#from pycalculator.parser import Parser
#from pycalculator.operations import operate
from pycalculator.grammar import Analyzer


def validate_argv(argv):
    """Validates argv."""
    if len(argv) != 2:
        raise Exception("Incorrect number of parameters.")

if __name__ == "__main__":
    validate_argv(sys.argv)

    #TOKENS = ['$']
    #p = Parser(sys.argv[1])

    #token = p.next_token()
    #while token != None:
    #    TOKENS.append(token)
    #    token = p.next_token()

    #operate(TOKENS)

    analzr = Analyzer(sys.argv[1])
    print(analzr.analyze())
