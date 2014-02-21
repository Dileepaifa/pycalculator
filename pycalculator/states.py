# -*- coding: utf-8 -*-

"""States."""

STATES = {
    ('S0', 'S1'): {'return_token': False},
    ('S0', 'S3'): {'return_token': False},
    ('S0', 'S4'): {'return_token': False},

    ('S1', 'S1'): {'return_token': False},
    ('S1', 'S11'): {'return_token': False},
    ('S1', 'S3'): {'return_token': True},
    ('S1', 'S4'): {'return_token': True},
    ('S1', 'S5'): {'return_token': True},
    ('S1', 'S6'): {'return_token': True},
    ('S1', 'S7'): {'return_token': True},

    ('S11', 'S2'): {'return_token': False},

    ('S2', 'S2'): {'return_token': False},
    ('S2', 'S3'): {'return_token': True},
    ('S2', 'S4'): {'return_token': True},
    ('S2', 'S5'): {'return_token': True},
    ('S2', 'S6'): {'return_token': True},
    ('S2', 'S7'): {'return_token': True},

    ('S3', 'S1'): {'return_token': True},

    ('S4', 'S1'): {'return_token': True},

    ('S5', 'S1'): {'return_token': True},

    ('S6', 'S1'): {'return_token': True},

    ('S7', 'S1'): {'return_token': True},
}

FINAL_STATES = ['S1', 'S2']


def S0(char):
    if char.isdigit():
        return S1
    elif char == '+':
        return S3
    elif char == '-':
        return S4
    else:
        raise Exception('Unexpected character ' + char)


def S1(char):
    if char.isdigit():
        return S1
    elif char == '+':
        return S3
    elif char == '-':
        return S4
    elif char == '.':
        return S11
    elif char == '*':
        return S5
    elif char == '^':
        return S6
    elif char == '/':
        return S7
    else:
        raise Exception('Unexpected character ' + char)


def S11(char):
    if char.isdigit():
        return S2
    else:
        raise Exception('Unexpected character ' + char)


def S2(char):
    if char.isdigit():
        return S2
    elif char == '+':
        return S3
    elif char == '-':
        return S4
    elif char == '*':
        return S5
    elif char == '^':
        return S6
    elif char == '/':
        return S7
    else:
        raise Exception('Unexpected character ' + char)


def S3(char):
    if char.isdigit():
        return S1
    else:
        raise Exception('Unexpected character ' + char)


def S4(char):
    if char.isdigit():
        return S1
    else:
        raise Exception('Unexpected character ' + char)


def S5(char):
    if char.isdigit():
        return S1
    else:
        raise Exception('Unexpected character ' + char)


def S6(char):
    if char.isdigit():
        return S1
    else:
        raise Exception('Unexpected character ' + char)


def S7(char):
    if char.isdigit():
        return S1
    else:
        raise Exception('Unexpected character ' + char)
