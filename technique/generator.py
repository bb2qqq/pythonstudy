# A def function which containing a yield is called generator-FUNCTION
# The object returned by calling this function is a generator-ITERATOR

# An iterable is an object that has an __iter__ method which returns an iterator,
# or which defines a __getitem__ method that can take sequential indexes -
# starting from zero (and raises an IndexError when the indexes are no longer valid).
# So an iterable is an object that you can get an iterator from.
# An iterator is an object with a next (Python 2) or __next__ (Python 3) method.

# To master yield, you must understand that when you call the function,
# the code you have written in the function body does not run.

def flatten(nested):
    try:
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested

for i in flatten([1,[2],[[3]]]):
    print i


def advance_flatten(nested):
    try:
        # Don't iterate over string-like objects:
        try: nested + ''
        except TypeError: pass
        else: raise TypeError
        for sublist in nested:
            for element in advance_flatten(sublist):
                yield element
    except TypeError:
        yield nested

def my_flatten(something):
    try:
        for sub_nested in something:    # if iterable, let's go to the loop, if not, return the value by except clause
            try: sub_nested + ''        # test if it is a string
            except TypeError: pass      # if not a string, TypeError occurs, let's continue
            else: raise TypeError       # if it's a string, raise Error so it can be returned
            for element in my_flatten(sub_nested):   #  Recursion to see if the element in sub_nested is still iterable.
                return                         #  This yield is the hardest part to understand

    except TypeError:               # if not iterable, return the value itself
        yield something
