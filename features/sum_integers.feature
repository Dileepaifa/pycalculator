Feature: Sum integers

    When some integers have the '+' symbol between them
    then the calculator must return the sum of those numbers.

    Scenario: Sum of two integers
        Given two integers and the + symbol are provided to the Analyzer
        When the analyze method is called
        Then the sum of those integers is returned
