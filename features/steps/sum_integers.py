# -*- coding: UTF-8 -*-

"""Sum integers."""

from behave import given, when, then

from pycalculator.grammar import Analyzer


@given('two integers and the {symbol} symbol are provided to the Analyzer')
def step_two_integers_and_the_symbol_are_provided_to_the_Analyzer(context, symbol):
    context.symbol = symbol
    if '+' in symbol:
        context.analzr = Analyzer("2+3")
    elif '*' in symbol:
        context.analzr = Analyzer("2*3")


@when('the analyze method is called')
def step_the_analyze_method_is_called(context):
    context.result = context.analzr.analyze()


@then('the {operation} of those integers is returned')
def step_the_operation_of_those_integers_is_returned(context, operation):
    if 'sum' in operation:
        assert context.result == 5
    elif 'multiplication' in operation:
        assert context.result == 6
