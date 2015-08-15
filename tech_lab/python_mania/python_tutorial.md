""" This tutorial is based on python 2.7"""


# Bulitin Functions

### raw\_input()

convert anything typed-in into string

    >>>raw_input()
    >>>test \n \t
    >>>'test \\n \\t'

### input()
Equal to `eval(raw_input())`

    >>>input()
    >>>1 + 1
    >>>2

### pow(a, b)
Equal to a ** b

    >>>pow(2, 3)
    >>>8



# Built-in Modules

## math

### Ceiling a number
Return value is float

    >>>import math
    >>>math.ceil(10.000001)
    >>>11.0
    >>>math.ceil(1)
    >>>1.0

### Floor a number
Return value is float

    >>>import math
    >>>math.floor(9.999999)
    >>>9.0
    >>>math.floor(8)
    >>>8.0

### Get the Square root of a number
Return value is float

    >>>import math
    >>>math.sqrt(9)
    >>>3.0
    >>>math.sqrt(3)
    >>>1.7320508075688772


## cmath
cmath refers to complicate math

### Get the Square root of a negative number
Return value is complicate number

    >>>import cmath
    >>>a = cmath.sqrt(-1)
    >>>a
    1j
    >>>a ** a
    (0.20787957635076193+0j)


## __future__
A module to store features that will be implement in future python.



# Syntaxs

## if condition in 1 line
    >>>if "I'm your daddy": print "I'm your daddy"


###

# DATA TYPES

## String


## Number

### Hexadecimals
Hexadecimals starts with `0x`

    >>>print 0xB
    11

### Octals
Octals starts with arbitary numbers of `0`

    >>>print 011
    9

    >>>0111 == 0000111
    True
