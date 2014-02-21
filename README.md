pycalculator
============

A simple calculator in Python.

It reads a string from the command line and returns the calculation.

Python version: 3.X

Usage:  

<pre>
python pycalculator/calc.py "5+3 -2"  
python pycalculator/calc.py "5+3 -2222     + 55/22.987/44"  
python pycalculator/calc.py "5+3^2"
</pre>  

It currently supports the operators: +, -, *, /, ^

'(' and ')' are included in the grammar, but the parser does not support them yet (work in progress).

Additionally, if we need to add new operations to the calculator we just need to modify the graph of the AFD (states module) and add new rules to the grammar (grammar module).

Tests: python -m unittest discover

Parser
------

The parser is a deterministic finite automaton (DFA).

Grammar
-------

This is the calculator's grammar:  

<pre>
E  --> T | E opadd T  
T  --> F | T opmult F  
F  --> P | F opexp P  
P  --> N | '(' E ')'  
N -->  'integer' | 'decimal'  
opadd  --> '+' | '-'  
opmult --> '*' | '/'  
opexp  --> '^'  
</pre>

This grammar will work correctly with the operator precedence. However, it is left-recursive and the calculator will reed tokens from left to right, so we need to convert it to an equivalent right-recursive grammar:

<pre>
S  --> E  
E  --> T E’  
E’ --> opadd T E’ | ε  
T  --> F T’  
T’ --> opmult F T’ | ε  
F  --> P F’  
F’ --> opexp P F’ | ε  
P  --> N | ( E )  
N  --> ‘integer’ | ‘decimal’  
opadd  --> '+' | '-'  
opmult --> '*' | '/'  
opexp  --> '^'  
</pre>

Parsing
-------

The calculator uses a recursive implementation of a LL parser (top-down).  

Naming the rules:  

<pre>
0   S  --> E  
1   E  --> T E’  
2   E’ --> + T E’  
3   E’ --> - T E’  
4   E' --> ε  
5   T  --> F T’  
6   T’ --> * F T’  
7   T’ --> / F T’  
8   T' --> ε  
9   F  --> P F’  
10  F’ --> ^ P F’  
11  F' --> ε  
12  P  --> N  
13  P  --> ( E )  
14  N  --> 'number'  
</pre>

Parsing table:  

<pre>
    +   -   *   /   ^   num (   )   $  
S   0   0   0   0   0   0   0   0   0  
E   1   1   1   1   1   1   1   1   -  
E'  2   3   4   4   4   4   4   4   4  
T   5   5   5   5   5   5   5   5   -  
T'  8   8   6   7   8   8   8   8   8  
F   9   9   9   9   9   9   9   9   -  
F' 11  11  11  11  10  11  11  11  11  
P   -   -   -   -  -   12  13   -   -  
N   -   -   -   -   -  14   -   -   -  
</pre>

Example: 2 * 5 + 3  

<pre>
Stack       String  
--------------------------  
S $           2 * 5 + 3 $  
E $           2 * 5 + 3 $  
T E'$         2 * 5 + 3 $  
F T'E'$       2 * 5 + 3 $  
P F'T'E'$     2 * 5 + 3 $  
N F'T'E'$     2 * 5 + 3 $  
i F'T'E'$     2 * 5 + 3 $  
F'T'E'$       * 5 + 3 $  
T'E'$         * 5 + 3 $  
* F T'E'$     * 5 + 3 $  
F T'E'$       5 + 3 $  
P F'T'E'$     5 + 3 $  
N F'T'E'$     5 + 3 $  
i F'T'E'$     5 + 3 $  
F'T'E'$       + 3 $  
T'E'$         + 3 $  
E'$           + 3 $  
+ T E'$       + 3 $  
T E'$         3 $  
F T'$         3 $  
P F'T'$       3 $  
N F'T'$       3 $  
i F'T'$       3 $  
F'T'$         $  
T'$           $  
$             $  
</pre>
