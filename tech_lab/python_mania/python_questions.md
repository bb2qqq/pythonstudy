* What is interface in python?

It may have something to do with [Abstract Base Class][1]?
View stackoverflow answer [here][2] and [here][3].


* what is singleton in python?

View doc [here][4]

* what is constructors in python?

In Python, the constructor is split over two methods, "__new__" and "__init__". The __new__ method is responsible for allocating memory for the instance, and receives the class as an argument (conventionally called "cls"). The __init__ method (often called "the initialiser") is passed the newly created instance as an argument (conventionally called "self").

[Definition][5] of constructor.


[1]: https://docs.python.org/2/library/abc.html
[2]: http://stackoverflow.com/questions/1913098/what-is-the-difference-between-an-interface-and-abstract-class
[3]: http://stackoverflow.com/questions/372042/difference-between-abstract-class-and-interface-in-python
[4]: http://python-3-patterns-idioms-test.readthedocs.org/en/latest/Singleton.html
[5]: http://en.wikipedia.org/wiki/Constructor_%28object-oriented_programming%29 
