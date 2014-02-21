# -*- coding: utf-8 -*-

"""grammar"""

from pycalculator.parser import Parser


class Analyzer(object):

    def __init__(self, initial_entry):
        self.preanalysis = ''
        self.parser = Parser(initial_entry)

    def next_token(self):
        """Gets the next token and calculates preanalysis."""
        token = self.parser.next_token()
        if token == None:
            self.preanalysis = '$'
        else:
            self.preanalysis = token

    def analyze(self):
        self.next_token()

        result = self.start()

        if self.preanalysis != '$':
            raise Exception('Found ' + self.preanalysis + ', expecting ' + '""')

        return result

    def start(self):
        return self.expression(0)

    def expression(self, amount):
        if self.preanalysis == '$':
            raise Exception('Found $, expecting token')
        result_term = self.term(amount)
        result_eq = self.expression_quote(result_term)
        return result_eq

    def expression_quote(self, left):
        if self.preanalysis == '+':
            self.operator()
            right = self.term(left)
            return self.expression_quote(left + right)
        elif self.preanalysis == '-':
            self.operator()
            right = self.term(left)
            return self.expression_quote(left - right)
        else:
            return left

    def term(self, amount):
        if self.preanalysis == '$':
            raise Exception('Found $, expecting token')
        result_factor = self.factor(amount)
        result_tq = self.term_quote(result_factor)
        return result_tq

    def term_quote(self, left):
        if self.preanalysis == '*':
            self.operator()
            right = self.factor(left)
            return self.term_quote(left * right)
        elif self.preanalysis == '/':
            self.operator()
            right = self.factor(left)
            return self.term_quote(left / right)
        else:
            return left

    def factor(self, amount):
        if self.preanalysis == '$':
            raise Exception('Found $, expecting token')
        result_primary = self.primary(amount)
        result_fq = self.factor_quote(result_primary)
        return result_fq

    def factor_quote(self, left):
        if self.preanalysis == '^':
            self.operator()
            right = self.primary(left)
            return self.factor_quote(left ** right)
        else:
            return left

    def primary(self, amount):
        if self.preanalysis == '$':
            raise Exception('Found $, expecting token')
        elif self.preanalysis == '(':
            # TODO: open parenthesis
            self.operator()
            result = self.expression(amount)  # TODO
            # TODO: close parenthesis
            self.operator()
            return result
        else:
            try:
                float(self.preanalysis)
            except ValueError:
                raise Exception('Found ' + self.preanalysis + 'expecting "(" or number')
            return self.number()

    def number(self):
        if self.preanalysis == '$':
            raise Exception('Found $, expecting token')
        try:
            if '.' in self.preanalysis:
                result = float(self.preanalysis)
            else:
                result = int(self.preanalysis)
        except ValueError:
            raise Exception('Found ' + self.preanalysis + 'expecting number')
        self.next_token()
        return result

    def operator(self):
        if self.preanalysis == '$':
            raise Exception('Found $, expecting token')
        self.next_token()
