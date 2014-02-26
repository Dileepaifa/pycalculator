Feature: Multiply integers

    When some integers have the '*' symbol between them
    then the calculator must return the multiplication of those numbers.

    Scenario: Multiplication of two integers
        Given two integers and the * symbol are provided to the Analyzer
        When the analyze method is called
        Then the multiplication of those integers is returned
