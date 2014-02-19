# -*- coding: utf-8 -*-

"""Parser."""

import re

from pycalculator.states import STATES, FINAL_STATES, S0


class Parser(object):

    """Input string parser"""

    def __init__(self, input_string):
        """Creates a new parser."""
        pattern = re.compile(r'\s+')
        self.input_string = re.sub(pattern, '', input_string)  # Delete whites
        self.cursor = 0
        if self.input_string:
            self.token = self.get_current_character()
            self.current_state = S0(self.get_current_character())
            self.increment_cursor()
        else:
            self.token = None
            self.current_state = None

    def get_current_character(self):
        try:
            return self.input_string[self.cursor]
        except IndexError:
            return None

    def increment_cursor(self):
        self.cursor += 1

    def check_end_of_expresion(self, token, state):
        if state not in FINAL_STATES:
                    raise Exception(token + ' cannot be the end of the expression.')

    def next_token(self):
        """Gets the next token from the input string."""
        char = self.get_current_character()
        state = self.current_state

        if char == None:
            if self.token == None:
                return self.token
            else:
                token = ''.join(self.token)
                self.token = None
                self.check_end_of_expresion(token, self.current_state.__name__)
                return token

        while char != None and STATES[state.__name__, state(char).__name__]['return_token'] == False:

            self.token = self.token + char
            self.current_state = self.current_state(char)
            self.increment_cursor()

            char = self.get_current_character()
            state = self.current_state

        token = ''.join(self.token)
        if char != None:
            self.token = char
            self.current_state = self.current_state(char)
            self.increment_cursor()
        else:
            self.token = None

        return token
