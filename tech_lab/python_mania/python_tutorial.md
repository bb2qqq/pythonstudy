""" This tutorial is based on python 2.7"""
[Source Code](https://www.python.org/downloads/release/python-2710/)

## Descriptors
Descriptors are assigned to classes.


## Decorators
### what is decorator?
It is a Syntax-Sugar in order to make function/method wrap process more readable.
Decorators looks like this:

    @dec2
    @dec1
    def my_func(*args):
        pass

when you want to use `my_func`, you are actually get the result of `dec2(dec1(func))`.  

### how to use decorator?
So, first you should make sure your decorators definition runs before your own function runs.  
And, then be aware that the decorators were executed starts from the one which is closest to `def` statement.  
Finally you should make sure **after all the decorate processes, you should get something callable**

### decorator features
* When you using decorators, you are actually saying:  
OK, I got a *var_name*, its now refers to a callable object.  
Now I'm going to pass it as an argument to a function.   
It then will pass the result of it to next function. Until the end of the decorators.  
And I will now assign the final result to *var_name*, now matter whatever it is only if it's callable.  

This means, you should take a look of what the decorators do to findout the final result.  
e.g.
    def evil_decorator(_input):
        return curse

    def curse(name):
        print "Fuck you! " + name

    @evil_decorator
    def greetings(name):
        print "Hello! " + name

Guess what will you got when you use `greetings("Mr. White")`?  
* All these processes above runs on the function definition parse-build period.  
That is to say, the decorators will run when the function code is imported/parsed, it won't wait until you call the function.  

* Another thing, you may specified serveral parameters in your original defination, but the final obj which the original name refers to,  
may take 0 parameters, or a bunch of parameters, amazing, isn't it? It all depends on what decorators give back to you.  

* During the decorating process, the original function can only be called with its obj, not with its name.  

    # Called with name, FAILED.
    # RESULT:  "NameError: global name 'print_2' is not defined"
    def switch(func):
        return print_2

    @switch
    def print_2():
        return 2


    # Called with obj,
    # RESULT: "2, returned the obj of print_2 funciton"
    def switch(func):
        func()
        return func

    @switch
    def print_2():
        return 2

This is to say, the name assiging is the last step of a decorating process.


* What if I called the original function in decorators, will it be an infinite loop? The answer is no.  
Only the original function will be triggered, but not the result of all decorate processes.


### decorate maker
The `@` can takes expressions after it, as it the value returned by expression is a func.  
This means you can even use eval after it.  
Here is a long expression decorator using eval:

    def ev(func):
    result = func(555)
    return result

    @eval("[i for i in globals().values() if hasattr(i, '__name__') and i.__name__ == 'ev'][0]")
    def my_print(n):
        def print_n():
            print n
        return print_n


## Bitwise operators
A bitwise operation operates on one or more bit patterns or binary numerals

* ~ (NOT) will reverse 1-0 for a number(if signed int, reverse its sign), `~7` means `reverse +0111`,  
thus we got `-1000`, which is `-8`.

    >>> ~7
    -8

* & (AND) will take two binary numbers, compare every bits of them,  
on each position, only when both number has value 1 on it, set that position to 1, else 0.  
For example. take 5(binary: 101) AND 11(binary: 1011), what we got will be `binary 0001`, that is 1.

    >>> 5 & 11
    1

If you'd like only keep last N bit of a int number, you can use `Bitwise AND` operator to do that:

    def get_last_n_bit(target_number, n):
        filter_number = int("1"*n, 2)
        return filter_number & target_number


* | (OR) is similar to &(And), but it will return 1 for each position if more than one number have value 1 on that position.  
Thus 5(b: 101) OR 11(b: 1011) should be (b: 1111), that is 15.

    >>> 5 | 11
    15

* ^ (XOR) is similar to |(OR), but it returns 1, only when exactly one number has value 1 on that position.  
If two numbers have value 1 on same position will return 0 for that position.  
Thus 5(b: 101) XOR 11(b: 1011) should be (b: 1110), that is 14.  

    >>> 5 ^ 11
    14

For its interesting character, we can use XOR to toggle switch status. Below is a toggleing code.  
    i = 0
    for n in range(6):
        i = i ^ 1
        print i
    1
    0
    1
    0
    1
    0

* >> (RIGHT SHIFT) will shift every bits of a number to right by specified steps, thus we can shrink it.  
If the step exceed max digit positions of that number, the number will be zero.  
e.g. for number 5(b: 101), if we `>>` it by 1, we got `0b10`(2), `>>` it by 2, we got `0b1`(1), etc.

    >>> 5 >> 0
    5
    >>> 5 >> 1
    2
    >>> 5 >> 2
    1
    >>> 5 >> 3
    0
    >>> 5 >> 4
    0

* << (LEFT SHIFT) is similar to RIGHT SHIFT, but on different direction, thus it enlarge the number.  
For 2(b:10), we excpet `2 << 1` to be `b: 100`, which is 4.  
We can inspect an interesting phenonemon, it seems to `<<` a number by `n` steps means to mulitply that number with `2**n`.  
Let's test it:

    def multiply_with_2_powers_n(target_number, n):
        return target_number << n

    for i in range(100):
        for j in range(20):
            assert multiply_with_2_powers_n(i, j) == i * (2**j)

    # TEST PASSED, NO ASSERTION ERROR ARISED

# Built-in Functions

### dir
When called without arguments, return a list of names of current scope.  
If you passed an object to it, it will return a list of names of the attributes of the object.


### `eval` and `exec`

1. `eval` returns the value of expression, `exec` returns `None`.

2. `eval` only accepts single expression, `exec` has no limit.

when the input is `str`, both `eval` and `exec` will use `compile` function to compile it into bytecode first.  
The difference is they'll pass different `mode` arguemnts to `compile`,  
`eval` passes `"eval"`, `exec` passes `"exec"`, and this made up the two different features we listed above.

[Furthur Discussions](http://stackoverflow.com/questions/2220699/whats-the-difference-between-eval-exec-and-compile-in-python)


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

## array

In python, an array is like a list, except it only accept certain types of value.

    >>>import array
    >>>num_array = array.array('i', range(5))
    >>>print num_array
    >>>array('i', [0, 1, 2, 3, 4])

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
### What is AST?
AST is short ofr `Abstract Syntax Tree`.  
It is a tree representation of the abstract syntax structure of a piece of source code.  
Below is a piece of pseudo-code and its AST:

    # CODE
    while b ≠ 0
        if a > b
            a := a − b
        else
            b := b − a
    return a

AST:
![](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Abstract_syntax_tree_for_Euclidean_algorithm.svg/800px-Abstract_syntax_tree_for_Euclidean_algorithm.svg.png)

> [Wiki](https://en.wikipedia.org/wiki/Abstract_syntax_tree)

### Differences between expressions and statement

1. Statemens are anything that can make up a line(or several lines) of python code.

2. Expressions is a subset of statements, it has these features:
    * Produce at least 1 value, the value can be any Python object.
    * Only contain identifiers, literals and operators.
    * Operators include arithmetic and boolean operators, the function call operator () the subscription operator [] and similar,

[Furthur Discussions](http://stackoverflow.com/questions/4728073/what-is-the-difference-between-an-expression-and-a-statement-in-python)

### if condition in 1 line
    >>>if "I'm your daddy": print "I'm your daddy"



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
