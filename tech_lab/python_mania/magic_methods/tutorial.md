Boom~~~

Magic methods 是那些在满足条件后默默触发而不需要你显式调用的内置methods.  
在python里，所有的运算符号都是`magic_method`，以加法为例。

Because everything in python is an object.  
When you executing `x + y`. You are actually doing `x.__add__(y)`.  
if `x` object do not have `__add__` method, or its `__add__` method doesn't support that type.  
We got an error.

In the following examples, `object.__name__(self)` was abbreviated to form `__name__`


### Operator methods
Below is a `magic_method` mapping for all operands:

      +   __add__
      -   __sub__
      *   __mul__
      //  __floordiv__
      /   __div__
      %   __mod__
      **  __pow__(self, other[, modulo])   # Modulo means after power, you can try calculate a modulo with an optional parameter.
      <<  __lshift__  # Bitwise operator
      >>  __rshift__  # Bitwise operator
      &   __and__     # Bitwise operator
      |   __or__      # Bitwise operator
      ^   __xor__     # Bitwise operator

These are extended assignments:

      +=    __iadd__
      -=    __isub__
      *=    __imul__
      /=    __idiv__
      //=   __ifloordiv__
      %=    __imod__
      **=   __ipow__(self, other[,mudulo])
      <<=   __ilshift__
      >>=   __irshift__
      &=    __iand__
      ^=    __ixor__
      |=    __ior__

Unary Operators:

      -         __neg__
      +         __pos__
      abs()     __abs__
      ~         __invert__
      int()     __int__
      long()    __long__
      float()   __float__
      oct()     __oct__
      hex()     __hex__


Comparison Operators:

    <         __lt__
    <=        __le__
    ==        __eq__
    !=        __ne__
    >=        __ge__
    >         __gt__

### Object Creation

* `__new__(cls, **parameters):`  
Responsible for creating new instances, it is the first method to be executed when creating a new instance.  
You can return any thing in `__new__`, but if its not an instance of the cls, the `__init__` magic method won't execute.  
Below is a endless self-calling hell made by myself:

    class MagicBall(object):
        def __new__(cls):
            return cls()

To make it valid, you need to change `return cls()` to `return super(MagicBall, cls).__new__(cls)`, which will init the instance with `object's __new__` method.  
Here is a workable edition:

    class MagicBall(object):
        def __new__(cls):
            cls.my_attr = 'arbitrary attr'
            return super(MagicBall, cls).__new__(cls)

* `__init__`  
called after `__new__`, it receive the newly created instance as first argument.  If `__init__` returning anything other than None will cause `TypeError`.  



""
